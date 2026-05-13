import psycopg2

# Connect to the database
conn = psycopg2.connect(
    host="localhost",
    database="financial_dashboard",
    user="postgres" ,
    password="236966"
)

# Create a cursor
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM expenses;")

# Fetch all rows
rows = cur.fetchall()

# Print each row
for row in rows:
    print(row)

# Clean up
cur.close()
conn.close()