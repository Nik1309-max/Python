'''
computer = S G W 
human =  S D L W
         G W D L
         W L W D
'''
import random as r
computer_choices = ["Scissor","Stone","Paper"]
human_score = 0
computer_score = 0
def game_operating_code():
    global human_score,computer_score
    human = input("Select Scissor,Paper or Stone: ").strip().lower()
    option = r.choice(computer_choices).lower()
    if human=="scissor" or human=="paper" or human=="stone":
        print(f"Computer's selection is: {option}")
    else:
        print("Invalid input!")
        
    if option == human:
        print("DRAW")
        print(f"You:{human_score}  Computer:{computer_score}")
    elif (option=="scissor" and human=="paper") or (option=="paper" and human=="stone") or (option=="stone" and human=="scissor"):
        computer_score+=1
        print("You Lose, Computer Won")
        print(f"You:{human_score}  Computer:{computer_score}")

    elif (option=="stone" and human=="paper") or (option=="paper" and human=="scissor") or (option=="scissor" and human=="stone"):
        human_score+=1
        print("You Won, Computer Lose")
        print(f"You:{human_score}  Computer:{computer_score}")
    
while True:
    if human_score==3 or computer_score==3:
        print(f"Round Ends {"You won" if human_score==3 else "Computer won"}")
        human_score=0
        computer_score=0            # Scores return to 0
        human_inp = input("Want to play another round or want to exit?").lower().strip()   # User input for next round/exit
        if human_inp == "exit":
            print("Game is closed successfully.")
            break
        elif human_inp=="play":
            print("Another round starting...")
            game_operating_code()  
        else:
            print("Invalid input!")
    
    else:
        game_operating_code()