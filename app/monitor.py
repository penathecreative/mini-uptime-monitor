from apscheduler.schedulers.background import BackgroundScheduler
import requests, json

def check_sites():
    try:
        with open("data/sites.json", "r+") as f:
            data = json.load(f)
            for url in data:
                try:
                    res = requests.get(url, timeout=5)
                    data[url]["status"] = "up" if res.status_code < 400 else "down"
                except Exception as e:
                    print(f"[ERROR] Failed to reach {url}: {e}")
                    data[url]["status"] = "down"
            f.seek(0)
            f.truncate()  # Clear old content before writing
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"[MONITOR ERROR]: {e}")

def start_monitor():
    print("Starting monitor scheduler...")
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_sites, "interval", seconds=60)
    scheduler.start()
