'''
This program can be used for 2 party voting system and could be modified for more party system. It also can be used for casting votes by user, declare result 
of the voting, delete all the data after the voting, verify the voter if it's in the voting list or not and atlast but not the least it also shows all of the 
voters name. 

This program can be more modified and could be more benificiary by adding some features like:
1. Delete the last vote by voter which was casted wrongly / by fault.
2. Adding more parties than only 2.
3. We can also add a file to access for fetching the data and id of voter and verify it before they cast the vote.

That's it, let's move to the real code and try to understand it.
'''

import random

# Function to cast vote by voter to any of two Parties.
def cast_vote(n):
    successful_votes = 0
    while successful_votes<n:
        voter_name = input("Enter voter's name here: ").strip().upper()
        with open("C:\\Users\\nkofb\\OneDrive\\Desktop\\cii\\hello.py\\Voting details\\Voter_list.txt","r") as d:
            voters_list = d.read().split(" | ")
        if voter_name in voters_list:
            print(f"{voter_name} has casted his vote once.")
            continue

         
        
        print(f"\n-- Voter {successful_votes+1} of {n} --")
        voter_choice = input("Party 1: Joginder Sharma \nParty 2: Urfi Singh\nChoose any one of them: ").strip()
        if voter_choice == "1":
            with open("C:\\Users\\nkofb\\OneDrive\\Desktop\\cii\\hello.py\\Voting details\\Party1_voter.txt","a") as p1:
                p1.write(f"{voter_name} | ")
            print("Your vote has been casted for Joginder Sharma.")
                
        elif voter_choice == "2":
            with open("C:\\Users\\nkofb\\OneDrive\\Desktop\\cii\\hello.py\\Voting details\\Party2_voter.txt","a") as p2:
                p2.write(f"{voter_name} | ")
            print("Your vote has been casted for Urfi Singh.")

        else:
            print("Invalid Input..!!. Vote not recorded")
            continue

        with open("C:\\Users\\nkofb\\OneDrive\\Desktop\\cii\\hello.py\\Voting details\\Voter_list.txt","a") as a:
            a.write(f"{voter_name} | ") 
        successful_votes+=1          

# Function to declare result after the end of casting vote.
def declare_result():
    num_party1 = 0
    num_party2 = 0
    with open("C:\\Users\\nkofb\\OneDrive\\Desktop\\cii\\hello.py\\Voting details\\Party1_voter.txt","r") as p1:
        num_party1+=(len(p1.read().split(" | "))-1)
    p1.close()
    with open("C:\\Users\\nkofb\\OneDrive\\Desktop\\cii\\hello.py\\Voting details\\Party2_voter.txt","r") as p2:
        num_party2+=(len(p2.read().split(" | "))-1)
    p2.close()

    if num_party1>num_party2:
        print(f"Party 1: {num_party1} Votes \nParty 2: {num_party2} Votes")
        print("Party 1 Won.")
    elif num_party1<num_party2:
        print(f"Party 1: {num_party1} Votes \nParty 2: {num_party2} Votes")
        print("Party 2 Won.")
    elif num_party1 == 0 and num_party2==0:
        print("No Votes has been casted..")
    elif num_party1==num_party2:
        print(f"Party 1 and Party 2, both got {num_party1}-{num_party2} votes.")
        print("So the winner will be decided by random choice of system...")
        ran_choice = random.choice(["Party 1","Party 2"])
        print(f"{ran_choice} Won.")
    
# Funtion to delete all the vote casted and all the data.
def delete_vote():
    with open("C:\\Users\\nkofb\\OneDrive\\Desktop\\cii\\hello.py\\Voting details\\Voter_list.txt","w") as d:
        d.write("")
    
    with open("C:\\Users\\nkofb\\OneDrive\\Desktop\\cii\\hello.py\\Voting details\\Party1_voter.txt","w") as p1:
        p1.write("")
    
    with open("C:\\Users\\nkofb\\OneDrive\\Desktop\\cii\\hello.py\\Voting details\\Party2_voter.txt","w") as p2:
        p2.write("")
   
    print("All data removed")

# Funtion to check the voter is present in voting list or not.
def verify_voter(voter):
    with open("C:\\Users\\nkofb\\OneDrive\\Desktop\\cii\\hello.py\\Voting details\\Voter_list.txt","r") as a:
       voter_list = a.read().split(" | ")
    if voter in voter_list:
        print(f"{voter} has casted his/her vote before.")
    else:
        print(f"{voter} hasn't casted his/her vote yet.")

# Function to show all of the voter name.
def show_voters_name():
    with open("C:\\Users\\nkofb\\OneDrive\\Desktop\\cii\\hello.py\\Voting details\\Voter_list.txt","r") as f:
        voters_list = f.read().split(" | ")
    if len(voters_list)!=0:
        for i in range(0,len(voters_list)-1):
            print(f"{i+1}. {voters_list[i]}")
    else:
        print("Voting is yet to be held...")

# Loop to execute all the above functions for user.
while True:
    user_inp = input("Start/Result/Delete/Verify/Voters/exit: ").strip().upper()
    if user_inp == "START":
        try:
            no_of_voters = int(input("Enter number of total voters: "))
            cast_vote(no_of_voters)
        except ValueError:
            print("Please enter a valid number.")
    elif user_inp == "VOTERS":
        show_voters_name()
    elif user_inp == "VERIFY":
        voter_name = input("Enter the voter name to check: ").strip().upper()
        verify_voter(voter_name)
    elif user_inp == "EXIT":
        print("Exitted from the voting program")
        break
    elif user_inp == "RESULT":
        declare_result()
    elif user_inp == "DELETE":
        delete_vote() 
    else:
        print("Invalid Input..!!")
        continue