import sqlite3
import gradio as gr

def fetch_phillies():
    conn = sqlite3.connect('../baseball.db')
    cursor = conn.cursor()

    query = '''SELECT playerID
    FROM batting
    WHERE yearID = 1976 AND teamID = 'PHI'

    '''

    cursor.execute(query)
    records = cursor.fetchall()
    conn.close()

    players = []
    for record in records:
        players.append(record[0])

    return players

def f(player):
    conn = sqlite3.connect('../baseball.db')
    cursor = conn.cursor()

    query = '''SELECT HR
    FROM batting
    WHERE playerID = ? AND yearID = 1976 AND teamID= 'PHI'

    '''

    cursor.execute(query, [player])
    records = cursor.fetchall()
    conn.close()

    return records[0][0]

print(f("schmimi01"))

with gr.Blocks() as iface:
    player = gr.Dropdown(label = "Player ID:", choices = fetch_phillies(), interactive= True)
    homeruns = gr.Number(label = "Homeruns Hit:")
    player.change(fn = f, inputs = [player], outputs = [homeruns])

iface.launch()