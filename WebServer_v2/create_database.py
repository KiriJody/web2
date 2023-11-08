import sqlite3;
 
con = sqlite3.connect("db.sqlite")
cursor = con.cursor()
 
# создаем таблицу people
cursor.execute("""CREATE TABLE IF NOT EXISTS people
                (id INTEGER PRIMARY KEY AUTOINCREMENT,  
                name TEXT, 
                age INTEGER)
            """)

# данные для добавления
people = [("Tom", 48), ("Bob", 32), ("Sam", 28), ("Alice", 33), ("Kate", 25)]
cursor.executemany("INSERT INTO people (name, age) VALUES (?, ?)", people)
 
con.commit() 

cursor.execute("SELECT * FROM people")
for person in cursor.fetchall():
    print(f"{person[1]} - {person[2]}")