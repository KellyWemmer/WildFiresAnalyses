import sqlite3
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

conn = sqlite3.connect(r'.\WildFires.db')

# Query the data
query =  'SELECT NWCG_GENERAL_CAUSE, COUNT(*) AS cause_count FROM Fires GROUP BY NWCG_GENERAL_CAUSE'
  # Replace with your query
data = pd.read_sql_query(query, conn)

# Export to CSV
data.to_csv('./output_data.csv', index=False)  # Save as CSV

#Fire count by state
queryState = 'SELECT STATE, COUNT(*) AS fire_count FROM Fires GROUP BY STATE'
dataState = pd.read_sql_query(queryState, conn)
dataState_sorted = dataState.sort_values(by = 'fire_count', ascending = False)
#Print to Console
for index, row in dataState_sorted.iterrows():
    print(f"State: {row['STATE']}, Number of Fires: {row['fire_count']}")

#Export to CSV
#dataState.to_csv('./state_count', index=False)
