import sqlite3 as sq
from loader import dp

base = sq.connect('PhrasMemory.db')
cur = base.cursor()

def sql_start(): # Это все будет сменено и переделано.
    if base:
        print('ДБ Подключена вроде как')
    base.execute(
        'CREATE TABLE IF NOT EXISTS ph_keys(Категория TEXT, Фраза TEXT , репутация TEXT)') 
    base.execute(
        'CREATE TABLE IF NOT EXISTS ph_respond(Категория TEXT, Ответ TEXT , репутация TEXT)') 

    base.commit()


def get_words(category): # Достать все ответы из дб

    r = None
    if category == None:
        r = cur.execute('SELECT Ответ FROM ph_respond').fetchall()
    else:
        r = cur.execute(
            'SELECT Ответ FROM ph_respond WHERE Категория == ?', (category,)).fetchall()
    return r


def get_keys(category): # Достать все ключи из дб

    r = None
    if category == None:
        r = cur.execute('SELECT Фраза FROM ph_keys').fetchall()
    else:
        r = cur.execute(
            'SELECT Фраза FROM ph_keys WHERE Категория == ?', (category,)).fetchall()
    return r


def get_tags(): # Достать все категории из дб

    r = cur.execute('SELECT Категория FROM ph_keys').fetchall()
    return r

def get_XY(): # Достать все КАТЕГОРИЯ - КЛЮЧ

    r = cur.execute('SELECT Категория, Фраза FROM ph_keys').fetchall()
    return r


def sql_remember(some_list):
    """
    some_list = ['',user_message,'','']

    """
    category_value = some_list[0]
    id_value = some_list[3]
    #ph_keys table
    key_value = some_list[1]
    #ph_respond table
    respond_value = some_list[2]
    cur.execute('INSERT INTO ph_keys VALUES(?, ?, ?)', 
                ('{}'.format(category_value),'{}'.format(key_value),'{}'.format(id_value))) # Добавление в PH_KEYS
    base.commit()
    cur.execute('INSERT INTO ph_respond VALUES(?, ?, ?)',
                ('{}'.format(category_value),'{}'.format(respond_value),'{}'.format(id_value))) # Добавление в PH_RESPOND
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







