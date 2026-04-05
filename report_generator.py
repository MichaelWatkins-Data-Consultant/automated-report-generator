import sqlite3
import pandas as pd
from datetime import datetime

# Connect to the database
conn = sqlite3.connect('superstore.db')

# --- Query 1: Total Sales and Profit by Region ---
region_query = """
    SELECT 
        Region,
        ROUND(SUM(Sales), 2) as Total_Sales,
        ROUND(SUM(Profit), 2) as Total_Profit,
        COUNT(DISTINCT Order_ID) as Total_Orders
    FROM sales
    GROUP BY Region
    ORDER BY Total_Sales DESC
"""

# --- Query 2: Top 5 Products by Sales ---
product_query = """
    SELECT 
        Product_Name,
        ROUND(SUM(Sales), 2) as Total_Sales,
        ROUND(SUM(Profit), 2) as Total_Profit
    FROM sales
    GROUP BY Product_Name
    ORDER BY Total_Sales DESC
    LIMIT 5
"""

# --- Query 3: Monthly Sales Trend ---
monthly_query = """
    SELECT 
        strftime('%Y-%m', Order_Date) as Month,
        ROUND(SUM(Sales), 2) as Monthly_Sales,
        ROUND(SUM(Profit), 2) as Monthly_Profit
    FROM sales
    GROUP BY Month
    ORDER BY Month DESC
    LIMIT 12
"""

# Run the queries
region_df = pd.read_sql_query(region_query, conn)
product_df = pd.read_sql_query(product_query, conn)
monthly_df = pd.read_sql_query(monthly_query, conn)

conn.close()

# --- Generate the Report ---
report_date = datetime.now().strftime('%Y-%m-%d')
report_filename = f'sales_report_{report_date}.txt'

with open(report_filename, 'w') as f:
    f.write("=" * 60 + "\n")
    f.write(f"  AUTOMATED SALES REPORT — Generated {report_date}\n")
    f.write("=" * 60 + "\n\n")

    f.write("SALES & PROFIT BY REGION\n")
    f.write("-" * 60 + "\n")
    f.write(region_df.to_string(index=False))
    f.write("\n\n")

    f.write("TOP 5 PRODUCTS BY SALES\n")
    f.write("-" * 60 + "\n")
    f.write(product_df.to_string(index=False))
    f.write("\n\n")

    f.write("MONTHLY SALES TREND (Last 12 Months)\n")
    f.write("-" * 60 + "\n")
    f.write(monthly_df.to_string(index=False))
    f.write("\n\n")

print(f"Report generated: {report_filename}")
print("Open the file to see your automated sales report!")