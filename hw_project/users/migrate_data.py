import psycopg2
from pymongo import MongoClient
from pymongo.server_api import ServerApi

# Підключення до MongoDB
uri = "mongodb+srv://Valerii:Peremoga2024@cluster1.3egn3sy.mongodb.net/?retryWrites=true&w=majority"
mongo_client = MongoClient(uri, server_api=ServerApi('1'))
mongo_db = mongo_client['hw']
author_collection = mongo_db['author']
quote_collection = mongo_db['quotes']

# Підключення до PostgreSQL
conn = psycopg2.connect(
    dbname='hw_project',
    user='postgres',
    password='Peremoga2024',
    host='localhost'
)
cur = conn.cursor()

# Отримання даних з колекції 'author' та вставка їх у таблицю 'authors' у PostgreSQL
for author_document in author_collection.find():
    print(author_document)
    cur.execute(
        "INSERT INTO authors (fullname, born_date, born_location, description) VALUES (%s, %s, %s, %s)",
        (author_document.get('fullname', ''), author_document.get('born_date', ''), author_document.get('born_location', ''), author_document.get('description', ''))
    )

# Отримання даних з колекції 'quotes' та вставка їх у таблицю 'quotes' у PostgreSQL
for quote_document in quote_collection.find():
    author_fullname = quote_document.get('author', '')
    cur.execute(
        "SELECT id FROM authors WHERE fullname = %s",
        (author_fullname,)
    )
    author_id = cur.fetchone()[0] if cur.rowcount > 0 else None
    if author_id:
        cur.execute(
            "INSERT INTO quotes (quote, author_id) VALUES (%s, %s)",
            (quote_document.get('quote', ''), author_id)
        )
        print( quote_document.get('quote', '') )

# Збереження змін у PostgreSQL та закриття підключення
conn.commit()
cur.close()
conn.close()
