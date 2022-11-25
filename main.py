from db import *

def setup():
    db_setup()

def settings():
    pass

def home_page():
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

def mode_page():
    print("---------------\n")
    print("""Mode page
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
            campaign_mode()
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

def campaign_mode():
    print("---------------\n")
    print("Welcome to Campaign mode!")
    print("""Pick a chapter:
    1 - Chapter 1
    2 - Chapter 2
    3 - Chapter 3
    # - Back to Mode page""")
    print("---------------")

    user_response_check = False
    user_response = input("Please enter 1 to choose Chapter 1, 2 to choose Chapter 2, 3 to choose Chapter 3 or # to go back to Mode page: ")

    while not user_response_check:
        if user_response == "1" or user_response == "Chapter 1" or user_response == "chapter 1":
            user_response_check = True
            print("\nYou have chosen 1 - Chapter 1.")
            #TODO: Chapter 1 page
        elif user_response == "2" or user_response == "Chapter 2" or user_response == "chapter 2":
            user_response_check = True
            print("\nYou have chosen 2 - Chapter 2.")
            #TODO: Chapter 2 page
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

def get_question():
    pass

home_page()

