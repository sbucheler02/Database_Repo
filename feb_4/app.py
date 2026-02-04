import sqlite3
import pandas as pd

conn = sqlite3.connect('../baseball.db')
cursor = conn.cursor()
query = """
    SELECT playerID, sum(HR) as careerHR
    FROM batting
    GROUP BY playerID
    ORDER BY careerHR desc
    LIMIT 10
"""

cursor.execute(query)
records = cursor.fetchall()
conn.close()

df = pd.DataFrame(records, columns = ['playerID', 'careerHR'])
print(df)