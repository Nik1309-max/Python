import random as ran
import time 
file_path = "C:\\Users\\nkofb\\OneDrive\\Desktop\\cii\\hello.py\\words_directory.txt"

def game_fun_code():
    with open(file_path,'r') as word_directory:
        word_lines = word_directory.read().split("\n")

    word_dict = {}
    for i in word_lines:
        word_dict[i.split(":")[0]] = i.split(":")[1]
    game_word_list = []
    while len(game_word_list)<5:
        random_word = ran.choice(list(word_dict.keys())).strip().capitalize()
        if random_word not in game_word_list:
            game_word_list.append(random_word)

    words_after_letter_removal = []
    for i in game_word_list:
        word_list = [k for k in i]
        word_index = [j for j in range(len(i))]
        index_to_removed = ran.choices(word_index,k=2)
        for z in index_to_removed:
            word_list[z] = "_"
        words_after_letter_removal.append("".join(word_list))

    user_input = []
    time_taken_in_unit = []
    time_taken_in_seconds = []
    for j in range(5):
        time_start = time.time()
        print(f"\n{j+1}.) Guess the word\n    {words_after_letter_removal[j]}          (Hint: {word_dict[game_word_list[j]]})")
        inp = input("Enter the guessed word: ").strip().capitalize()
        time_end = time.time()
        print("\n=========================================================================================================")
        user_input.append(inp)
        time_taken_in_seconds.append(time_end-time_start)
        if time_end-time_start>60:
            time_taken_in_unit.append(f"{(time_end-time_start)/60:.2f} minutes")
        else:
            time_taken_in_unit.append(f"{(time_end-time_start):.2f} seconds")

    
    score = 0
    result = []
    for i in range(5):
        if user_input[i]==game_word_list[i]:
            result.append("Correct")
            score+=1
        else:
            result.append("Incorrect")

    print(f"You got {score} words correct.\n")
    while True:
        inp = input("Enter `Show` for displaying mangled words and your response or enter `play` to play more: ").strip().lower()
        if inp=="play":
            game_fun_code()
        elif inp=="show":
            print("===========================================================\n")
            print(f"{" "*5}Mangled Words     Your Response     Result     Time Taken")
            print(f"   -------------------------------------------------------------")
            for j in range(5):
                print(f"{j+1}.)  {game_word_list[j]}{" "*(18-len(game_word_list[j]))}{user_input[j]}{" "*(18-len(user_input[j]))}{result[j]}{" "*(11-len(result[j]))}{time_taken_in_unit[j]}")
            print(f"   -------------------------------------------------------------")
            if sum(time_taken_in_seconds)>60:
                print(f"                                  Total time taken: {sum(time_taken_in_seconds)/60:.2f} minutes")
            else:
                print(f"                                 Total time taken: {sum(time_taken_in_seconds):.2f} seconds")
            print("\n===========================================================")
            break

        else:
            print("\n***************** Error ********************\n")
            
def add_words():
    with open(file_path,"a") as word_directory:
        inp_word = input("Enter the word here: ")
        inp_hint = input("Enter the hint here: ")
        
while True:
    print("\n======= Word Guessing Game =======\n")
    print("Choose any one from below option:\n1.) PLAY >> to play the game\n2.) ADD >> to add more words in the game\n3.) EXIT >> to exit from game")
    inp = input("Enter your choice here: ").lower().strip()
    if inp=="exit":
        print("Program ended successfully.")
        print("============================================\n")
        break
    elif inp == "play":
        game_fun_code()
    else:
        print("\n************** ERROR 404 *******************\n")
