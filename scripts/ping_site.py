import os
import time
import json
import datetime
import requests

URL = "https://old.reddit.com/r/Btechtards/"

BASE_DIR = os.path.abspath(os.path.dirname(__file__) + os.sep + "..")
DATA_DIR = os.path.join(BASE_DIR, "data")
JSON_PATH = os.path.join(DATA_DIR, "site_data.json")
HTML_PATH = os.path.join(DATA_DIR, "site_data.html")


def ensure_data_dir():
    os.makedirs(DATA_DIR, exist_ok=True)


def load_data():
    if os.path.exists(JSON_PATH):
        try:
            with open(JSON_PATH, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []


def save_data(data):
    with open(JSON_PATH, "w") as f:
        json.dump(data, f, indent=2)


def generate_html(data):
    html = []
    html.append("<table border='1' cellpadding='5' cellspacing='0'>")
    html.append("<tr><th>Timestamp</th><th>Status Code</th><th>Response Time (s)</th></tr>")
    for entry in data:
        ts = entry.get("timestamp")
        dt = datetime.datetime.fromtimestamp(ts).isoformat() if ts else ""
        status = entry.get("status_code", "")
        resp_time = entry.get("response_time", "")
        html.append(f"<tr><td>{dt}</td><td>{status}</td><td>{resp_time}</td></tr>")
    html.append("</table>")
    with open(HTML_PATH, "w") as f:
        f.write("\n".join(html))


def main():
    ensure_data_dir()
    data = load_data()
    start = time.time()
    try:
        resp = requests.get(URL, timeout=10)
        resp_time = time.time() - start
        status = resp.status_code
    except requests.RequestException:
        resp_time = None
        status = None
    entry = {
        "timestamp": int(time.time()),
        "status_code": status,
        "response_time": round(resp_time, 3) if resp_time is not None else None
    }
    data.append(entry)
    save_data(data)
    generate_html(data)


if __name__ == "__main__":
    main()
