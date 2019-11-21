"""
integration project: sports trivia game
__author__ = Allan Marin
"""


def main():
    """
    Starts the program
    :return:
    """
    score = 0
    print("Hello and welcome to sports trivia!")
    user_wishes_to_continue = True
    while user_wishes_to_continue:
        # Main Menu
        print("Main Menu")
        print("1) play")
        print("2) info")
        print("3) exit")
        print("Stars:")
        for stars in range(score):
            print("*" + "", end="")
        print("")
        main_menu = int(input("Enter the number of menu option desired: "))
        # play options menu
        if main_menu == 1:
            print("Sports Option Menu")
            print("1) Football")
            print("2) Basketball")
            print("3) Baseball")
            print("4) Hockey")
            print("5) Soccer")
            user_input = int(input("Enter the number of sport "
                                   "option desired: "))
            # football is selected
            if user_input == 1:
                print("You Chose Football Trivia!")
                print("Let's Begin!")
                # football question 1
                print("Question 1: Who won Super Bowl 51 in 2017?")
                print("Answers:")
                print("1 ) Atlanta Falcons")
                print("2 ) New England Patriots")
                print("3 ) Oakland Raiders")
                print("4 ) Baltimore Ravens")
                user_input = int(input("Enter Answer Here: "))
                if user_input == 2:
                    print("correct! The New England Patriots won Super Bowl"
                          " 51 in 2017 against the Atlanta Falcons.")
                    score = score + 1
                    print("score:", score)
                else:
                    print("Incorrect, The New England Patriots won Super Bowl"
                          " 51 in 2017 against the Atlanta Falcons.")
                    print("score:", score)
                # next question 1
                user_input = askingUsertoContinue()
                # football question 2
                if user_input == 3:
                    user_wishes_to_continue = False
                    print("Thank you for playing")
                elif user_input == 1:
                    print("Question 2: who owns the current title of most"
                          " running yards in their career as of 2019?")
                    print("1) Frank Gore")
                    print("2) Adrian Peterson")
                    print("3) Emmitt Smith")
                    print("4) Josh Jacobs")
                    user_input = int(input("Enter Ansewer Here: "))
                    if user_input == 3:
                        print(
                            "Correct, Emmit smith has the record for most"
                            " running yards in a career with a total of"
                            " 18,355 yards!")
                        score = score + 1
                        print("score:", score)
                    else:
                        print(
                            "incorrect,Emmit smith has the record for most"
                            " running yards in a career with a total of"
                            " 18,355 yards!")
                        print("score:", score)
                    # next question 2
                    user_input = askingUsertoContinue()
                    # end game after question 1
                    if user_input == 3:
                        user_wishes_to_continue = False
                        print("Thank You for playing!")
                        print("score:", score)
                    elif user_input == 1:
                        # football question 3
                        print("Question 3: Who is the starting quarterback of"
                              " the packers as of 2019?")
                        print("1) Derk Carr")
                        print("2) Tom Brady")
                        print("3) Aaron Rodgers")
                        print("4) Cam Newton")
                        user_input = int(input("Enter Answer Here:"))
                        if user_input == 3:
                            print("Correct, Aaron Rodgers is the starting"
                                  " quarterback for the Packers as of 2019.")
                            score = score + 1
                            print("score:", score)
                        else:
                            print("Incorrect, Aaron Rodgers is the startign"
                                  " quarterback for the Packers as of 2019.")
                        print(
                            "Thank You for playing the football portion of"
                            " Sports Trivia! Would you like to return to ")
                        print("score:", score)
                        print("1) Return to Main Menu")
                        print("2) End Game")
                        user_input = int(input("Enter Answer Here:"))
                        if user_input == 2:
                            user_wishes_to_continue = False
                            print("Thank You for playing!")
                            print("score:", score)
            # basketball is selected
            elif user_input == 2:
                print("You Chose Basketball Trivia!")
                print("Lets Begin!")
                # basketball question 1
                print("Question 1: What team did LeBron James get drafted to?")
                print("Answers:")
                print("1 ) Clevland Cavaleirs")
                print("2 ) Toronto Raptors")
                print("3 ) Miami Heat")
                print("4 ) Chicago Bulls")
                user_input = int(input("Enter Answer Here:"))
                if user_input == 1:
                    print("Correct, LeBron James was drafted to the"
                          " Clevland Calvaliers in 2003.")
                    score = score + 1
                    print("score:", score)
                else:
                    print("incorrect, LeBron James was drafted to the"
                          " Clevland Cavaliers in 2003.")
                    print("score:", score)
                # next question 3
                user_input = askingUsertoContinue()
                # exit for basketball question 1
                if user_input == 3:
                    user_wishes_to_continue = False
                    print("Thank You for playing!")
                    # main menu for basketball question 1
                elif user_input == 1:
                    # basketball question 2
                    print("Question 2: Who holds the record for most NBA"
                          " championships as of 2019?")
                    print("1) LA Lakers")
                    print("2) Chicago Bulls")
                    print("3) Boston Celtics")
                    print("4) Golden State Worriors")
                    user_input = int(input("Enter Answer Here: "))
                    if user_input == 3:
                        print("correct, the Boston Celtics hold the Most"
                              " NBA championships with a total of 17")
                        score = score + 1
                        print("score:", score)
                    else:
                        print("incorrect, the Boston Celtics hold the Most"
                              " NBA championships with a total of 17")
                        print("score:", score)
                    # next question 4
                    user_input = askingUsertoContinue()
                    # exit for basketball question 2
                    if user_input == 3:
                        user_wishes_to_continue = False
                        print("Thank You for playing!")
                        # basketball question 3
                    elif user_input == 1:
                        print("Question 3: How many NBA teams are"
                              " there as of 2019")
                        print("1) 32")
                        print("2) 30")
                        print("3) 18")
                        print("4) 46")
                        user_input = int(input("Enter Answer Here:"))
                        if user_input == 2:
                            print("Correct, There are currently 30 NBA"
                                  " teams as of 2019")
                            score = score + 1
                            print("score:", score)
                        else:
                            print("Incorrect, There are currently 30 NBA"
                                  " teams as of 2019")
                            print("score:", score)
                        print(
                            "Thank You for playing the basketball portion"
                            " of Sports Trivia! Would you like to return to ")
                        print("1) Return to Main Menu")
                        print("2) End Game")
                        user_input = int(input("Enter Answer Here:"))
                        # Exit for basketball question 3
                        if user_input == 2:
                            user_wishes_to_continue = False
                            print("Thank You for playing!")
                # baseball is selected
                elif user_input == 3:
                    print("Coming Soon")
                # hockey is selected
                elif user_input == 4:
                    print("Coming Soon")
                # soccer is selected
                elif user_input == 5:
                    print("Coming Soon")
        # info from main menu
        elif main_menu == 2:
            print("Game Info")
            print(
                "Thank you for playing Sports Trivia! This trivia game is"
                " a basic knowledge quiz about various sports.\nIn the "
                "Sports"
                " options menu you can select one of 5 different sports to be"
                " quized on.\nEach sport has 3 questions and you will be"
                " awarded 1 point for every question correctly answered."
                " \nWhen you end the game you will recive a *for how many "
                "points you have earned. Challenge your friends to see who"
                " knows the most across all 5 sports!")
            print(" ")
            print("Please select and option below")
            print("1) return to Main Menu")
            print("2) Exit game")
            user_input = int(input("Enter menu option desired here:"))
            if user_input == 2:
                user_wishes_to_continue = False
                print("Thank You for playing!")
        # exit from Main Menu
        elif main_menu == 3:
            user_wishes_to_continue = False
            print("Thank You for playing!")
            print("score:", score)


def askingUsertoContinue():
    """
    displays a reoccurring question
    """
    print("would you like another question?")
    print("1 ) yes")
    print("2 ) return to Main Menu")
    print("3 ) exit game")
    user_input = int(input("enter answer here:"))
    return user_input


"""
    returms the user input to the to either deplay next question, 
    return to main menu or end game
"""

main()
