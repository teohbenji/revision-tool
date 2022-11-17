from db import *

def setup():
    db_setup()

def main():
    print(db_get_questions_by_chap(1))

main()