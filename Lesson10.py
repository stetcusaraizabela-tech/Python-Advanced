import sqlite3
connection = sqlite3.connect("agent_db.sl3", 5)

cursor = connection.cursor()
print(connection)
print(cursor)
connection.close()