import sqlite3 as sq
from loader import dp

def sql_start():
    global base, cur
    base = sq.connect('PhrasMemory.db')
    cur = base.cursor()
    if base:
        print('ДБ Подлкючена вроде как')
    base.execute(
        'CREATE TABLE IF NOT EXISTS phMemory(category TEXT, phrase TEXT PRIMARY KEY, ph_respond TEXT, rep_inf TEXT)')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO phMemory VALUES (?, ?, ?, ?)',
                    tuple(data.values()))
        base.commit()


async def sql_responder(message):
    for graph in cur.execute('SELECT * FROM phMemory').fetchall():
        if message.text == graph[1]:
            await message.answer(graph[2])

        
        #await dp.bot.send_message(message.from_user.id, f'{graph[0]}, {graph[1]} ,{graph[2]}, {graph[-1]}')