import random
attempts_list = []
def show_score():
    if len(attempts_list) <= 0:
        print("There is currently no high score, its your for the taking!")
    else:
        print("The current high score is {} attempts".format(min(attempts_list)))
def start_game():
    random_number = int(random.randint(1,10))
    print("Hey There! Welcome to the game of guesses!")
    player_name = input("Enter your name!")
    wanna_play =input("Hi, {}, wouldyou like to play the play the guessing game?"("Enter Yes/No").formate(player_name))
    attempts = 0
    show_score()
    while wanna_play.lower() == "yes":
        try:
           guess = input("Pick a number btween 1 and 10")
           if int(guess) < 1 or int(guess) > 10:
               raise ValueError("Please guess a number within the given range")
           if int(guess) == random_number:
               print("Congrates! You guesed it right!")
               attempts += 1
               attempts_list.append(attempts)
               print("It took you {} attempts".format(attempts))
               player_again = input("Would you like to play again? (Enter Yes/No)")
               attempts = 0
               random_number = int(random.randint(1,10))
               if player_again.lower() == "no":
                   print("Thats cool, have a nice day!")
                   break
           elif int(guess) < random_number:
                print("Its lower ")
                attempts +=1
           elif int(guess) > random_number:
               print("Its higher") 
               attempts += 1
        except ValueError as err:
            print("Oh!, that is not a valid value. Try again...")
            print("({})".format(err))
    else:
        print("Thats cool, have a nice day!")  
if __name__== "__main__":
    start_game()              
               
