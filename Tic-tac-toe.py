'''
1|2|3
4|5|6
7|8|9

123,456,789,147,258,369,159,357

We have to include the return to input when user gave the position taken input or invalid input for now it's just break the loop when we get error in case of 
empty input or invalid input or position which is been taken by another player already before.

'''

def game_work_code():
        # Game board which would be changed by it's positions by players input.
        game_board = '''1|2|3
4|5|6
7|8|9'''            

        pos_taken = set()    # It keeps data of both players taken positions of game board.
        win_pos_list = ["123","321","312","231","213","132","456","465","564","546","645","654","789","798","987","978","879","897","147","174","471","147","741","714","258","285","582","528","825","852","369","396","936","963","693","639","159","195","591","519","915","951","357","375","537","573","735","753"]     # These are the winning position list/values which need to any player for winning game.
        user1_inp_set = set()
        user2_inp_set = set()

        while True:
            # Draw condition which works when players take 8 out of 9 positions and no-one is won yet so system declare that game as draw.
            if len(pos_taken)>=8:
                if (user1_inp_str not in win_pos_list or user2_inp_str not in win_pos_list):
                    print("\n=== Draw ===\n")
                    break
            else:
                # Now the game part begins
                print(f"\n{game_board}")
                user1_inp = int(input("Player 1 position: "))
                # If player 1 position is new position then it will acquire that position in board as "X"
                if user1_inp not in pos_taken:
                    game_board = game_board.replace(str(user1_inp),"X")
                    print(f"\n{game_board}")
                    pos_taken.add(user1_inp)
                    user1_inp_set.add(user1_inp)
                    user1_inp_list = [str(i) for i in user1_inp_set]
                    user1_inp_str = "".join(user1_inp_list)
                    print(user1_inp_str)
                    # This will check if player 1's 3 positions are in winning conditions or not is it is then it will declare the result.
                    if user1_inp_str in win_pos_list or user1_inp_str[-3:] in win_pos_list:
                        print(f"\n=== Player 1 Won ===\n")
                        break
                # This statement simply stops the player 1 to take the position of player 2 already taken position.
                elif user1_inp in pos_taken:
                    print(f"Position taken by Player 2.")
                    break
                # This statement stops user to give any other input other than numbers
                else:
                    print("Invalid Input.")
                    break

                user2_inp = int(input("Player 2 position: "))
                # If player 2 position is new position then it will acquire that position in board as "O"
                if user2_inp not in pos_taken: 
                    game_board = game_board.replace(str(user2_inp),"O")
                    print(f"\n{game_board}")
                    pos_taken.add(user2_inp)
                    user2_inp_set.add(user2_inp)
                    user2_inp_list = [str(i) for i in user2_inp_set]
                    user2_inp_str = "".join(user2_inp_list)
                    print(user2_inp_str)
                    # This will check if player 2's 3 positions are in winning conditions or not is it is then it will declare the result.
                    if user2_inp_str in win_pos_list or user1_inp_str[-3:] in win_pos_list:
                        print(f"\n=== Player 2 Won! ===\n")
                        break
                # This statement simply stops the player 2 to take the position of player 1 already taken position.
                elif user2_inp in pos_taken:
                    print(f"Position taken by Player 1.")
                    break
                # This statement stops user to give any other input other than numbers
                else:
                    print("Invalid Input.")
                    break          
            
# Game won't stop with using while loop user have to select either "play" so he/she can enter in game or "exit" to exit from the game
while True:
    user_inp = input("Want to play Tic-Tac_toe or Exit from game: ").lower().strip()
    if user_inp == "exit":
        print("Exitted from the game.")
        break
    elif user_inp == "play":
        game_work_code()
    else:
        print("--- Invalid Input ---")