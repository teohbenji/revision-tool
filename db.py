import sqlite3

class Question:
    """Stores data in each row from questions table

    Attributes:
        id: Unique identifier
        chap_num: The chapter where the question is from
        name: Question name
    """
    def __init__(self, id, chap_num, name):
        """Inits Question with id, chap_num, name."""
        self._id = None if id == None else id
        self._chap_num = chap_num
        self._name = name

class Answer:
    """Stores data in each row from answers table

    Attributes:
        id: Unique identifier
        qn_id: Foreign key. Linked to id in questions table
        name: Answer name
    """
    def __init__(self, id, qn_id, name):
        """Inits Answer with id, qn_id, name."""
        self._id = id
        self._qn_id = qn_id
        self._name = name

class Chapter:
    """Stores data in each row from chapter table

    Attributes:
        id: Unique identifier
        chapter_num: The chapter number
        high_score: highest score of the chapter ever attained
        unlocked: boolean variable. True if unlocked, False if still locked.
    """
    def __init__(self, id, chapter_num, high_score, unlocked):
        """Inits Answer with id, qn_id, name."""
        self._id = id
        self._chapter_num = chapter_num
        self._high_score = high_score
        self._unlocked = unlocked

def setup_questions_table(cursor):
    """Create and populate questions table
    
    Args:
        cursor: cursor object for executing SQLite queries

    Returns:
        None
    """
    create_table_query = """CREATE TABLE IF NOT EXISTS questions (
                            id INTEGER PRIMARY KEY,
                            chap_num INTEGER,
                            name TEXT)"""

    cursor.execute(create_table_query)

    # Populates table with question list
    question_list = [(1, "What is the value of x = 7 / 2?"),
                    (1, "What is the value of x = 7 // 2?"),
                    (1, "What is the value of x = 7 % 2?"),
                    (1, "a = 1, b = 2. What does a >= b return?"),
                    (1, "a = 2, b = 1. What does a == b return?"),
                    (2, "Chapter 2 Question 1"),
                    (2, "Chapter 2 Question 2"),
                    (2, "Chapter 2 Question 3"),
                    (2, "Chapter 2 Question 4"),
                    (2, "Chapter 2 Question 5")]

    cursor.executemany("INSERT INTO questions (chap_num, name) VALUES(?, ?)", question_list)

def setup_answers_table(cursor):
    """Create and populate answers table
    
    Args:
        cursor: cursor object for executing SQLite queries

    Returns:
        None
    """
    create_table_query = """CREATE TABLE IF NOT EXISTS answers (
                            id INTEGER PRIMARY KEY,
                            qn_id INTEGER,
                            name TEXT,
                            FOREIGN KEY (qn_id)
                                REFERENCES questions (id)
                            )"""

    cursor.execute(create_table_query)

    # Populates table with answer list
    answer_list = [(1, "3.5"),
                  (2, "3"),
                  (3, "1"),
                  (4, "False"),
                  (5, "False"),
                  (6, "Chapter 2 Question 1 Answer 1"),
                  (6, "Chapter 2 Question 1 Answer 2"),
                  (7, "Chapter 2 Question 2 Answer 1"),
                  (7, "Chapter 2 Question 2 Answer 2"),
                  (7, "Chapter 2 Question 2 Answer 3"),
                  (8, "Chapter 2 Question 3 Answer"),
                  (9, "Chapter 2 Question 4 Answer"),
                  (10, "Chapter 2 Question 5 Answer")]

    cursor.executemany("INSERT INTO answers (qn_id, name) VALUES(?, ?)", answer_list)

def setup_chapters_table(cursor):
    """Create and populate chapters table
    
    Args:
        cursor: cursor object for executing SQLite queries

    Returns:
        None
    """
    create_table_query = """CREATE TABLE IF NOT EXISTS chapters (
                            id INTEGER PRIMARY KEY,
                            chapter_num INTEGER,
                            high_score INTEGER,
                            unlocked BOOLEAN
                            )"""

    cursor.execute(create_table_query)

    # Populates table with chapter list
    chapter_list = [(1, 0, True),
                  (2, 0, False),
                  (3, 0, False),
                  (4, 0, False),
                  (5, 0, False),
                  (6, 0, False),
                  (7, 0, False)]

    cursor.executemany("INSERT INTO chapters (chapter_num, high_score, unlocked) VALUES(?, ?, ?)", chapter_list)  

def get_all_table_names(cursor):
    """Gets all table names in schema

    Args:
        cursor: cursor object for executing SQLite queries
        
    Returns:
        A list of single variable tuples containing table names in schema.
        E.g. [(customers,), (orders,)]
    """
    cursor.execute("""SELECT name FROM sqlite_schema WHERE type ='table'""")
    results = cursor.fetchall()

    return results

def db_setup():
    """Setup database by deleting and recreating tables"""
    # Define connection and cursor
    connection = sqlite3.connect('main.db')
    cursor = connection.cursor()

    # # TODO: Delete all tables in schema
    results = get_all_table_names(cursor)
    
    for result in results:
        (table_name, ) = result
        cursor.execute("DROP TABLE IF EXISTS " + table_name)

    # Setup schema 
    setup_questions_table(cursor)
    setup_answers_table(cursor)
    setup_chapters_table(cursor)

    connection.commit()
    cursor.close()
    connection.close()

#TODO: In future, get_chapters_from_user_id
def db_get_all_chapters():
    """Gets list of all chapter data from chapters table

    Args:
        None

    Returns:
        A list of data for each chapter. Each row is represented as a Chapter object, and then appended into
        chapters_list.
    """
    connection = sqlite3.connect('main.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM chapters")
    results = cursor.fetchall()
    chapters_list = []
    
    # Save each result in Chapter object
    for result in results:
        chapter = Chapter(result[0], result[1], result[2], result[3])
        chapters_list.append(chapter)
    
    cursor.close()
    connection.close()

    return chapters_list

def get_chapter_high_score(chap_num):

    connection = sqlite3.connect('main.db')
    cursor = connection.cursor()

    cursor.execute("SELECT high_score FROM chapters WHERE chapter_num = ?", (chap_num,))

    chapter_high_score = cursor.fetchall()
    
    cursor.close()
    connection.close()

    return chapter_high_score

def update_chapter_high_score(chap_num, new_high_score):
    pass

def db_get_questions_by_chap_num(chap_num):
    """Gets list of questions of specified chapter number from questions table

    Args:
        chap_num: chapter number

    Returns:
        A list of questions. Each row is represented as a Question object, and then appended into
        question_list.
    """

    connection = sqlite3.connect('main.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM questions WHERE chap_num = ?", (chap_num,))

    question_list = []
    results = cursor.fetchall()

    # Save each result in Question object
    for result in results:
        question = Question(result[0], result[1], result[2])
        question_list.append(question)
    
    cursor.close()
    connection.close()

    return question_list

def db_get_answers_by_question_id(qn_id):
    """Gets list of answers of specified question id from answers table

    Args:
        qn_id: question id

    Returns:
        A list of answers. Each row is represented as an Answer object, and then appended into
        answer_list.
    """

    connection = sqlite3.connect('main.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM answers WHERE qn_id = ?", (qn_id,))

    answer_list = []
    results = cursor.fetchall()

    # Save each result in Answer object
    for result in results:
        answer = Answer(result[0], result[1], result[2])
        answer_list.append(answer)
    
    cursor.close()
    connection.close()

    return answer_list


def db_get_all_questions():
    """Gets a list of all questions from questions table

    Args:
        None
        
    Returns:
        A list of question objects. Each row is represented as a Question object, and then appended into
        question_list.
    """
    connection = sqlite3.connect('main.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM questions")
    results = cursor.fetchall()
    question_list =[]
    
    # Save each result in Question object
    for result in results:
        question = Question(result[0], result[1], result[2])
        question_list.append(question)
    
    cursor.close()
    connection.close()

    return question_list
    
    cursor.execute(query)

    connection.commit()
    connection.close()

