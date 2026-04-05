import sqlite3
import pandas as pd

# Load the CSV file
df = pd.read_csv('Sample - Superstore.csv', encoding='latin1')

# Clean up column names (remove spaces)
df.columns = df.columns.str.strip().str.replace(' ', '_')

# Connect to SQLite database (creates it if it doesn't exist)
conn = sqlite3.connect('superstore.db')

# Load the data into a table called 'sales'
df.to_sql('sales', conn, if_exists='replace', index=False)

print(f"Database created successfully!")
print(f"Total records loaded: {len(df)}")
print(f"Columns: {list(df.columns)}")

conn.close()