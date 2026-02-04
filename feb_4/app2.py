import sqlite3
import pandas as pd

conn = sqlite3.connect('../baseball.db')
cursor = conn.cursor()
query = """
    SELECT yearID, sum(HR) as yearHRs
    FROM batting
    WHERE teamID = 'PHI'
    GROUP BY yearID
    ORDER BY yearHRs desc
    LIMIT 11
"""

cursor.execute(query)
records = cursor.fetchall()
conn.close()

df = pd.DataFrame(records, columns = ['yearID', 'yearHRs'])
print(df)