from db import *

def home_page():
    """Creates home page CLI
    
    Includes options to start program, access settings or exit program"""
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
            settings_page()
        elif user_response == "3" or user_response == "Exit" or user_response == "exit":
            user_response_check = True
            print("\nYou have chosen 3 - Exit.")
            print("Thank you for playing! :)")
            quit()
        else:
            print("\nYou entered an invalid command: {}.".format(user_response))
            print("Please enter a valid command.")
            user_response = input("Please enter 1 to choose a game mode, 2 to go to settings or 3 to exit the game: ")

def settings_page():
    """Creates settings page CLI
    
    Includes options to add question or return to home page"""
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
            #TODO: Redirect to select user page?
        elif user_response == "3" or user_response == "Back to Home page" or user_response == "back to Home page":
            user_response_check = True
            print("\nYou have chosen 3 - Back to Home page.")
            home_page()
        else:
            print("\nYou entered an invalid command: {}.".format(user_response))
            print("Please enter a valid command.")
            user_response = input("Please enter 1 to add a question, 2 to ?? or 3 to go back to Home page: ")

def mode_page():
    """Creates mode page CLI
    
    Includes options to play campaign, sudden death or return to home page"""
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
        print("{} - Chapter {} ({})".format(chap_num, chap_num, "Unlocked" ))

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
            user_response_check = False
            user_response = input("Please enter 1 to attempt the next chapter, 2 to try this chapter again or # to go back to home page: ")
            while user_response_check == False:
                if user_response == "1":
                    user_response_check = True
                    campaign(chap_num + 1)
                elif user_response == "2":
                    user_response = True
                    campaign(chap_num)
                elif user_response == "#":
                    user_response_check = True
                    home_page()
                else:
                    print("\nYou entered an invalid command: {}.".format(user_response))
                    print("Please enter a valid command.")
                    user_response = input("Please enter 1 to try again or # to go back to home page: ")
        else:
            print("Congratulations! You have completed campaign mode!")
            user_response_check = False
            user_response = input("Please enter 1 to try this chapter again or # to go back to home page: ")
            while user_response_check == False:
                if user_response == "1":
                    user_response_check = True
                    campaign(chap_num)
                elif user_response == "#":
                    user_response_check = True
                    home_page()
                else:
                    print("\nYou entered an invalid command: {}.".format(user_response))
                    print("Please enter a valid command.")
                    user_response = input("Please enter 1 to try again or # to go back to home page: ")
    
     # UI for failed attempt. Prompt to try again or return to home page
    else:
        user_response_check = False
        user_response = input("Please enter 1 to try again or # to go back to home page: ")
        while user_response_check == False:
            if user_response == "1":
                user_response_check = True
                campaign(chap_num)
            elif user_response == "#":
                user_response_check = True
                home_page()
            else:
                print("\nYou entered an invalid command: {}.".format(user_response))
                print("Please enter a valid command.")
                user_response = input("Please enter 1 to try again or # to go back to home page: ")

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
    question_list = db_get_questions_by_chap_num(chap_num)

    for question in question_list:
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
    print(question._name)
    print("\n")
    user_answer = input("answer: ")
    
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

def main():
    home_page()

def setup():
    db_setup()

main()
