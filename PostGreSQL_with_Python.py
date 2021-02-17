import psycopg2 as pg2

# Connect to postgres
conn = pg2.connect(database='dvdrental', user='postgres', password=********)

# Make cusor connection to execute SQL queries
cur = conn.cursor()

# Execute
cur.execute('SELECT * FROM payment')

# First row of data
cur.fetchone()

# Fetch as much as I need
cur.fetchmany(10) -  # Returns as list of tuples and specifies data time

# Close it
connc.close()
