import sqlite3

connection = sqlite3.connect("agents_db.sl3", 5)
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS agents;")
cursor.execute("""
CREATE TABLE agents (
    codename TEXT,
    level INTEGER,
    specialty TEXT
);
""")
connection.commit()
cursor.execute("INSERT INTO agents (codename, level, specialty) VALUES('Shadow Fox', 5, 'Stealth');")
cursor.execute("INSERT INTO agents (codename, level, specialty) VALUES('night cry', 2 ,'nightmares');")
cursor.execute("INSERT INTO agents (codename, level, specialty) VALUES('purple durple kurple nightmare', 8, 'fry');")
cursor.execute("INSERT INTO agents (codename, level, specialty) VALUES('triple nicle', 7, 'Calls your boss');")
cursor.execute("INSERT INTO agents (codename, level, specialty) VALUES('treksx Fox', 6, 'haker');")
connection.commit()

print("=== ALL AGENTS ===")
cursor.execute("SELECT * FROM agents;")
result = cursor.fetchall()
print(result)

print("=== ALL AGENTS ===")
cursor.execute("SELECT rowid, codename, level, specialty FROM agents;")
all_agents = cursor.fetchall()

for agent in all_agents:
    print("ID:", agent[0], end=" ")
    print("| Name:", agent[1], end=" ")
    print("| Level:", agent[2], end=" ")
    print("| Specialty:", agent[3])

cursor.execute("UPDATE agents SET level = 9 WHERE codename = 'Shadow Fox';")
print("===After the update===")
connection.commit()
cursor.execute("SELECT rowid, codename, level, specialty FROM agents;")
all_agents = cursor.fetchall()


for agent in all_agents:
    print("ID:", agent[0], end=" ")
    print("| Name:", agent[1], end=" ")
    print("| Level:", agent[2], end=" ")
    print("| Specialty:", agent[3])
cursor.execute("SELECT rowid, codename, level, specialty FROM agents WHERE level >= 5;")
all_agents = cursor.fetchall()

print("challange5")
print("agents 5 or higher")


for agent in all_agents:
    print("ID:", agent[0], end=" ")
    print("| Name:", agent[1], end=" ")
    print("| Level:", agent[2], end=" ")
    print("| Specialty:", agent[3])

cursor.execute("DELETE FROM agents WHERE level <= 5;")
connection.commit()
cursor.execute("SELECT rowid, codename, level, specialty FROM agents;")
all_agents = cursor.fetchall()

print("challange5")
print("agents 5 or higher")


for agent in all_agents:
    print("ID:", agent[0], end=" ")
    print("| Name:", agent[1], end=" ")
    print("| Level:", agent[2], end=" ")
    print("| Specialty:", agent[3])
connection.close()