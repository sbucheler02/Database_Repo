import sqlite3
import pandas as pd
import gradio as gr

conn = sqlite3.connect('../baseball.db')
cursor = conn.cursor()
query = """
        WITH top_hitters AS (SELECT nameFirst, nameLast
        FROM batting INNER JOIN people
        ON batting.playerID = people.playerID
        WHERE teamID = 'PHI'
        GROUP BY batting.playerID
        ORDER BY sum(HR) desc
        LIMIT 10)

        SELECT CONCAT (nameFirst, ' ', nameLast) AS player
        FROM top_hitters
        ORDER BY nameLast

"""

cursor.execute(query)
records = cursor.fetchall()
conn.close()

players_list = []
for player in records:
    players_list.append(player[0])
print(players_list)

with gr.Blocks() as iface:
    players = gr.Dropdown(choices = players_list, label = 'Select Player')

iface.launch()