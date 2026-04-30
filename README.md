# 🌦️ Weather Data Pipeline

## Overview

I built this project to understand how a simple API script can be turned into a structured data pipeline. Instead of just fetching weather data, the goal was to process it, store it properly, and track how the system runs over time.

The pipeline collects real-time weather data, analyzes it, and stores it in both a CSV file and a SQLite database. It also logs each run so it's easier to see when the pipeline executed and whether it worked correctly.

---

## Project Structure

* `fetch.py` – gets data from the weather API
* `process.py` – converts raw data into a structured format
* `storage.py` – saves data to CSV
* `db.py` – handles database storage and pipeline tracking
* `main.py` – runs the full pipeline

---

## How the Pipeline Works

The pipeline follows a simple flow:

Fetch → Process → Analyze → Store → Track

Each part is separated into its own file so the system is easier to understand and extend.

---

## Features

* Fetches real-time weather data from an API
* Processes data using pandas
* Stores data in:

  * CSV (for backup)
  * SQLite database (main storage)
* Prevents duplicate entries using timestamps
* Tracks each pipeline run (time, status, rows inserted)
* Generates basic analytics:

  * average temperature
  * max and min temperature
  * average wind speed

---

## Example Output

![Weather Output](weather.png)

---

## Technologies Used

* Python
* pandas
* SQLite
* requests

---

## Limitations

* Only captures current weather (no historical dataset yet)
* Runs manually (not automated)
* No dashboard or visualization

---

## Takeaway

This project helped me understand how data flows through a system—from collection to storage to analysis. It also gave me experience organizing code into a modular pipeline instead of writing everything in one script.
