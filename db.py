import sqlite3

def db_setup():
    """Setup main.db by deleting and recreating tables"""
    # Define connection and cursor
    connection = sqlite3.connect('main.db')
    cursor = connection.cursor()

    results = get_all_table_names(cursor)
    
    for result in results:
        (table_name, ) = result
        cursor.execute("DROP TABLE IF EXISTS " + table_name)

    # Setup schema 
    setup_questions_table(cursor)
    setup_answers_table(cursor)
    setup_chapters_table(cursor)
    setup_scores_table(cursor)

    connection.commit()
    cursor.close()
    connection.close()

class Question:
    """Stores data in each row from questions table

    Attributes:
        id: Unique identifier
        chap_num: The chapter where the question is from
        name: Question name
    """
    def __init__(self, id, chap_num, name):
        """Inits Question with id, chap_num, name."""
        self._id = id
        self._chap_num = chap_num
        self._name = name
    
    def __eq__(self, other) : 
        return self.__dict__ == other.__dict__

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

    #Compare attribute values of two Answer objects
    def __eq__(self, other) : 
        return self.__dict__ == other.__dict__

class Chapter:
    """Stores data in each row from chapter table

    Attributes:
        id: Unique identifier
        chap_num: The chapter number
        high_score: highest score of the chapter ever attained
        unlocked: boolean variable. True if unlocked, False if still locked.
    """
    def __init__(self, id, chap_num, high_score, unlocked):
        """Inits Answer with id, qn_id, name."""
        self._id = id
        self._chap_num = chap_num
        self._high_score = high_score
        self._unlocked = unlocked

    #Compare attribute values of two Chapter objects
    def __eq__(self, other) : 
        return self.__dict__ == other.__dict__

class Score:
    """Stores data in each row from scores table

    Attributes:
        id: Unique identifier
        name: User's name
        score: Value of score
    """
    def __init__(self, id, name, score):
        """Inits Score with id, name, score."""
        self._id = id
        self._name = name
        self._score = score

    #Compare attribute values of two Answer objects
    def __eq__(self, other) : 
        return self.__dict__ == other.__dict__   

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
                  (6, "Answer 1"),
                  (6, "Answer 2"),
                  (7, "Answer 1"),
                  (7, "Answer 2"),
                  (7, "Answer 3"),
                  (8, "Answer"),
                  (9, "Answer"),
                  (10, "Answer")]

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
                            chap_num INTEGER,
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

    cursor.executemany("INSERT INTO chapters (chap_num, high_score, unlocked) VALUES(?, ?, ?)", chapter_list) 

def setup_scores_table(cursor):
    """Creates empty scores table
    
    Args:
        cursor: cursor object for executing SQLite queries

    Returns:
        None
    """
    create_table_query = """CREATE TABLE IF NOT EXISTS scores (
                            id INTEGER PRIMARY KEY,
                            name TEXT,
                            score INTEGER
                            )"""

    cursor.execute(create_table_query)

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

def db_get_all_chapters(db='main'):
    """Gets list of all chapter data from chapters table

    Args:
        db: Default value is 'main' to access main.db, use 'test' instead for accessing test.db 

    Returns:
        A list of data for each chapter. Each row is represented as a Chapter object, and then appended into
        chapters_list.
    """
    connection = sqlite3.connect('test.db' if db == 'test' else 'main.db')
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

def db_get_unlocked_chap_nums(db='main'):
    """Gets list of unlocked chapter numbers from chapters table

    Args:
        db: Default value is 'main' to access main.db, use 'test' instead for accessing test.db 

    Returns:
        A list of unlocked chapter numbers.
    """
    connection = sqlite3.connect('test.db' if db == 'test' else 'main.db')
    cursor = connection.cursor()

    cursor.execute("SELECT chap_num FROM chapters where unlocked = 1")
    results = cursor.fetchall()

    unlocked_chap_nums_list = []

    for result in results:
        (chap_num, ) = result
        unlocked_chap_nums_list.append(chap_num)
    
    cursor.close()
    connection.close()

    return unlocked_chap_nums_list

def db_get_locked_chap_nums(db='main'):
    """Gets list of locked chapter numbers from chapters table

    Args:
        db: Default value is 'main' to access main.db, use 'test' instead for accessing test.db 

    Returns:
        A list of locked chapter numbers.
    """
    connection = sqlite3.connect('test.db' if db == 'test' else 'main.db')
    cursor = connection.cursor()

    cursor.execute("SELECT chap_num FROM chapters where unlocked = 0")
    results = cursor.fetchall()
    locked_chap_nums_list = []

    for result in results:
        (chap_num, ) = result
        locked_chap_nums_list.append(chap_num)
    
    cursor.close()
    connection.close()

    return locked_chap_nums_list

def db_get_chapter_high_score(chap_num, db='main'):
    """Gets high score of chapter from chapters table

    Args:
        chap_num: Chapter number
        db: Default value is 'main' to access main.db, use 'test' instead for accessing test.db 

    Returns:
        High score of chapter
    """
    connection = sqlite3.connect('test.db' if db == 'test' else 'main.db')
    cursor = connection.cursor()

    cursor.execute("SELECT high_score FROM chapters WHERE chap_num = ?", (chap_num,))

    (high_score,) = cursor.fetchone()

    cursor.close()
    connection.close()

    return high_score

def db_update_chapter_high_score(chap_num, new_high_score, db='main'):
    """Updates high score of chapter in chapters table

    Args:
        chap_num: Chapter number
        new_high_score: New high score that replaces old high score in table
        db: Default value is 'main' to access main.db, use 'test' instead for accessing test.db 

    Returns:
        None
    """
    
    connection = sqlite3.connect('test.db' if db == 'test' else 'main.db')
    cursor = connection.cursor()

    cursor.execute('''UPDATE chapters
                      SET high_score = ?
                      WHERE chap_num = ?''', (new_high_score, chap_num))

    connection.commit()
    cursor.close()
    connection.close()

def db_update_chapter_unlocked(chap_num, db='main'):
    """Updates unlocked status of chapter in chapters table

    Args:
        chap_num: Chapter number
        db: Default value is 'main' to access main.db, use 'test' instead for accessing test.db

    Returns:
        None
    """
    connection = sqlite3.connect('test.db' if db == 'test' else 'main.db')
    cursor = connection.cursor()

    cursor.execute('''UPDATE chapters
                      SET unlocked = ?
                      WHERE chap_num = ?''', (1, chap_num))

    connection.commit()
    cursor.close()
    connection.close()

def db_get_all_questions(db="main"):
    """Gets a list of all questions from questions table

    Args:
        db: Default value is 'main' to access main.db, use 'test' instead for accessing test.db
        
    Returns:
        A list of question objects. Each row is represented as a Question object, and then appended into
        question_list.
    """
    connection = sqlite3.connect('test.db' if db == 'test' else 'main.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM questions")
    results = cursor.fetchall()
    questions_list =[]

    # Save each result in Question object
    for result in results:
        question = Question(result[0], result[1], result[2])
        questions_list.append(question)

    cursor.close()
    connection.close()

    return questions_list

def db_get_questions_by_chap_num(chap_num, db='main'):
    """Gets list of questions of specified chapter number from questions table

    Args:
        chap_num: chapter number
        db: Default value is 'main' to access main.db, use 'test' instead for accessing test.db

    Returns:
        A list of questions. Each row is represented as a Question object, and then appended into
        question_list.
    """

    connection = sqlite3.connect('test.db' if db == 'test' else 'main.db')
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

def db_get_answers_by_question_id(qn_id, db='main'):
    """Gets list of answers of specified question id from answers table

    Args:
        qn_id: question id
        db: Default value is 'main' to access main.db, use 'test' instead for accessing test.db

    Returns:
        A list of answers. Each row is represented as an Answer object, and then appended into
        answer_list.
    """

    connection = sqlite3.connect('test.db' if db == 'test' else 'main.db')
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

def db_add_question(question, db='main'):
    """Adds question into questions table

    question object has empty id value, only _chap_num and _name
    db: Default value is 'main' to access main.db, use 'test' instead for accessing test.db

    Args:
        question: Question object

    Returns:
        None
    """
    connection = sqlite3.connect('test.db' if db == 'test' else 'main.db')
    cursor = connection.cursor()
    
    cursor.execute("INSERT INTO questions (chap_num, name) VALUES(?, ?)", (question._chap_num, question._name))

    connection.commit()
    cursor.close()
    connection.close()

def db_get_newest_question_id(db = 'main'):
    """Gets id of newest question from questions table

    Args:
        db: Default value is 'main' to access main.db, use 'test' instead for accessing test.db

    Returns:
        newest_qn_id: id of newest question
    """
    connection = sqlite3.connect('test.db' if db == 'test' else 'main.db')
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM questions ORDER BY id DESC LIMIT 1")

    result = cursor.fetchall()
    (newest_qn_id,) = result[0]

    return newest_qn_id

def db_add_answer(answer, db = 'main'):
    """Adds answer into answers table

    answer object has empty id value, only _qn_id and _name

    Args:
        answer: Answer object
        db: Default value is 'main' to access main.db, use 'test' instead for accessing test.db

    Returns:
        None
    """
    connection = sqlite3.connect('test.db' if db == 'test' else 'main.db')
    cursor = connection.cursor()

    cursor.execute("INSERT INTO answers (qn_id, name) VALUES(?, ?)", (answer._qn_id, answer._name))

    connection.commit()
    cursor.close()
    connection.close()


def db_get_highscores(db='main'):
    """Gets list of the 5 highest scores in sudden death

    Args:
        db: Default value is 'main' to access main.db, use 'test' instead for accessing test.db

    Returns:
        A list of scores. Each row is represented as a score object, and then appended into
        scores_list.
    """
    connection = sqlite3.connect('test.db' if db == 'test' else 'main.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM scores ORDER BY score DESC LIMIT 5")

    results = cursor.fetchall()
    scores_list = []

    # Save each result in Score object
    for result in results:
        score = Score(result[0], result[1], result[2])
        scores_list.append(score)

    cursor.close()
    connection.close()

    return scores_list

def db_add_score(score, db='main'):
    """Add new score from sudden death mode
    Args:
        score: score object to be added
        db: Default value is 'main' to access main.db, use 'test' instead for accessing test.db

    Returns:
        None
    """
    connection = sqlite3.connect('test.db' if db == 'test' else 'main.db')
    cursor = connection.cursor()

    cursor.execute("INSERT INTO scores (name, score) VALUES(?, ?)", (score._name, score._score))

    connection.commit()
    cursor.close()
    connection.close()

def db_sort_question_by_chapter(db='main'):
    connection = sqlite3.connect('test.db' if db == 'test' else 'main.db')
    cursor = connection.cursor()
    
    cursor.execute("SELECT chap_num FROM questions" )
    chapter_set = set(cursor.fetchall())

    chapter_question_list = []

    for chap_tuple in chapter_set:
        (chap_num, ) = chap_tuple
        cursor.execute("SELECT * FROM questions WHERE chap_num = ?", (chap_num,))

        question_list = []
        #(last_chap, ) = list(chapter_set)[-1]
        results = cursor.fetchall()

        # Save each result in Question object
        for result in results:
            question = Question(result[0], result[1], result[2])
            question_list.append(question)

        chapter_question_list.append(question_list)

    cursor.close()
    connection.close()
    
    return chapter_question_list

def db_get_all_qn_id(db='main'):
    #TODO: write docstring
    connection = sqlite3.connect('test.db' if db == 'test' else 'main.db')
    cursor = connection.cursor()
    
    cursor.execute("SELECT id FROM questions" )
    id_list = cursor.fetchall()
    str_id_list = []
    for id_tuple in id_list:
        (id,) = id_tuple
        str_id_list.append(str(id))

    cursor.close()
    connection.close()
    
    return str_id_list

def db_remove_question_by_id(id, db = 'main'):
    #TODO: write docstring
    connection = sqlite3.connect('test.db' if db == 'test' else 'main.db')
    cursor = connection.cursor()
    
    cursor.execute("DELETE FROM questions where id = ?" , (id,))

    connection.commit()
    cursor.close()
    connection.close()

def db_remove_answer_by_qn_id(qn_id, db = 'main'):
    #TODO: write docstring
    connection = sqlite3.connect('test.db' if db == 'test' else 'main.db')
    cursor = connection.cursor()
    
    cursor.execute("DELETE FROM answers where qn_id = ?" , (qn_id,))

    connection.commit()
    cursor.close()
    connection.close()

