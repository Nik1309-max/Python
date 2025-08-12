'''
computer = S G W 
human =  S D L W
         G W D L          # Win or Lose chances of each party, i.e. computer/human
         W L W D
'''
import random as r
computer_choices = ["Snake","Gun","Water"]
human_score = 0
computer_score = 0

# Function controlling the game
def game_operating_code():
    global human_score,computer_score
    human = input("Select Snake,Water or Gun: ").strip().lower()   # User input
    option = r.choice(computer_choices).lower()     # Computer choice choosed randomly

    if human in computer_choices:
        print(f"Computer's selection is: {option}")      # Computer choice randomly
    else:
        print("Invalid input!")
        
    if option == human:
        print("DRAW")
        print(f"You:{human_score}  Computer:{computer_score}")       # Draw result
    elif (option=="snake" and human=="water") or (option=="water" and human=="gun") or (option=="gun" and human=="snake"):
        computer_score+=1
        print("You Lose, Computer Won")
        print(f"You:{human_score}  Computer:{computer_score}")       # Computer Win
    elif (option=="gun" and human=="water") or (option=="water" and human=="snake") or (option=="snake" and human=="gun"):
        human_score+=1
        print("You Won, Computer Lose")
        print(f"You:{human_score}  Computer:{computer_score}")        # Human Win
    
# Infinite loop till user doesn't select exit from app/game
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
