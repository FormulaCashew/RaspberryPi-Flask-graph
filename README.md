# Raspberry Pi Flask Web App - Temperature Data Viewer

This project is a lightweight web application that runs on a Raspberry Pi using Flask. It reads temperature data from a `.txt` file, displays it in a table, and visualizes it with a line chart using Chart.js.

---

## File Structure

project/
├── app.py
├── data.txt
├── templates/
│ └── index.html
├── static/ # (optional, for extra CSS/JS)
└── README.md

---

## Requirements

- Python 3.x
- Flask
- A Raspberry Pi (or any Linux machine)

### Install python3 app.py


```bash
pip install flask
```
## data.txt Format

Date,Temperature
2025-06-05 11:00:06,49
2025-06-05 11:00:08,50
2025-06-05 11:00:10,48
...

- Use comma-separated values

- Each line contains a datetime and a temperature (°C)

- The first line is the header

## Run the app
```bash
python3 app.py

```

Open a browser and go to

```bash
http://<your-raspberry-pi-ip>:5000
```

# What it does
Reads and parses data.txt

- Displays a line chart (datetime vs temperature)

- Shows a data table with all records

- Responsive frontend with Bootstrap + Chart.js
