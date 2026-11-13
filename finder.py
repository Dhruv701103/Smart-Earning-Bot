
import json
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

API_URL = "https://remoteok.com/api"

KEYWORDS = [
    "ai", "data annotation", "data labeling",
    "machine learning", "research",
    "evaluator", "transcription", "python"
]

def find_opportunities():
    print("Searching public remote job listings...")

    request = urllib.request.Request(
        API_URL,
        headers={"User-Agent": "Smart-Earning-Bot/1.0"}
    )

    with urllib.request.urlopen(request, timeout=30) as response:
        jobs = json.loads(response.read().decode("utf-8"))

    matches = []

    for job in jobs:
        if not isinstance(job, dict):
            continue

        title = job.get("position", "")
        description = job.get("description", "")
        tags = " ".join(job.get("tags", []))
        text = f"{title} {description} {tags}".lower()

        if not job.get("url"):
            continue

        if any(word in text for word in KEYWORDS):
            matches.append({
                "title": title,
                "company": job.get("company", "Not listed"),
                "location": job.get("location", "Not listed"),
                "salary": job.get("salary", "Not disclosed"),
                "source": "Remote OK",
                "url": job["url"]
            })

    Path("reports").mkdir(exist_ok=True)

    report = {
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "source": API_URL,
        "opportunities_found": len(matches),
        "opportunities": matches
    }

    filename = datetime.now(timezone.utc).strftime(
        "reports/opportunities_%Y-%m-%d.json"
    )

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)

    print("Opportunities found:", len(matches))
    print("Report saved:", filename)

if __name__ == "__main__":
    find_opportunities()
