# Automated Sales Report Generator

## The Problem

Small business owners and operations teams waste hours every week
manually pulling data, calculating totals, and building reports by hand.
The process is slow, error-prone, and pulls smart people away from
actual decision-making.

## The Solution

A Python and SQL pipeline that automatically:

- Ingests raw sales data into a SQLite database
- Runs SQL queries to aggregate sales, profit, and trends
- Generates a clean formatted report — named and dated automatically
- Runs in seconds with zero manual steps

## The Result

What used to take hours of manual work now runs in seconds.
The report is always consistent, always accurate, and requires
no human intervention to produce.

## How It Works

1. `setup_database.py` — loads raw CSV data into a SQLite database
2. `report_generator.py` — queries the database and generates the report

## Sample Output

The report automatically produces:

- Sales and profit breakdown by region
- Top 5 products by revenue
- Monthly sales trend for the last 12 months

## Tools Used

Python · SQL · SQLite · Pandas

## How To Run

```bash
# Step 1 - Set up the database
python3 setup_database.py

# Step 2 - Generate the report
python3 report_generator.py
```

A dated report file will appear in your folder automatically.
