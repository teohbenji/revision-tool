import sqlite3

def test_db_setup():
    connection = sqlite3.connect('test.db')
    cursor = connection.cursor()

    command_1 = """DROP TABLE questions"""
    cursor.execute(command_1)

    command_2 = """CREATE TABLE IF NOT EXISTS questions (
                   id INTEGER PRIMARY KEY,
                   chapter INTEGER,
                   name TEXT)"""

    cursor.execute(command_2)

    command_3 = """INSERT INTO questions (chapter, name)
                 VALUES 
                 (1, "Hello world"),
                 (1, "Royce"),
                 (2, "Benjamin"),
                 (2, "Sean")"""
                
    cursor.execute(command_3)
    cursor.execute("SELECT * FROM questions")

    results = cursor.fetchall()
    print(results)

    connection.commit()
    connection.close()
