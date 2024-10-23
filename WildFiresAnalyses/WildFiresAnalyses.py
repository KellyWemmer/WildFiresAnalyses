import sqlite3
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

#conn = sqlite3.connect(r'C:\Users\Kelly\Desktop\WildFires/WildFires.db')



#query = 'SELECT NWCG_GENERAL_CAUSE, COUNT(*) AS cause_count FROM Fires GROUP BY NWCG_GENERAL_CAUSE'

#df = pd.read_sql_query(query, conn)

#conn.close()

##print(df.head())

#plt.figure(figsize=(6,4))
#plt.bar(df['NWCG_GENERAL_CAUSE'], df['cause_count'], color = 'skyblue')
#plt.xlabel('Fire Cause')
#plt.ylabel("Number of Fires")
#plt.title('Number of Fires by Cause')
#plt.xticks(rotation=45, ha='right')

#plt.tight_layout()
#plt.show()


conn = sqlite3.connect(r'C:\Users\Kelly\Desktop\WildFires\WildFires.db')


# Query the data
query =  'SELECT NWCG_GENERAL_CAUSE, COUNT(*) AS cause_count FROM Fires GROUP BY NWCG_GENERAL_CAUSE'
  # Replace with your query
data = pd.read_sql_query(query, conn)

# Export to CSV
#data.to_csv('C:\Users\Kelly\Desktop\WildFires\output_data.csv', index=False)  # Save as CSV
data.to_csv('C:/Users/Kelly/Desktop/WildFires/output_data.csv', index=False)  # Save as CSV
# Or export to Excel
#data.to_excel('output_data.xlsx', index=False)  # Save as Excel

