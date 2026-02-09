import sqlite3
import pandas as pd

conn = sqlite3.connect('../baseball.db')
cursor = conn.cursor()
query = """
        SELECT yearID, sum(HR) as yearHRs
        FROM batting
        WHERE teamID = 'PHI'
        GROUP BY yearID
        ORDER BY -yearID
        LIMIT 10

"""

cursor.execute(query)
records = cursor.fetchall()
conn.close()
df = pd.DataFrame(records, columns = ['year', 'HRs'])
print(df)