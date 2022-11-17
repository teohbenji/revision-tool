import sqlite3

def db_setup():
    # define connection and cursor
    connection = sqlite3.connect('main.db')
    cursor = connection.cursor()

    # drops questions table
    drop_table_query = """DROP TABLE IF EXISTS questions"""
    cursor.execute(drop_table_query)

    # creates questions table
    create_table_query = """CREATE TABLE IF NOT EXISTS questions (
                            id INTEGER PRIMARY KEY,
                            chapter INTEGER,
                            name TEXT)"""

    cursor.execute(create_table_query)

    # add to questions
    question_list = [(1, "What is the value of x = 5 // 2?"),
                    (1, "What is the value of x = 5 // 2?"),
                    (1, "What is the value of x = 5 % 2?"),
                    (1, "a = 1, b = 2. What does a >= b return?"),
                    (1, "a = 2, b = 1. What does a == b return?"),
                    (2, "Chapter 2 Question")]

    cursor.executemany("INSERT INTO questions (chapter, name) VALUES(?, ?)", question_list)
   
    cursor.execute("SELECT * FROM questions")
    results = cursor.fetchall()
    print(results) #Print out table, ensure values are correct

    connection.commit()
    connection.close()

def db_get_all_questions():
    connection = sqlite3.connect('main.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM questions")
    results = cursor.fetchall()
    print(results)

    connection.commit()
    connection.close()

def db_get_questions_by_chap(chap):
    connection = sqlite3.connect('main.db')
    cursor = connection.cursor()

    #Input parameters need to be of tuple type
    cursor.execute("SELECT id, name FROM questions WHERE chapter = ?", (chap,))

    results = cursor.fetchall()
    
    connection.commit()
    cursor.close()
    connection.close()

    return results


def db_add_question():
    connection = sqlite3.connect('main.db')
    cursor = connection.cursor()

    query = """INSERT INTO questions (id, chapter, name)
                 VALUES 
                 (1, 1, "Failure")"""
    
    cursor.execute(query)

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

