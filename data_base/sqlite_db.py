from os import curdir
import sqlite3 as sq
import turtle

def sql_start():
    global base, cur
    base = sq.connect('mosoblcb.db')
    cur = base.cursor()
    if base:
        print('Подключение в БД успешно')
    base.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, id_user INT, firstName TEXT, lastName TEXT, name_device TEXT, description TEXT, photo_inventar TEXT, photo_puth TEXT, contact_user TEXT, appeal TEXT )')
    base.commit

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO users VALUES (null, ?, ?, ?, ?, ?, ?, ?, ?, ?)', tuple(data.values()))
        base.commit()