from flask import Flask, render_template, send_file,jsonify
from datetime import datetime, timedelta
import csv
import os

app = Flask(__name__)

DATA_FILE = './data.txt'

from flask import jsonify

@app.route("/table")
def table():
    data = read_data()
    return render_template("table.html", data=data)

@app.route("/api/data")
def api_data():
    all_data = read_data()
    now = datetime.now()
    one_minute_ago = now - timedelta(seconds=120)

    filtered = [
        {"date": entry["date"], "temperature": entry["temperature"]}
        for entry in all_data
        if entry["timestamp"] >= one_minute_ago
    ]
    return jsonify(filtered)

def read_data():
    data = []
    try:
        with open(DATA_FILE, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if "date" in row and "temperature" in row:
                    try:
                        temp = int(row["temperature"])
                        timestamp = datetime.strptime(row["date"], "%Y-%m-%d_%H:%M:%S")
                        data.append({
                            "date": row["date"],
                            "timestamp": timestamp,
                            "temperature": temp
                        })
                    except (ValueError, KeyError):
                        continue
    except Exception as e:
        print("Error reading file:", e)
    return data

@app.route("/")
def index():
    data = read_data()
    dates = [entry["date"] for entry in data]
    temps = [entry["temperature"] for entry in data]
    return render_template("index.html", data=data, dates=dates, temps=temps)

@app.route("/download")
def download_file():
    if os.path.exists(DATA_FILE):
        return send_file(DATA_FILE, as_attachment=True)
    else:
        return "Data file not found", 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

