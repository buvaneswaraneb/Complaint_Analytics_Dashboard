from __future__ import annotations

import sqlite3
from pathlib import Path
from threading import Lock

import pandas as pd


import os

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
CSV_PATH = DATA_DIR / "sample_complaints.csv"

if os.getenv("VERCEL"):
    DB_PATH = Path("/tmp/complaints.db")
else:
    DB_PATH = DATA_DIR / "complaints.db"

# Guard so init_db only runs its expensive checks once per process
_db_initialised = False
_init_lock       = Lock()


def get_connection() -> sqlite3.Connection:
    """Return a thread-safe SQLite connection with WAL mode and Row factory."""
    connection = sqlite3.connect(DB_PATH, check_same_thread=False)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA journal_mode=WAL")
    connection.execute("PRAGMA synchronous=NORMAL")
    return connection


def init_db() -> None:
    """Initialise the database exactly once per process."""
    global _db_initialised
    if _db_initialised:
        return
    with _init_lock:
        if _db_initialised:          # double-checked locking
            return
        if not os.getenv("VERCEL"):
            DATA_DIR.mkdir(exist_ok=True)
        with get_connection() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS complaints (
                    id           TEXT PRIMARY KEY,
                    created_date TEXT NOT NULL,
                    closed_date  TEXT,
                    area         TEXT NOT NULL,
                    category     TEXT NOT NULL,
                    priority     TEXT,
                    status       TEXT NOT NULL DEFAULT 'Pending',
                    description  TEXT NOT NULL
                )
                """
            )
            migrate_schema(connection)
            count = connection.execute("SELECT COUNT(*) FROM complaints").fetchone()[0]
            if count == 0:
                seed_complaints(connection)
        _db_initialised = True


def migrate_schema(connection: sqlite3.Connection) -> None:
    columns = {
        row["name"]: dict(row) for row in connection.execute("PRAGMA table_info(complaints)").fetchall()
    }
    needs_rebuild = (
        columns.get("closed_date", {}).get("notnull") == 1
        or columns.get("priority", {}).get("notnull") == 1
    )
    if not needs_rebuild:
        return

    connection.execute(
        """
        CREATE TABLE complaints_new (
            id           TEXT PRIMARY KEY,
            created_date TEXT NOT NULL,
            closed_date  TEXT,
            area         TEXT NOT NULL,
            category     TEXT NOT NULL,
            priority     TEXT,
            status       TEXT NOT NULL DEFAULT 'Pending',
            description  TEXT NOT NULL
        )
        """
    )
    connection.execute(
        """
        INSERT INTO complaints_new (
            id, created_date, closed_date, area, category, priority, status, description
        )
        SELECT
            id,
            created_date,
            NULLIF(closed_date, ''),
            area,
            category,
            NULLIF(priority, ''),
            status,
            description
        FROM complaints
        """
    )
    connection.execute("DROP TABLE complaints")
    connection.execute("ALTER TABLE complaints_new RENAME TO complaints")


def seed_complaints(connection: sqlite3.Connection) -> None:
    df = pd.read_csv(CSV_PATH)
    df.to_sql("complaints", connection, if_exists="append", index=False)


def read_complaints_df() -> pd.DataFrame:
    init_db()
    with get_connection() as connection:
        return pd.read_sql_query("SELECT * FROM complaints", connection)


def row_to_dict(row: sqlite3.Row | None) -> dict[str, object] | None:
    if row is None:
        return None
    return dict(row)
