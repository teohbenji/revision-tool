from db import *
import os.path
import random

def home_page():
    """Creates home page CLI
    
    Includes options to start program, access settings or exit program"""
    print("""---------------\nHome page
    1 - Start
    2 - Settings
    3 - Exit""")
    print("---------------")

    user_response = input("Please enter 1 to choose a game mode, 2 to go to settings or 3 to exit the game: ")

    #Reprompts user for valid user_response input
    while user_response != "1" and user_response != "Start" and user_response != "start" and \
          user_response != "2" and user_response != "Settings" and user_response != "settings" and \
          user_response != "3" and user_response != "Exit" and user_response != "exit":

        print("\nYou entered an invalid command: {}.".format(user_response))
        print("Please enter a valid command.")
        user_response = input("Please enter 1 to choose a game mode, 2 to go to settings or 3 to exit the game: ")

    #Redirects user based on user_response
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
    print("""---------------\nSettings page
    1 - Add a question
    2 - Remove a question
    3 - Reset program
    # - Back to Home page""")
    print("---------------")

    user_response = input("Please enter 1 to add a question, 2 to remove a question, 3 to reset program or # to go back to Home page: ")

    #Reprompts user for valid user_response input
    while user_response != "1" and user_response != "Add a question" and user_response != "add a question" and \
          user_response != "2" and user_response != "Remove a question" and user_response != "remove a question" and \
          user_response != "3" and user_response != "Reset Program" and user_response != "reset Program" and \
          user_response != "#" and user_response != "Back to Home page" and user_response != "back to Home page":
        print("\nYou entered an invalid command: {}.".format(user_response))
        print("Please enter a valid command.")
        user_response = input("Please enter 1 to add a question, 2 to remove a question, 3 to reset program or # to go back to Home page: ")

    #Redirects user based on user_response
    if user_response == "1" or user_response == "Add a question" or user_response == "add a question":
        print("\nYou have chosen 1 - Add a question.")
        add_new_question_page()
    elif user_response == "2" or user_response == "Remove a question" or user_response == "remove a question":
        print("\nYou have chosen 2 - Remove a question.")
        remove_question_page()
    elif user_response == "3" or user_response == "Reset Program" or user_response == "reset Program":
        print("\nYou have chosen 3 - Reset program.")
        reset_page()         
    elif user_response == "#" or user_response == "Back to Home page" or user_response == "back to Home page":
        print("\nYou have chosen # - Back to Home page.")
        home_page()

def reset_page():
    """Creates reset data CLI
    
    Includes options to confirm reset database or return to settings page"""
    #Warns user before resetting database
    print("WARNING: Are you sure you want to reset the program?")
    print("ALL PROGRESS WILL BE LOST, including new questions created and the highscores in campaign and sudden death mode.\n")

    user_response = input("Please enter 1 to confirm or # to go back to the settings page: ")

    #Reprompts user for valid user_response input
    while user_response != "1" and user_response != "#":
        print("\nYou entered an invalid command: {}.".format(user_response))
        print("Please enter a valid command.")
        user_response = input("Please enter 1 to confirm, # to go back to the settings page: ")

    #Resets database
    if user_response == "1":
        db_setup()
        print("\n---------------------------------------------------")
        print("Reset success! Returning you to the settings page")
        print("---------------------------------------------------\n")

    else:
        print("\nYou have chosen # - Back to Settings page.")

    #Returns user back to settings page
    settings_page()

def mode_page():
    """Creates mode page CLI
    
    Includes options to play campaign, sudden death or return to home page"""
    print("\n---------------")
    print("""Mode Select
    1 - Campaign (Play on to move to the next chapter)
    2 - Sudden death (One wrong answer and you lose...)
    # - Back to Home page""")
    print("---------------")

    user_response = input("Please enter 1 to choose Campaign mode, 2 to choose Sudden death Mode or # to go back to Home page: ")

    #Reprompts user for valid user_response input
    while user_response != "1" and user_response != "Campaign" and user_response != "campaign" and \
          user_response != "2" and user_response != "Sudden death" and user_response != "sudden death" and \
          user_response != "#" and user_response != "Back to Home page" and user_response != "back to Home page":
        print("\nYou entered an invalid command: {}.".format(user_response))
        print("Please enter a valid command.")
        user_response = input("Please enter 1 to choose Campaign mode, 2 to choose Sudden death Mode or # to go back to Home page: ")

    #Redirects user based on user_response
    if user_response == "1" or user_response == "Campaign" or user_response == "campaign":
        print("\nYou have chosen 1 - Campaign to start Campaign mode.")
        chapter_select_page()
    elif user_response == "2" or user_response == "Sudden death" or user_response == "sudden death":
        print("\nYou have chosen 2 - Sudden death")
        sudden_death_page()
    elif user_response == "#" or user_response == "Back to Home page" or user_response == "back to Home page":
        print("\nYou have chosen # - Back to Home page.")
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
    #Redirects user based on user_response
    if user_response in valid_inputs_list:
        chap_num = int(user_response[-1])
        campaign(chap_num)
    elif user_response == "#" or user_response == "Back to Mode page" or user_response == "back to Mode page":
        mode_page()

    #Reprompts user for valid user_response input
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
    if current_score >= 4:
        db_update_chapter_unlocked(chap_num + 1)

        if chap_num < 7:
            print("Congratulations! You have unlocked chapter {}!".format(chap_num + 1))

            user_response = input("Please enter 1 to attempt the next chapter, 2 to try this chapter again or # to go back to home page: ")
            
            #Reprompts user for valid user_response input
            while user_response != "1" and user_response != "2" and user_response != "#":
                print("\nYou entered an invalid command: {}.".format(user_response))
                print("Please enter a valid command.")
                user_response = input("Please enter 1 to attempt the next chapter, 2 to try this chapter again or # to go back to home page: ")

            #Redirects user based on user_response
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

            #Reprompts user for valid user_response input
            while user_response != "1" and user_response != "#":
                print("\nYou entered an invalid command: {}.".format(user_response))
                print("Please enter a valid command.")
                user_response = input("Please enter 1 to try again or # to go back to home page: ")

            #Redirects user based on user_response
            if user_response == "1":
                campaign(chap_num)
            elif user_response == "#":
                print("\nYou have chosen # - Back to Home page.")
                home_page()
    
     # UI for failed attempt. Prompt to try again or return to home page
    else:
        print("\nYou failed to unlock the next chapter. :(")
        user_response = input("Please enter 1 to try again or # to go back to home page: ")

        #Reprompts user for valid user_response input
        while user_response != "1" and user_response != "#":
            print("\nYou entered an invalid command: {}.".format(user_response))
            print("Please enter a valid command.")
            user_response = input("Please enter 1 to try again or # to go back to home page: ")

        #Redirects user based on user_response
        if user_response == "1":
            campaign(chap_num)
        elif user_response == "#":
            print("\nYou have chosen # - Back to Home page.")
            home_page()

def sudden_death_page():
    """Creates scorecard page CLI."""
    user_response = input("Please enter 1 to begin the sudden death game mode, 2 to view the top 5 highscores or # to go back to Home page: ")

    #Reprompts user for valid user_response input
    while user_response != "1" and user_response != "2" and user_response != "#":
        print("\nYou entered an invalid command: {}.".format(user_response))
        print("Please enter a valid command.")
        user_response = input("Please enter 1 to begin the sudden death game mode, 2 to view the top 5 highscores or # to go back to Home page: ")

    #Redirects user based on user_response
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
        #Reprompts user for valid user_response input
        while user_response != "1" and user_response != "#":
            print("\nYou entered an invalid command: {}.".format(user_response))
            print("Please enter a valid command.")
            user_response = input("Please enter 1 to try again or # to go back to home page: ")

        #Redirects user based on user_response
        if user_response == "1":
            print("\nYou have chosen 1 - Sudden death to start Sudden death. One wrong move you loseeeeeeee.")
            grade_sudden_death()
            
        elif user_response == "#":
            print("\nYou have chosen # - Back to Home page.")
            home_page()
 
def grade_sudden_death():
    """Handles logic for sudden death mode.

    User answers every question in questions table. If user gets question wrong, the mode ends.
    """
    correct_qns_num = 0
    questions_list = db_get_all_questions()
    question_num = 0 

    while len(questions_list) > 0:
        question_num += 1

        question = random.choice(questions_list)
        answers_list = db_get_answers_by_question_id(question._id)
        isAnswerCorrect = grade_question_page(question_num, question, answers_list)

        #User gets answer right
        if isAnswerCorrect:
            correct_qns_num += 1
            questions_list.pop(questions_list.index(question))

        #User gets answer wrong    
        else:
            print("You got {} questions correct!".format(correct_qns_num))
            user_name = input("What name would you like to save this score under?")
            score = Score("", user_name, correct_qns_num)
            db_add_score(score)

            user_response = input("Please enter 1 to try again or # to go back to home page: ")
            #Reprompts user for valid user_response input
            while user_response != "1" and user_response != "#":
                print("\nYou entered an invalid command: {}.".format(user_response))
                print("Please enter a valid command.")
                user_response = input("Please enter 1 to try again or # to go back to home page: ")

            #Redirects user based on user_response
            if user_response == "1":
                grade_sudden_death()

            elif user_response == "#":
                print("\nYou have chosen # - Back to Home page.")
                home_page()
    
    complete_sudden_death_page(correct_qns_num)

def complete_sudden_death_page(correct_qns_num):
    """CLI displayed after user gets every sudden death question correct
    
    Args:
        correct_qns_num: Number of questions user answered correctly
    
    """
    print("Congratulations! You have completed the sudden death gamemode! You got all {} questions right!".format(correct_qns_num))
    user_name = input("What name would you like to save this score under?")

    score = Score("", user_name, correct_qns_num)
    db_add_score(score)

    #Reprompts user for valid user_response input
    user_response = input("Please enter 1 to try again or # to go back to home page: ")
    while user_response != "1" and user_response != "#":
        print("\nYou entered an invalid command: {}.".format(user_response))
        print("Please enter a valid command.")
        user_response = input("Please enter 1 to try again or # to go back to home page: ")

    #Redirects user based on user_response
    if user_response == "1":
        grade_sudden_death()
    elif user_response == "#":
        print("\nYou have chosen # - Back to Home page.")
        home_page()

def grade_campaign_questions(chap_num):
    """Checks results of user attempting 5 questions from selected chapter.

    Args:
        chap_num: chapter number

    Returns:
        current_score: User score out of 5
        result_list: List of length 5 containing user results. Either "Correct" or "Wrong"
    """

    current_score = 0
    result_list = []
    questions_list = db_get_questions_by_chap_num(chap_num)
    
    #Choose random 5 questions from all the questions in the chapter
    random_questions_list = random.sample(questions_list, 5)
    question_num = 0

    for question in random_questions_list:
        answers_list = []
        answers_list = db_get_answers_by_question_id(question._id)
        question_num += 1

        isResultTrue = grade_question_page(question_num, question, answers_list)

        if isResultTrue:
            result_list.append("Correct")
            current_score += 1
        else:
            result_list.append("Wrong")
    
    return current_score, result_list

def grade_question_page(question_num, question, answers_list,):
    """Creates question grading CLI

    Prints question, then prints different lines depending on user input. If user answer is wrong, prints out all possible answers

    Args:
        question_no: Question number
        question: Question object
        answers_list: list of Answer objects
        
    Returns:
        True if correct answer, False if wrong answer
    """
    grading = "wrong"
    print("\n\nQuestion {}:\n{}".format(question_num, question._name))
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

def add_new_question_page():
    """Creates add new question CLI"""
    print("Hello, you are about to add a new question. Enter # at anytime to quit back to Settings page")
    chap_num = input("\nWhich chapter from Chapters 1-7 is the new question from: ")

    #Reprompts user for valid chap_num input
    while chap_num not in [str(i) for i in range(1,8)] and chap_num != '#':
        print("\nYou entered an invalid command: {}.".format(chap_num))
        chap_num = input("Please enter a valid Chapter number from 1 - 7: ")

    if chap_num in [str(i) for i in range(1,8)]:
        print("\nYou will add a question under Chapter {}".format(chap_num))
    
    #Returns user to settings page
    elif chap_num == '#':
        print("\nYou have entered # to go back to Settings page.\n")
        settings_page()
    
    qn_type = input("\nIs your question an mcq or open-ended question?\n1 - MCQ\n2 - Open-ended\nEnter 1 or 2: ")

    #Reprompts user for valid qn_type input
    while qn_type != '1' and qn_type != '2' and qn_type != '#':
        print("\nYou entered an invalid command: {}.".format(qn_type))
        qn_type = input("\nIs your question an mcq or open-ended question?\n1 - MCQ\n2 - Open-ended\nEnter 1 or 2: ")

    #Creates mcq question
    if qn_type == '1':
        add_mcq_question_page(chap_num)
    
    #Creates open_ended question
    elif qn_type == '2':
        add_open_ended_question_page(chap_num)

    #Returns user to settings page
    elif qn_type == '#':
        print("\nYou have entered # to go back to Settings page.\n")
        settings_page()

def add_mcq_question_page(chap_num):
    """Creates add mcq question CLI

    Args: 
        chap_num: Chapter number of new question
    
    Returns:
        None
    """
    print("\nYou have chosen to add an MCQ question")
    question_name = input("Input your new question: ")

    if question_name == '#':
        print("\nYou have entered # to go back to Settings page.\n")
        settings_page()

    option_number = [str(i) for i in range(1,100)]
    answer_options = []
    add_another_option = '1'
    question_name += "\n(To answer, enter 1 for Option 1, enter 2 for Option 2 etc.)"

    #Prompts user to add new answer option
    while add_another_option != '2' and add_another_option != '#':
        new_mcq_option = input("\nAdd your MCQ Option: ")

        #Returns user to settings page
        if new_mcq_option =='#':
            print("\nYou have entered # to go back to Settings page.\n")
            settings_page()
        
        current_option = option_number.pop(0)
        #Adds answer options to question name
        answer_options.append(current_option)
        question_name += "\nOption {}".format(current_option) + " - " + new_mcq_option
        print("\nYou have entered:\nChapter number: {}\nQuestion: {}".format(chap_num, question_name))

        add_another_option = input("\nDo you want to add another MCQ Option?\n1 - Yes\n2 - No\nEnter 1 or 2: ")

        #Reprompts user for valid add_another_option input
        while add_another_option != '1' and add_another_option != '2' and add_another_option != '#':
            print("\nYou entered an invalid command: {}.".format(add_another_option))
            add_another_option = input("Do you want to add another MCQ Option?\n1 - Yes\n2 - No\nEnter 1 or 2: ")

    #Returns user to settings page
    if add_another_option =='#':
        print("\nYou have entered # to go back to Settings page.\n")
        settings_page()

    answer_name = input("\nInput your answer to the question (Eg. Enter 1 for Option 1, Enter 2 for Option 2): ")

    #Reprompts user for valid answer_name input
    while answer_name not in answer_options and answer_name != '#':
        print("\nYou entered an invalid option: {}.".format(answer_name))
        answer_name = input("\nInput your answer to the question (Eg. Enter 1 for Option 1, Enter 2 for Option 2): ")
    
    #Returns user to settings page
    if answer_name == '#':
        print("\nYou have entered # to go back to Settings page.\n")
        settings_page()

    confirm_add_question(chap_num, question_name, answer_name)

def add_open_ended_question_page(chap_num):
    """Creates add open ended question CLI

    Args: 
        chap_num: Chapter number of new question
    
    Returns:
        None
    """
    print("\nYou have chosen to add an open-ended question")
    question_name = input("Input your new question: ")

    #Returns user to settings page
    if question_name == '#':
        print("\nYou have entered # to go back to Settings page.\n")
        settings_page()

    print("\nYou have entered:\nChapter number: {}\nQuestion: {}".format(chap_num, question_name))

    answer_name = input("\nInput your answer to the question: ")

    #Returns user to settings page
    if answer_name == '#':
        print("\nYou have entered # to go back to Settings page.\n")
        settings_page()
    
    confirm_add_question(chap_num, question_name, answer_name)

def confirm_add_question(chap_num, question_name, answer_name):
    """Adds question after user confirmation
    
    Args:
        chap_num: Chapter number of new question
        question_name: Name of question to be added
        answer_name: Name of answer to be added

    Returns:
        None
    """
    print("\nYou have entered:\nChapter number: {}\nQuestion: {}\nAnswer: {}".format(chap_num, question_name, answer_name))

    confirmation = input("\nTo confirm the addition of the above question, please enter 1: ")
    
    #Reprompts user for valid confirmation input
    while confirmation != '1' and confirmation != '#':
        print("\nYou entered an invalid command: {}.".format(confirmation))
        confirmation = input("Please enter 1 to confirm your new question and answer or # to quit: ")

    if confirmation == "1":
        question = Question('', int(chap_num), question_name)
        db_add_question(question)

        answer = Answer("", db_get_newest_question_id(), answer_name)
        db_add_answer(answer)

        print("------------------------------------------\nYou have successfully added the question and answer.")
        print("You will be redirected to Settings page.------------------------------------------\n")
        settings_page()

    #Returns user to settings page
    elif confirmation == '#':
        print("\nYou have entered # to go back to Settings page.\n")
        settings_page()

def remove_question_page():
    """Creates remove question CLI """
    print("\nHello, you are about to remove a question. Enter # at anytime to quit back to Settings page")
    print("1 - Remove specific question (Based on unique question id number. If you do not know the unique question id, pick option 2.)\
        \n2 - Show all unique question id, question and answer\
        \n# - Go back to Settings page")

    user_response = input("Please enter 1 to remove a question, 2 to show all questions and answers, or # to return to the Settings page: ")

    #Reprompts user for valid user_response input
    while user_response != "1" and user_response != "2" and user_response != "#":
        print("\nYou entered an invalid command: {}.".format(user_response))
        print("Please enter a valid command.")
        user_response = input("Please enter 1 to remove a question, 2 to show all questions and answers, or # to return to the Settings page: ")

    if user_response == "1":
        print("\nYou have chosen 1 - Remove specific question.")
        remove_question()

    elif user_response == "#":
        print("\nYou have chosen # - Back to Settings page.")
        settings_page()

    elif user_response == "2":
        print("\nYou have chosen 2 - Show all questions and answers.")
        show_all_qns_and_answers_page()

def show_all_qns_and_answers_page():
    """Creates CLI to display all questions and answers"""
    chapter_question_list = db_get_questions_sorted_by_chapter()
    chapter_answer_list = sort_answer_by_chapter(chapter_question_list)

    print("--------------------------------")
    for chapter_list, chapter_list2 in zip(chapter_question_list, chapter_answer_list):

        print("Chapter {} Questions\n".format(chapter_list[0]._chap_num))
        for question, answer in zip(chapter_list, chapter_list2):
            #Prints question with single answer
            if len(answer) == 1:
                print("\nQuestion Unique ID: {} \
                    \nQuestion: {} \
                    \nAnswer: {} ".format (question._id, question._name, answer[0]._name))
            
            #Prints question with multiple answers
            else:
                multiple_answer_string = ""
                for multipleanswer in answer:
                    multiple_answer_string += "{}/".format(multipleanswer._name)
                print("\nQuestion Unique ID: {} \
                    \nQuestion: {} \
                    \nMultiple way to answer: {} ".format (question._id, question._name, multiple_answer_string))

        print("\n--------------------------------")

    user_response = input("Please enter 1 to remove a question or # to return to the Settings page: ")

    #Reprompts user for valid user_response input
    while user_response != "1" and user_response != "#":
        print("\nYou entered an invalid command: {}.".format(user_response))
        print("Please enter a valid command.")
        user_response = input("Please enter 1 to remove a question or # to return to the Settings page: ")

    #Redirects user based on user_response
    if user_response == "1":
        print("\nYou have chosen 1 - Remove specific question.")
        remove_question()
        
    elif user_response == "#":
        print("\nYou have chosen # - Back to Settings page.")
        settings_page()

def sort_answer_by_chapter(chapter_question_list):
    """Sorts answer objects by chapter

    Args:
        chapter_question_list: List of questions sorted by chapter

    Returns:
        chapter_answer_list: List of answers sorted by chapter
    """
    chapter_answer_list = []
    for chapter in chapter_question_list:
        answer_list = []
        for question in chapter:
            answer = db_get_answers_by_question_id(question._id)
            answer_list.append(answer)
            
        chapter_answer_list.append(answer_list)
        
    return chapter_answer_list

def remove_question():
    """Deletes question based on qn id that user inputs"""
    qn_id = input("\nPlease enter the unique ID number of the question you wish to remove: ")
    valid_qn_id_list = db_get_all_question_ids()

    #Reprompts user for valid qn_id input
    while qn_id not in valid_qn_id_list and qn_id != '#':
        print("\nYou entered an invalid command: {}.".format(qn_id))
        print("Please enter a valid command.")

        qn_id = input("Enter # to go back to Settings. If not, please enter a valid unique ID number of the question you wish to remove: ")

    if qn_id == "#":
        print("\nYou have chosen # - Back to Settings page.")
        settings_page()

    elif qn_id in valid_qn_id_list:
        db_remove_question_by_id(int(qn_id))
        db_remove_answer_by_question_id(int(qn_id))

        print("\nYou have successfully deleted the question and answer with unique id: {}".format(qn_id))
        print("You will be directed back to Settings page\n")
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

if __name__ == '__main__':
    main()