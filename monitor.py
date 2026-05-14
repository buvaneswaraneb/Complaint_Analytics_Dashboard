import requests
import time
import sys

backend = 'https://complaint-analytics-dashboard-k20j.vercel.app/health'
frontend = 'https://complaintanalyticsdashboard.streamlit.app/'

print("Starting deployment monitor...")
for i in range(12):
    try:
        b_res = requests.get(backend, timeout=10)
        f_res = requests.get(frontend, timeout=10)
        print(f"Attempt {i+1}: Backend={b_res.status_code}, Frontend={f_res.status_code}")
        if b_res.status_code == 200 and f_res.status_code == 200:
            print("DEPLOYMENT SUCCESSFUL")
            sys.exit(0)
    except Exception as e:
        print(f"Attempt {i+1}: Waiting for server... ({e})")
    time.sleep(10)
print("DEPLOYMENT STILL IN PROGRESS - Please check manually in a minute.")
