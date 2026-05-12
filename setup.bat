@echo off
cd /d "%~dp0"
python -m venv .venv
call .venv\Scripts\activate
pip install -r requirements.txt
echo.
echo Setup complete. Run run_backend.bat and run_dashboard.bat to start.
pause
