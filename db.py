import sqlite3

class Question:
    def __init__(self, id, chap, name):
        self._id = id
        self._chap = chap
        self._name = name

class Answer:
    def __init__(self, id, qn_id, name):
        self._id = id
        self._qn_id = qn_id
        self._name = name

#TODO: Error handling

def populate_questions_table(cursor):
    # Create questions table
    create_table_query = """CREATE TABLE IF NOT EXISTS questions (
                            id INTEGER PRIMARY KEY,
                            chapter INTEGER,
                            name TEXT)"""

    cursor.execute(create_table_query)

    # Populates table with answer list
    question_list = [(1, "What is the value of x = 7 / 2?"),
                    (1, "What is the value of x = 7 // 2?"),
                    (1, "What is the value of x = 7 % 2?"),
                    (1, "a = 1, b = 2. What does a >= b return?"),
                    (1, "a = 2, b = 1. What does a == b return?"),
                    (2, "Chapter 2 Question")]

    cursor.executemany("INSERT INTO questions (chapter, name) VALUES(?, ?)", question_list)

def populate_answers_table(cursor):
    # Create answers table
    create_table_query = """CREATE TABLE IF NOT EXISTS answers (
                            id INTEGER PRIMARY KEY,
                            qn_id INTEGER,
                            name TEXT,
                            FOREIGN KEY (qn_id)
                                REFERENCES questions (id)
                            )"""

    cursor.execute(create_table_query)

    # initialised answer list
    answer_list = [(0, "3.5"),
                  (1, "3"),
                  (2, "1"),
                  (3, "False"),
                  (4, "False"),
                  (5, "Test")]

    cursor.executemany("INSERT INTO answers (qn_id, name) VALUES(?, ?)", answer_list)
   
def db_setup():
    # Define connection and cursor
    connection = sqlite3.connect('main.db')
    cursor = connection.cursor()

    # TODO: Make automatic drop table code without specifiying table names
    cursor.execute("DROP TABLE IF EXISTS answers")
    cursor.execute("DROP TABLE IF EXISTS questions")

    populate_questions_table(cursor)
    populate_answers_table(cursor)

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

def db_get_questions_by_chap_num(chap_num):
    """Gets list of questions of specified chapter number from questions table

    Args:
        chap: chapter number

    Returns:
        A list of questions. Each row is represented as a Question object, and then appended into
        question_list.

    Raises:
        ???
    """

    connection = sqlite3.connect('main.db')
    cursor = connection.cursor()

    #Input parameters need to be of tuple type
    cursor.execute("SELECT * FROM questions WHERE chapter = ?", (chap_num,))

    question_list = []
    results = cursor.fetchall()

    for result in results:
        question = Question(result[0], result[1], result[2])
        question_list.append(question)
    
    cursor.close()
    connection.close()

    return question_list

def db_get_question_answers(qn_id):
    """Gets list of answers of specified question id from answers table

    Args:
        qn_id: question id

    Returns:
        A list of answers. Each row is represented as an Answer object, and then appended into
        answer_list.

    Raises:
        ???
    """

    connection = sqlite3.connect('main.db')
    cursor = connection.cursor()

    #Input parameters need to be of tuple type
    cursor.execute("SELECT * FROM answers WHERE qn_id = ?", (qn_id,))

    answer_list = []
    results = cursor.fetchall()

    for result in results:
        answer = Answer(result[0], result[1], result[2])
        answer_list.append(answer)
    
    cursor.close()
    connection.close()

    return answer_list

question_list = db_get_questions_by_chap_num(1)

for question in question_list:
    answer_list = db_get_question_answers(question._id)
    
    for answer in answer_list:
        print(question._name, answer._name)

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

