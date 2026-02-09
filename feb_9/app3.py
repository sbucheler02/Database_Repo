import sqlite3
import pandas as pd

conn = sqlite3.connect('../baseball.db')
cursor = conn.cursor()
query = """
        SELECT teamID, sum(HR)
        FROM batting
        WHERE yearID = 2025
        GROUP BY teamID
        HAVING sum(HR) >= 200

"""

cursor.execute(query)
records = cursor.fetchall()
conn.close()

print(records)

df = pd.DataFrame(records, columns = ['team', 'homeruns'])
print(df)