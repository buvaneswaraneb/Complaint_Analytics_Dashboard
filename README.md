# 📊 Complaint Analytics Dashboard

A professional, full-stack real-time public service complaint intelligence dashboard. This application features a **FastAPI backend** hosted on **Vercel** and a **Streamlit frontend** hosted on **Streamlit Community Cloud**.

---

## 🚀 Live Production Links

- **Dashboard (Frontend):** [https://complaintanalyticsdashboard.streamlit.app/](https://complaintanalyticsdashboard.streamlit.app/)
- **API (Backend):** [https://complaint-analytics-dashboard-k20j.vercel.app/docs](https://complaint-analytics-dashboard-k20j.vercel.app/docs)

---

## ✨ Features

- **Professional UI/UX** — Modern SVG icons and Mac-style hover zoom effects on KPI cards.
- **FastAPI Integration** — Robust backend logic for data management and analytics.
- **KPI Cards** — Real-time metrics for total complaints, closure rates, and average resolution times.
- **Interactive Charts** — Visualized trends using Plotly (Monthly trends, category distribution, area summaries).
- **Secure Admin Panel** — Snappy, 2-step authentication (Username + Password) with auto-advance transitions.
- **Resilient Architecture** — Hybrid data loading (Vercel API with local SQLite fallback for high availability).

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | [Streamlit](https://streamlit.io/) |
| **Backend** | [FastAPI](https://fastapi.tiangolo.com/) |
| **Deployment** | [Vercel](https://vercel.com/) & [Streamlit Cloud](https://streamlit.io/cloud) |
| **Charts** | [Plotly](https://plotly.com/python/) |
| **Database** | SQLite |
| **Styling** | Custom CSS + Inter Google Font |

---

## 📁 Project Structure

```
Complaint_Analytics_Dashboard/
├── api/
│   └── index.py              # Vercel Serverless Entry Point
├── backend/
│   ├── main.py               # FastAPI application core
│   ├── analytics.py          # Business intelligence logic
│   └── database.py           # Database management (SQLite)
├── data/
│   └── sample_complaints.csv # Initial seed data
├── streamlit_app.py          # Main Streamlit Dashboard (Production)
├── requirements.txt          # Python dependencies
└── vercel.json               # Vercel deployment configuration
```

---

## 🔐 Admin Access

The admin panel allows updating and deleting complaint records.

| Field | Value |
|-------|-------|
| Username | `admin` |
| Password | `admin123` |

---

## 👤 Author

**Adithyan KS**
- GitHub: [@adithyanks2005](https://github.com/adithyanks2005)

---

<div align="center">
  Built with ❤️ by Adithyan KS
</div>
