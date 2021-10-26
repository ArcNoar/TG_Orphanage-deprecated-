import sqlite3 as sq
from loader import dp


# TODO ЩА ВСЕ БЛЯТЬ ЭТО ПЕРЕДЕЛЫВАТЬ БУДУ

def sql_start(): # Это все будет сменено и переделано.
    global base, cur
    base = sq.connect('PhrasMemory.db')
    cur = base.cursor()
    if base:
        print('ДБ Подключена вроде как')
    base.execute(
        'CREATE TABLE IF NOT EXISTS ph_keys(Категория TEXT, Фраза TEXT , репутация TEXT)') 
    base.execute(
        'CREATE TABLE IF NOT EXISTS ph_respond(Категория TEXT, Ответ TEXT , репутация TEXT)') 

    base.commit()


async def sql_add_command(batch_list):
    """
    batch_list = [['Category','Phrase','Answer','Rep'],['Category2','Phrase2','Answer2','Rep2']]
    """
    try:

        for batch in batch_list:
            #general
            category_value = batch[0]
            rep_value = batch[3]
            #ph_keys table
            key_value = batch[1]
            #ph_respond table
            respond_value = batch[2]

            cur.execute('INSERT INTO ph_keys VALUES(?, ?, ?)', 
                        ('{}'.format(category_value),'{}'.format(key_value),'{}'.format(rep_value))) # Добавление в PH_KEYS
            base.commit()
            cur.execute('INSERT INTO ph_respond VALUES(?, ?, ?)',
                        ('{}'.format(category_value),'{}'.format(respond_value),'{}'.format(rep_value))) # Добавление в PH_RESPOND
            base.commit()
    except:
        print('Не удалось загрузить батч в ДБ. Предоставленный батч не является списком')


async def sql_responder(message):
    pass

