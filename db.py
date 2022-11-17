import sqlite3

def db_setup():
    # define connection and cursor
    connection = sqlite3.connect('main.db')
    cursor = connection.cursor()

    # drops questions table
    command_1 = """DROP TABLE questions"""
    cursor.execute(command_1)

    # creates questions table

    command_2 = """CREATE TABLE IF NOT EXISTS questions (
                   id INTEGER PRIMARY KEY,
                   chapter INTEGER,
                   name TEXT)"""

    cursor.execute(command_2)

    # add to questions
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

def db_get_questions_by_chap(chap):
    connection = sqlite3.connect('test.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM questions WHERE chapter = {}".format(chap))

    results = cursor.fetchall()
    
    connection.commit()
    connection.close()

    return results

def db_get_questions_by_chap(chap):
    connection = sqlite3.connect('main.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM questions WHERE chapter = {}".format(chap))

    results = cursor.fetchall()
    
    connection.commit()
    connection.close()

    return results

def db_add_question():
    connection = sqlite3.connect('main.db')
    cursor = connection.cursor()

    command = """INSERT INTO questions (id, chapter, name)
                 VALUES 
                 (1, 1, "Failure")"""
    
    cursor.execute(command)

    connection.commit()
    connection.close()
    
def db_get_all_questions():
    connection = sqlite3.connect('main.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM questions")

    results = cursor.fetchall()
    
    connection.commit()
    connection.close()

    return results

