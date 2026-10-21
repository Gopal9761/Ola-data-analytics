"""Loads the cleaned CSV into SQLite, runs sql/ola_queries.sql and prints the answers."""
import sqlite3, pandas as pd
con = sqlite3.connect(':memory:')
pd.read_csv('data/ola_bookings_clean.csv').to_sql('bookings', con, index=False)
con.executescript(open('sql/ola_queries.sql').read())
views = ['ride_distance_for_each_vehicle','cancelled_rides_by_customers','Top_5_Customers','Rides_cancelled_by_Drivers_P_C_Issues',
         'Max_Min_Driver_Rating','AVG_Cust_Rating','total_successful_ride_value']
for v in views:
    print(f'\n== {v}'); print(pd.read_sql(f'SELECT * FROM {v}', con).to_string(index=False))
for v in ['Successful_Bookings','UPI_Payment','Incomplete_Rides_Reason']:
    print(f'\n== {v}: {pd.read_sql(f"SELECT COUNT(*) n FROM {v}", con).n[0]} rows')
