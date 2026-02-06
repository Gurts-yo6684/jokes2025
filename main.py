

# # make this performance task ready for submission
# # To give the user a fun experience hearing knock knock jokes

# joke = input("Do you want to hear a joke? ")
# if joke == "no":
#     print("Okay suit yourself!")
# while joke == "yes":
#     print("Great, Let's Play")
#     question = input("Do you want to hear a joke about robbers, tanks, or pencils? ")
#     if question == "robbers":
#         input("Knock Knock ")
#         input("Calder")
#         print("Calder police - I've been robbed!")
#         joke = input("Do you want to hear another joke or are you finished? ")
#     elif question == "tanks":
#         input("Knock Knock ")
#         input("Tank ")
#         input("You are welcome! ")
#         joke = input("Do you want to hear another joke or are you finished? ")
#     elif question == "pencils":
#         input("Knock Knock ")
#         input("Broken pencil ")
#         input("Nevermind, it's pointless! ")
#         joke = input("Do you want to hear another joke or are you finished? ")
# if joke == "finished":
#     rate = int(input("Please rate our game 1-10! "))
#     final_score = int(rate * 10)
#     print(str(final_score) + " percent satisfaction rate")
#     friend = input("Would you recommend this game to a friend? ")

#     if friend == "yes" or friend == "maybe":
#         print("Thanks, we appreciate it. ")
#     else:
#         print("Sorry you did not enjoy it. ")



#dada necessities

#At least one list
# At least two functions
# At least one abstraction
# Parameters used inside function calls
# A clear algorithm with sequencing, selection, and iteration
# Meaningful input and output
# Cleaner structure and reduced repetition





# def deliver_joke(setup, punchline):
#     input(f"{setup} ")
#     print(f"{punchline}")

# class JokeCollection:
#     def __init__(self):
#         # A list to store the jokes as dictionaries
#         self.jokes = [
#             {
#                 'category': 'robbers',
#                 'setup': 'Knock Knock',
#                 'punchline_part1': 'Calder',
#                 'punchline_part2': "Calder police - I've been robbed!"
#             },
#         ]
           
        

# tank.joke= [
#        {
#                 'category': 'tanks',
#                 'setup': 'Knock Knock',
#                 'punchline_part1': 'Tank',
#                 'punchline_part2': 'You are welcome!'
#             },
# ]

# pencil.joke=[ {
#                 'category': 'pencils',
#                 'setup': 'Knock Knock',
#                 'punchline_part1': 'Broken pencil',
#                 'punchline_part2': "Nevermind, it's pointless!"
#             }]
# def options():
#     options1= "Do you want to hear a joke about robbers, tanks, or pencils? "

# jokes= []

# joke = input("Do you want to hear a joke? ")
# if joke == "no":
#     print("otay bye")
# else:

#     print(input( "okay, pick a joke!!! tank, pencil, or robber?"))
# if joke == tank:
  


def tell_joke(setup, punchline):
    print("Knock, knock.")
    input("... ")
    print(setup)
    input("... ")
    print(punchline)
    print("Funny, right??!!?!?! :)")

def get_feedback():
        rate = int(input("Please rate our game 1-10! "))
        for rate in range(1, 11):
            if rate >= 1:
                final_score = rate * 10
            else: final_score = 0
        print(f"{final_score}% satisfaction rate! Thanks!")

    
def get_friend_recommendation():
        friend = input("Would you recommend this game to a friend? (yes/no/maybe): ").lower()
        if friend == "yes" or friend == "maybe":
            print("Thanks, we appreciate it.")
        else:
            print("Sorry you did not enjoy it.")

jokes_list = [
    ("Calder", "Calder police, I've been robbed!"),
    ("Tank", "You are welcome!"),
    ("Broken pencil", "Nevermind, it's pointless!")
]
#main code
play = input("Do you want to hear a joke? (yes/no): ").lower()

while play == "yes":
    print("--- Joke Time ---")
    print("1. Robbers")
    print("2. Tanks")
    print("3. Pencils")
    
    choice = input("Do you want to hear a joke about robbers, tanks, or pencils? (1/2/3): ")

    if choice == "1":
        tell_joke(jokes_list[0][0], jokes_list[0][1])
    elif choice == "2":
        tell_joke(jokes_list[1][0], jokes_list[1][1])
    elif choice == "3":
        tell_joke(jokes_list[2][0], jokes_list[2][1])
    else:
        print("That's not an option!")

    play = input("Do you want to hear another joke? (yes/no): ").lower()


print("Okay, suit yourself!")
get_feedback()
get_friend_recommendation()
print("Game Over.")
