
from datetime import datetime
import json
import os

def run_bot():
    print("SMART EARNING BOT STARTED")

    report = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "status": "Running",
        "earning": 0,
        "tasks_found": 0,
        "message": "No verified paid tasks recorded yet."
    }

    os.makedirs("reports", exist_ok=True)

    filename = f"reports/report_{report['date']}.json"

    with open(filename, "w") as file:
        json.dump(report, file, indent=4)

    print("Daily report generated successfully!")

if __name__ == "__main__":
    run_bot()
