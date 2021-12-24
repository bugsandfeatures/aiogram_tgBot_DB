import sqlite3
import re

async def add(item):
    connect = sqlite3.connect('db.db')
    cursor = connect.cursor()
    m = []
    m.append(item)
    cursor.execute('INSERT INTO shop VALUES(?)', m)
    connect.commit()
    cursor.close()

async def buy():
    connect = sqlite3.connect('db.db')
    cursor = connect.cursor()
    query = 'SELECT * FROM shop'
    cursor.execute(query)
    data = cursor.fetchall()
    m = []

    for i in data:
        m.append(i)

    l = len(data)
    g = []

    for i in range(l):
        a = re.sub('|\(|\'|\,|\)', '', str(m[i]))
        g.append(a)
    c = []


    for i in g:
        q = i + '\n'
        c.append(q)

    v = '\n'.join(c)
    return v