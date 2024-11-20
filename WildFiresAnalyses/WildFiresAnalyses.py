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
#data.to_csv('./output_data.csv', index=False)  # Save as CSV

##Fire count by state
#queryState = 'SELECT STATE, COUNT(*) AS fire_count FROM Fires GROUP BY STATE'
#dataState = pd.read_sql_query(queryState, conn)
#dataState_sorted = dataState.sort_values(by = 'fire_count', ascending = False)
##Print to Console
#for index, row in dataState_sorted.iterrows():
#    print(f"State: {row['STATE']}, Number of Fires: {row['fire_count']}")

#Export to CSV
#dataState.to_csv('./state_count', index=False)



#Total number of fires per year
#Try uploading a SQL file
#Use connection string
#cursor = conn.cursor();

#with open("Num_Fires_Per_Year.sql", "r") as file:
#    sql_script = file.read()

##Executes sql command in SQL file
#cursor.execute(sql_script)

##Fetch all results and print them
#results =cursor.fetchall()
#for row in results:
#    print(f"Year: {row[0]}, Number: {row[1]}")

## Commit changes to file and close the connection

#conn.close()

#Total number of fires per year excel file for Tableau
queryState = 'SELECT FIRE_YEAR, COUNT(*) AS NumberOfFires FROM Fires GROUP By FIRE_YEAR ORDER By FIRE_YEAR'
dataState = pd.read_sql_query(queryState, conn)
dataState_sorted = dataState.sort_values(by = 'FIRE_YEAR', ascending = True)
#Print to Console
#for index, row in dataState_sorted.iterrows():
#    print(f"Year: {row[0]}, Number: {row[1]}")

#Export to CSV
dataState.to_csv('./num_per_year.csv', index=False)


