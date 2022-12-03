from db import *
import os.path
import random

def home_page():
    """Creates home page CLI
    
    Includes options to start program, access settings or exit program"""
    print("""---------------  
Home page
    1 - Start
    2 - Settings
    3 - Exit""")
    print("---------------")

    user_response = input("Please enter 1 to choose a game mode, 2 to go to settings or 3 to exit the game: ")

    while user_response != "1" and user_response != "Start" and user_response != "start" and \
          user_response != "2" and user_response != "Settings" and user_response != "settings" and \
          user_response != "3" and user_response != "Exit" and user_response != "exit":

        print("\nYou entered an invalid command: {}.".format(user_response))
        print("Please enter a valid command.")
        user_response = input("Please enter 1 to choose a game mode, 2 to go to settings or 3 to exit the game: ")

    if user_response == "1" or user_response == "Start" or user_response == "start":
        print("\nYou have chosen 1 - Start to choose a game mode.")
        mode_page()
    elif user_response == "2" or user_response == "Settings" or user_response == "settings":
        print("\nYou have chosen 2 - Settings.")
        settings_page()
    elif user_response == "3" or user_response == "Exit" or user_response == "exit":
        print("\nYou have chosen 3 - Exit.")
        print("Thank you for playing! :)")
        quit()

def settings_page():
    """Creates settings page CLI
    
    Includes options to add question or return to home page"""
    print("""Settings page
    1 - Add a question
    2 - Reset program
    3 - Back to Home page""")
    print("---------------")

    user_response = input("Please enter 1 to add a question, 2 to reset program or 3 to go back to Home page: ")

    while user_response != "1" and user_response != "Add a question" and user_response != "add a question" and \
          user_response != "2" and user_response != "Reset Program" and user_response != "reset Program" and \
          user_response != "3" and user_response != "Back to Home page" and user_response != "back to Home page":
        print("\nYou entered an invalid command: {}.".format(user_response))
        print("Please enter a valid command.")
        user_response = input("Please enter 1 to add a question, 2 to reset program or 3 to go back to Home page: ")

    if user_response == "1" or user_response == "Add a question" or user_response == "add a question":
        print("\nYou have chosen 1 - Add a question.")
        add_new_question()
    elif user_response == "2" or user_response == "Reset Program" or user_response == "reset program":
        print("\nYou have chosen 2 - Reset program.")
        reset_page()            
    elif user_response == "3" or user_response == "Back to Home page" or user_response == "back to Home page":
        print("\nYou have chosen 3 - Back to Home page.")
        home_page()

def mode_page():
    """Creates mode page CLI
    
    Includes options to play campaign, sudden death or return to home page"""
    print("---------------\n")
    print("""Mode Select
    1 - Campaign (Play on to move to the next chapter)
    2 - Sudden death (One wrong answer and you lose...)
    3 - Back to Home page""")
    print("---------------")

    user_response = input("Please enter 1 to choose Campaign mode, 2 to choose Sudden death Mode or 3 to go back to Home page: ")

    while user_response != "1" and user_response != "Campaign" and user_response != "campaign" and \
          user_response != "2" and user_response != "Sudden death" and user_response != "sudden death" and \
          user_response != "3" and user_response != "Back to Home page" and user_response != "back to Home page":
        print("\nYou entered an invalid command: {}.".format(user_response))
        print("Please enter a valid command.")
        user_response = input("Please enter 1 to choose Campaign mode, 2 to choose Sudden death Mode or 3 to go back to Home page: ")

    if user_response == "1" or user_response == "Campaign" or user_response == "campaign":
        print("\nYou have chosen 1 - Campaign to start Campaign mode.")
        chapter_select_page()
    elif user_response == "2" or user_response == "Sudden death" or user_response == "sudden death":
        print("\nYou have chosen 2 - Sudden death")
        sudden_death_page()
    elif user_response == "3" or user_response == "Back to Home page" or user_response == "back to Home page":
        print("\nYou have chosen 3 - Back to Home page.")
        home_page()

def chapter_select_page():
    """Creates chapter select page CLI
    
    Only unlocked chapters are available for user to select. Best score out of previous attempts are shown"""
    print("---------------\n")
    print("Welcome to Campaign mode!")

    unlocked_chap_nums_list = db_get_unlocked_chap_nums()
    locked_chap_nums_list = db_get_locked_chap_nums()
    #Valid inputs refer to inputs with correct chapter numbers, and invalid inputs refers to inputs with wrong chapter numbers
    correct_inputs_list = []
    wrong_inputs_list = []

    for chap_num in unlocked_chap_nums_list:
        correct_inputs_list += [str(chap_num), "Chapter {}".format(str(chap_num)), "chapter {}".format(str(chap_num))]
        print("{} - Chapter {} ({}) * Highest score: {} / 5 *".format(chap_num, chap_num, "Unlocked", db_get_chapter_high_score(chap_num)))

    for chap_num in locked_chap_nums_list:
        wrong_inputs_list += [str(chap_num), "Chapter {}".format(str(chap_num)), "chapter {}".format(str(chap_num))]
        print("{} - Chapter {} ({})".format(chap_num, chap_num, "Locked" ))
    
    print("# - Back to Mode page")
    print("---------------")

    chapter_select_page_input_validation(correct_inputs_list, wrong_inputs_list)

def chapter_select_page_input_validation(valid_inputs_list, invalid_inputs_list):
    """Validates user input when selecting chapter
    
        If user selects unlocked chapter, user is redirected to campaign.
        If user selects mode, user is redirected to mode page
        Depending on whether user selects locked chapter or types wrong input, different messages are output 
        and user has to select chapter again
    """
    user_response = input("Please enter 1 to choose Chapter 1, 2 to choose Chapter 2, so on and so forth or # to go back to Mode page: ")
    
    if user_response in valid_inputs_list:
        chap_num = int(user_response[-1])
        campaign(chap_num)
    elif user_response == "#" or user_response == "Back to Mode page" or user_response == "back to Mode page":
        mode_page()
    elif user_response in invalid_inputs_list:
        chap_num = int(user_response[-1])
        print("\nChapter {} is locked.".format(chap_num))
        print("Please choose an unlocked chapter instead.")
        chapter_select_page_input_validation(valid_inputs_list, invalid_inputs_list)
    else:
        print("\nYou entered an invalid command: {}.".format(user_response))
        print("Please enter a valid command.")
        chapter_select_page_input_validation(valid_inputs_list, invalid_inputs_list)

def campaign_scorecard_page(score, result_list):
    """Creates scorecard page CLI. 
    
    Result of each question is printed. If score >3 /5, prints Success. Else prints Try again!"""
    print("\n\n\n----Scorecard----")
    for i in range(5):
        print("Q{} - {}".format(i + 1, result_list[i]))
        
    if score >= 4:
        print("Result: {}/5 Success!".format(score))
    else:
        print("Result: {}/5 Try again!".format(score))

    print("\n\n\n")

#TODO: Pass in user id in future
def campaign(chap_num):
    """Handles logic for campaign chapter, where user has to attempt 5 questions from selected chapter.

    Args:
        chap_num: chapter number

    Returns:
        None
    """
    (current_score, result_list) = grade_campaign_questions(chap_num)

    # Get high score of chapter from database
    # If user's current score > database high score
    # Update high score
    # Update next chapter score
    # If not dont do anything

    campaign_scorecard_page(current_score, result_list)

    chap_high_score = db_get_chapter_high_score(chap_num)
    
    #Update high score if user beats highscore
    if current_score > chap_high_score:
        db_update_chapter_high_score(chap_num, current_score)
        print("Congratulations, you just got a new highscore of {}/5!".format(current_score))
    
    # UI for new chapter being unlocked
    # TODO: put this in a new function
    if current_score >= 4:
        #NOT BEING UNLOCKED
        db_update_chapter_unlocked(chap_num + 1)
        if chap_num < 7:
            print("Congratulations! You have unlocked chapter {}!".format(chap_num + 1))

            user_response = input("Please enter 1 to attempt the next chapter, 2 to try this chapter again or # to go back to home page: ")
            
            while user_response != "1" and user_response != "2" and user_response != "#":
                print("\nYou entered an invalid command: {}.".format(user_response))
                print("Please enter a valid command.")
                user_response = input("Please enter 1 to attempt the next chapter, 2 to try this chapter again or # to go back to home page: ")

            if user_response == "1":
                campaign(chap_num + 1)
            elif user_response == "2":
                campaign(chap_num)
            elif user_response == "#":
                print("\nYou have chosen # - Back to Home page.")
                home_page()

        else:
            print("Congratulations! You have completed campaign mode!")

            user_response = input("Please enter 1 to try this chapter again or # to go back to home page: ")
            while user_response != "1" and user_response != "#":
                print("\nYou entered an invalid command: {}.".format(user_response))
                print("Please enter a valid command.")
                user_response = input("Please enter 1 to try again or # to go back to home page: ")

            if user_response == "1":
                campaign(chap_num)
            elif user_response == "#":
                print("\nYou have chosen # - Back to Home page.")
                home_page()
    
     # UI for failed attempt. Prompt to try again or return to home page
    else:
        print("\nYou failed to unlock the next chapter. :(")
        user_response = input("Please enter 1 to try again or # to go back to home page: ")

        while user_response != "1" and user_response != "#":
            print("\nYou entered an invalid command: {}.".format(user_response))
            print("Please enter a valid command.")
            user_response = input("Please enter 1 to try again or # to go back to home page: ")

        if user_response == "1":
            campaign(chap_num)
        elif user_response == "#":
            print("\nYou have chosen # - Back to Home page.")
            home_page()

def sudden_death_page():
    user_response = input("Please enter 1 to begin the sudden death game mode, 2 to view the top 5 highscores or # to go back to Home page: ")

    while user_response != "1" and user_response != "2" and user_response != "#":
        print("\nYou entered an invalid command: {}.".format(user_response))
        print("Please enter a valid command.")
        user_response = input("Please enter 1 to begin the sudden death game mode, 2 to view the top 5 highscores or # to go back to Home page: ")

    if user_response == "1":
        print("\nYou have chosen 1 - Sudden death to start Sudden death. One wrong move you loseeeeeeee.")
        grade_sudden_death()

    elif user_response == "#":
        print("\nYou have chosen # - Back to Home page.")
        home_page()

    elif user_response == "2":
        print("\nYou have chosen 2 - These are your champions:")
        highscores = db_get_highscores()
        place = 1

        for score in highscores:
            print("{}) {} - {}".format(place, score._name, score._score))
            place += 1
            
        print("\n")

        user_response = input("Please enter 1 to attempt the sudden death game mode or # to go back to home page: ")

        while user_response != "1" and user_response != "#":
            print("\nYou entered an invalid command: {}.".format(user_response))
            print("Please enter a valid command.")
            user_response = input("Please enter 1 to try again or # to go back to home page: ")

        if user_response == "1":
            print("\nYou have chosen 1 - Sudden death to start Sudden death. One wrong move you loseeeeeeee.")
            grade_sudden_death()
            
        elif user_response == "#":
            print("\nYou have chosen # - Back to Home page.")
            home_page()
 
    # grade_sudden_death()

def grade_sudden_death():
    """Handles logic for sudden death mode.

    User answers every question in questions table. If user gets question wrong, the mode ends.

    Args:
        None

    Returns:
        None
    """
    questions_correct = 0
    questions_list = db_get_all_questions()

    while len(questions_list) > 0:
        question = random.choice(questions_list)
        answers_list = db_get_answers_by_question_id(question._id)
        isResultCorrect = grade_question_page(question, answers_list)

        if isResultCorrect:
            questions_correct += 1
            questions_list.pop(questions_list.index(question))
        else:
            print("You got {} questions correct!".format(questions_correct))
            user_name = input("What name would you like to save this score under?")
            score = Score("", user_name, questions_correct)
            db_add_score(score)

            user_response = input("Please enter 1 to try again or # to go back to home page: ")

            while user_response != "1" and user_response != "#":
                print("\nYou entered an invalid command: {}.".format(user_response))
                print("Please enter a valid command.")
                user_response = input("Please enter 1 to try again or # to go back to home page: ")

            if user_response == "1":
                grade_sudden_death()
            elif user_response == "#":
                print("\nYou have chosen # - Back to Home page.")
                home_page()


    print("Congratulations! You have completed the sudden death gamemode! You got all {} questions right!".format(questions_correct))
    user_name = input("What name would you like to save this score under?")
    score = Score("", user_name, questions_correct)
    db_add_score(score)

    user_response = input("Please enter 1 to try again or # to go back to home page: ")
    while user_response != "1" and user_response != "#":
        print("\nYou entered an invalid command: {}.".format(user_response))
        print("Please enter a valid command.")
        user_response = input("Please enter 1 to try again or # to go back to home page: ")

    if user_response == "1":
        grade_sudden_death()
    elif user_response == "#":
        print("\nYou have chosen # - Back to Home page.")
        home_page()

def grade_campaign_questions(chap_num):
    """Cheks results of user attempting 5 questions from selected chapter.

    Args:
        chap_num: chapter number

    Returns:
        current_score: User score out of 5
        result_list: List of length 5 containing user results. Either "Correct" or "Wrong"
    """

    current_score = 0
    result_list = []
    questions_list = db_get_questions_by_chap_num(chap_num)
    
    #Choose 5 questions out of all the questions in the chapter
    random_questions_list = random.sample(questions_list, 5)

    for question in random_questions_list:
        answers_list = []
        answers_list = db_get_answers_by_question_id(question._id)
        isResultTrue = grade_question_page(question, answers_list)

        if isResultTrue:
            result_list.append("Correct")
            current_score += 1
        else:
            result_list.append("Wrong")
    
    return current_score, result_list

def grade_question_page(question, answers_list):
    """Creates question grading CLI

    Prints different lines depending on user answer. If user answer is wrong,
    prints out all possible answers

    Args:
        question: Question object
        answers_list: list of Answer objects
        
    Returns:
        Boolean depending on user's answer
    """
    grading = "wrong"
    print("\n\nQuestion: {}".format(question._name))
    print("\n")
    user_answer = input("Your answer: ")
    
    for answer in answers_list:
        if user_answer == answer._name:
            grading = "right"
            print("You got it {}!".format(grading))
            input("Press enter to continue")

            return True

    print("You got it {}!".format(grading))
    print("Correct answer(s): ")

    #Prints out all correct answers
    for answer in answers_list:
        print(answer._name)
    input("Press enter to continue")

    return False

def reset_page():
    """Creates reset data CLI

    Warns user before resetting database.

    Args:
        None
        
    Returns:
        None
    """
    print("""WARNING: Are you sure you want to reset the program?\n
ALL progress will be LOST, including new questions created,\n
and the highscores in campaign and sudden death mode.
          """)

    user_response = input("Please enter 1 to confirm, 2 to go back to the settings page, or # to return to the home page: ")

    while user_response != "1" and user_response != "2" and user_response != "#":
        print("\nYou entered an invalid command: {}.".format(user_response))
        print("Please enter a valid command.")
        user_response = input("Please enter 1 to confirm, 2 to go back to the settings page, or # to return to the home page: ")

    if user_response == "1":
        db_setup()
        print("""--------------------
Reset success! Returning you to homepage
--------------------
                """)
        home_page()
        #break(This was here when using user_response_check) After changing while loop no need break right?
    elif user_response == "2":
        print("\nYou have chosen 2 - Back to Settings page.")
        settings_page()
        #break(This was here when using user_response_check) After changing while loop no need break right?
    elif user_response == "#":
        print("\nYou have chosen # - Back to Home page.")
        home_page()
        #break(This was here when using user_response_check) After changing while loop no need break right?

def add_new_question():
    print("Hello, you are about to add a new question. Enter # at anytime to quit back to Settings page")

    chap_num = input("\nWhich chapter from Chapter 1-7 is the new question from:  ")

    while chap_num not in [str(i) for i in range(1,8)] and chap_num != '#':
        print("\nYou entered an invalid command: {}.".format(chap_num))
        chap_num = input("Please enter a valid Chapter number from 1 - 7: ")

    if chap_num in [str(i) for i in range(1,8)]:
        print("\nYou will add a question under Chapter {}".format(chap_num))
    elif chap_num == '#':
        print("\nYou have entered # to go back to Settings page.\n")
        settings_page()
    
    mcq_or_not = input("\nIs your question an mcq or open-ended question?\n1 - MCQ\n2 - Open-ended\nEnter 1 or 2: ")
    while mcq_or_not != '1' and mcq_or_not != '2' and mcq_or_not != '#':
        print("\nYou entered an invalid command: {}.".format(mcq_or_not))
        mcq_or_not = input("\nIs your question an mcq or open-ended question?\n1 - MCQ\n2 - Open-ended\nEnter 1 or 2: ")

    if mcq_or_not == '1':
        is_mcq_question = True
        print("\nYou will add an MCQ question")
    elif mcq_or_not == '2':
        is_mcq_question = False
        print("\nYou will add an open-ended question")
    elif mcq_or_not == '#':
        print("\nYou have entered # to go back to Settings page.\n")
        settings_page()

    if is_mcq_question:
        new_question = input("Input your new question: ")

        if new_question == '#':
            print("\nYou have entered # to go back to Settings page.\n")
            settings_page()

        option_number = [str(i) for i in range(1,100)]
        answer_options = []
        more_options = '1'
        new_question += " (To answer, enter 1 for Option 1, enter 2 for Option 2 etc.)"

        while more_options != '2' and more_options != '#':
            new_mcq_option = input("\nAdd your MCQ Option: ")
            if new_mcq_option =='#':
                print("\nYou have entered # to go back to Settings page.\n")
                settings_page()
            current_option = option_number.pop(0)

            answer_options.append(current_option)
            new_question += "\nOption {}".format(current_option) + " - " + new_mcq_option
            print("\nYou have entered:\nChapter number: {}\nQuestion: {}".format(chap_num, new_question))
            more_options = input("\nDo you want to add more MCQ Options?\n1 - Yes\n2 - No\nEnter 1 or 2: ")

            while more_options != '1' and more_options != '2' and more_options != '#':
                print("\nYou entered an invalid command: {}.".format(more_options))
                more_options = input("Do you want to add more MCQ Options?\n1 - Yes\n2 - No\nEnter 1 or 2: ")

        if more_options =='#':
            print("\nYou have entered # to go back to Settings page.\n")
            settings_page()

        new_answer = input("\nInput your answer to the question (Eg. Enter 1 for Option 1, Enter 2 for Option 2): ")

        while new_answer not in answer_options and new_answer != '#':
            print("\nYou entered an invalid option: {}.".format(new_answer))
            new_answer = input("\nInput your answer to the question (Eg. Enter 1 for Option 1, Enter 2 for Option 2): ")
            
        if new_answer == '#':
            print("\nYou have entered # to go back to Settings page.\n")
            settings_page()

    else:
        new_question = input("Input your new question: ")

        if new_question == '#':
            print("\nYou have entered # to go back to Settings page.\n")
            settings_page()

        print("\nYou have entered:\nChapter number: {}\nQuestion: {}".format(chap_num, new_question))

        new_answer = input("\nInput your answer to the question: ")

        if new_answer == '#':
            print("\nYou have entered # to go back to Settings page.\n")
            settings_page()

    print("\nYou have entered:\nChapter number: {}\nQuestion: {}\nAnswer: {}".format(chap_num, new_question, new_answer))

    confirmation = input("\nTo confirm the addition of the above question, please enter 1: ")
    
    while confirmation != '1' and confirmation != '#':
        print("\nYou entered an invalid command: {}.".format(confirmation))
        confirmation = input("Please enter 1 to confirm your new question and answer or # to quit: ")

    if confirmation == "1":
        question = Question('', int(chap_num), new_question)
        db_add_question(question)

        answer = Answer("", db_get_newest_question_id(), new_answer)
        db_add_answer(answer)

        print("\nYou have successfully added the question and answer.")
        print("You will be directed back to Settings page.\n")
        settings_page()

    elif confirmation == '#':
        print("\nYou have entered # to go back to Settings page.\n")
        settings_page()

def initial_setup():
    """Setups if main.db doesn't exist"""
    db_exists = os.path.exists('main.db')

    if not db_exists:
        db_setup()

def main():
    """Main logic of program"""
    initial_setup()
    home_page()

main()
