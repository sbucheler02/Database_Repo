import sqlite3
import pandas as pd

conn = sqlite3.connect('../baseball.db')
cursor = conn.cursor()
query = """
        SELECT playerID
        FROM batting
        WHERE playerID LIKE 'ch%'
        GROUP BY playerID

"""

cursor.execute(query)
records = cursor.fetchall()
conn.close()
df = pd.DataFrame(records, columns = ['player'])
print(df)