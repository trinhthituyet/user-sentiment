import sqlite3

class TrendDB():
    def __init__(self):
        self.conn = sqlite3.connect('example.db')
        self.cursor = self.conn.cursor()

    def insert_trend(self, trend):
        self.cursor.execute("INSERT INTO trends (name, tweet_volume, timestamp) VALUES (?, ?, ?)", 
                            (trend['name'], trend['tweet_volume'], trend['timestamp']))
        self.conn.commit()