@echo off
cd /d "%~dp0"
if not exist ".venv\Scripts\activate.bat" (
  echo Virtual environment not found. Run setup.bat first.
  pause
  exit /b
)
call .venv\Scripts\activate
python -m streamlit run frontend\streamlit_app.py
pause
