import sqlite3
import csv

conn = sqlite3.connect("mtgoxUSD.s3")
c = conn.cursor()
c.execute(""" 
    CREATE TABLE IF NOT EXISTS mtgoxUSD (time INT, price FLOAT, trades FLOAT);
    """)

for i, row in enumerate(open("mtgoxUSD.csv", "rb")):
    row = row[:-1].split(",")
    c.execute("INSERT INTO mtgoxUSD VALUES (?, ?, ?)", row)
    if i % 50000 == 0:
        print i
        conn.commit()

conn.commit()
conn.close()

