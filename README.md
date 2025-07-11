# Land Measurement Automation 🗺️

This project automates the process of calculating elevation differences and status (RISE/FALL) between survey points using Python.

## Features

- Mid thread validation (top, mid, bottom input)
- Calculate elevation & height difference automation
- Distance input between points
- Automatic status check (RISE or FALL)
- Export result to Excel .xlsx format
- Neatly formatted table output in terminal

## How It Works

1. User enters number of points and initial AMSL elevation.
2. For each point pair:
   - Input backsight and foresight using thread readings
   - Mid-thread is validated automatically
   - Elevation difference is calculated
   - Status is shown (RISE/FALL)
3. Final result can be exported to Excel

## Requirements

- Python 3.x
- pandas library
- tabulate library

Install via:
```bash
pip install pandas tabulate
