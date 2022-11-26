from db import *

def home_page():
    """Creates home page UI. User has options to select game mode, settings or exit program"""
    print("""Home page
    1 - Start
    2 - Settings
    3 - Exit""")
    print("---------------")

    user_response_check = False
    user_response = input("Please enter 1 to choose a game mode, 2 to go to settings or 3 to exit the game: ")

    while not user_response_check:
        if user_response == "1" or user_response == "Start" or user_response == "start":
            user_response_check = True
            print("\nYou have chosen 1 - Start to choose a game mode.")
            mode_page()
        elif user_response == "2" or user_response == "Settings" or user_response == "settings":
            user_response_check = True
            print("\nYou have chosen 2 - Settings.")
            #TODO: Settings page
        elif user_response == "3" or user_response == "Exit" or user_response == "exit":
            user_response_check = True
            print("\nYou have chosen 3 - Exit.")
            print("Thank you for playing! :)")
        else:
            print("\nYou entered an invalid command: {}.".format(user_response))
            print("Please enter a valid command.")
            user_response = input("Please enter 1 to choose a game mode, 2 to go to settings or 3 to exit the game: ")

def settings_page():
    """Creates settings page UI. User has option to add question."""
    print("""Settings page
    1 - Add a question
    2 - ??
    3 - Back to Home page""")
    print("---------------")

    user_response_check = False
    user_response = input("Please enter 1 to add a question, 2 to ?? or 3 to go back to Home page: ")

    while not user_response_check:
        if user_response == "1" or user_response == "Add a question" or user_response == "add a question":
            user_response_check = True
            print("\nYou have chosen 1 - Add a question.")
            #TODO Add a question function
        elif user_response == "2" or user_response == "??" or user_response == "??":
            user_response_check = True
            print("\nYou have chosen 2 - ??.")
            #TODO: ??
        elif user_response == "3" or user_response == "Back to Home page" or user_response == "back to Home page":
            user_response_check = True
            print("\nYou have chosen 3 - Back to Home page.")
            home_page()
        else:
            print("\nYou entered an invalid command: {}.".format(user_response))
            print("Please enter a valid command.")
            user_response = input("Please enter 1 to add a question, 2 to ?? or 3 to go back to Home page: ")

def mode_page():
    """Creates mode page UI. Option to add question."""
    print("---------------\n")
    print("""Mode Select
    1 - Campaign (Play on to move to the next chapter)
    2 - Sudden death (One wrong answer and you lose...)
    3 - Back to Home page""")
    print("---------------")

    user_response_check = False
    user_response = input("Please enter 1 to choose Campaign mode, 2 to choose Sudden death Mode or 3 to go back to Home page: ")

    while not user_response_check:
        if user_response == "1" or user_response == "Campaign" or user_response == "campaign":
            user_response_check = True
            print("\nYou have chosen 1 - Campaign to start Campaign mode.")
            chapter_select_page()
        elif user_response == "2" or user_response == "Sudden death" or user_response == "sudden death":
            user_response_check = True
            print("\nYou have chosen 2 - Sudden death to start Sudden death. One wrong move you loseeeeeeee.")
            #TODO: Sudden death page
        elif user_response == "3" or user_response == "Back to Home page" or user_response == "back to Home page":
            user_response_check = True
            print("\nYou have chosen 3 - Back to Home page.")
            home_page()
        else:
            print("\nYou entered an invalid command: {}.".format(user_response))
            print("Please enter a valid command.")
            user_response = input("Please enter 1 to choose Campaign mode, 2 to choose Sudden death Mode or 3 to go back to Home page: ")

def chapter_select_page():
    """Creates chapter select page UI. Only unlocked chapters are available for user to select. Best score out of previous attempts are shown"""
    print("---------------\n")
    print("Welcome to Campaign mode!")
    chapter_list = db_get_all_chapters()
    
    for chapter in chapter_list:
        print("{} - Chapter {} ({})".format(chapter._chapter_num, chapter._chapter_num, "Unlocked" if chapter._unlocked == 1 else "Locked"))
        
    print("# - Back to Mode page")
    print("---------------")

    #TODO: Only allow user to 
    #get a list of chapter nums from chapter_list, and store in valid_inputs list
    #for each of the chapternums, append "Chapter <chapter_num>" and "chapter <chapter_num>" to valid_inputs list
    #if user_response is in chapter_list, call campaign(user_response)
    #Else if, if #, go back to mode page
    #Else get user_response again
    
    user_response_check = False
    user_response = input("Please enter 1 to choose Chapter 1, 2 to choose Chapter 2, so on and so forth or # to go back to Mode page: ")

    while not user_response_check:
        if user_response == "1" or user_response == "Chapter 1" or user_response == "chapter 1":
            user_response_check = True
            print("\nYou have chosen 1 - Chapter 1.")
            campaign(1)
        elif user_response == "2" or user_response == "Chapter 2" or user_response == "chapter 2":
            user_response_check = True
            print("\nYou have chosen 2 - Chapter 2.")
            campaign(2)
        elif user_response == "3" or user_response == "Chapter 3" or user_response == "chapter 3":
            user_response_check = True
            print("\nYou have chosen 3 - Chapter 3.")
            #TODO: Chapter 3 page
        elif user_response == "#" or user_response == "Back to Mode page" or user_response == "back to Mode page":
            mode_page()
        else:
            print("\nYou entered an invalid command: {}.".format(user_response))
            print("Please enter a valid command.")
            user_response = input("Please enter 1 to choose Chapter 1, 2 to choose Chapter 2, 3 to choose Chapter 3 or # to go back to Mode page: ")

def campaign_scorecard_page(score, result_list):
    """Creates scorecard page UI. 
    
    Result of each question is printed. If score >3 /5, print Success. Else print Try again!"""
    print("\n\n\n----Scorecard----")
    for i in range(5):
        print("Q{} - {}".format(i + 1, result_list[i]))
        
    if score >= 4:
        print("Result: {}/5 Success!".format(score))
    else:
        print("Result: {}/5 Try again!".format(score))

    print("\n\n\n")

def setup():
    db_setup()

#TODO: Pass in user id in future
def campaign(chap_num):
    """Handles logic for campaign chapter, where user has to attempt 5 questions from selected chapter.

    Args:
        chap_num: chapter number

    Returns:
        None
    """
    current_score = 0
    result_list = []
    question_list = db_get_questions_by_chap_num(chap_num)
    answers_list = []

    for question in question_list:
        answers_list.append(db_get_answers_by_question_id(question._id))
        isResultTrue = grade_question(question, answers_list)

        if isResultTrue:
            result_list.append("Correct")
            current_score += 1
        else:
            result_list.append("Wrong")

    # Get high score of chapter from database
    # If user's current score > database high score
    # Update high score
    # Update next chapter score
    # If not dont do anything

    campaign_scorecard_page(current_score, result_list)

def grade_question(question, answers_list):
    """Gets list of questions of specified chapter number from questions table

    Args:
        question: Question object
        answers_list: List of answer object(s) linked to question

    Returns:
        Boolean: True if user answer is in answer list, False if not.s
    """
    print(question._name)
    print("\n")
    user_answer = input("answer: ")

    if user_answer in answers_list:
        print("You got it right!")
        input("Press enter to continue")
        return True
    else:
        print("You got it wrong!")
        print("Correct answer(s): ")

        for answer in answers_list:
            print(answer)
        
        input("Press enter to continue")
        return False

home_page()

