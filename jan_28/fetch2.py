import sqlite3
import pandas as pd

conn = sqlite3.connect('baseball.db')
cursor = conn.cursor()

query = '''
        SELECT playerID, teamID, yearID, HR
        FROM batting
        WHERE HR > 20 AND (yearID = 1976 OR yearID = 1980);
'''

cursor.execute(query)
records = cursor.fetchall()
conn.close()

records_df = pd.DataFrame(records, columns = ['playerID', 'teamID', 'yearID', 'HR'])

print(records_df)