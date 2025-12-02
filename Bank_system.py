'''
This python program is a banking system which gives user function to make a new account, show balance of their account, deposit money in their account and 
debit money from their account.

This program can be more modified and make it more efficient by adding more functions like:
1. Delete the bank account of user.
2. Adding the transaction data of each user either in their file or making a folder for each user and print it whenever user wants it.
3. Give the user option either to open current/ saving account.
4. Fn to make user FD of the amount or random amount FD.
5. also add the timing module to track all the transactions of user.

Let's move to the real code.
'''

import random
import time
# Function to make new bank account.

path = "C:\\Users\\HP\\Desktop\\Coding\\Python\\Bank sys\\"
def new_account():
    acc_num_list = []
    acc_name_list = []
    with open(path+f"Bank_Details.txt","r") as bsr:
        acc_details = bsr.read().split()
    for i in range(len(acc_details)):
        if i%2==0:
            acc_num_list.append(acc_details[i])
        else:
            acc_name_list.append(acc_details[i])

    try:
        user_name = input("\n\tName: ").strip().upper()
        user_dob = input("\tDate Of Birth(DD/MM/YYYY): ").strip()
        user_father_name = input("\tFather's name: ").strip().upper()
        user_mother_name = input("\tMother's name: ").strip().upper()
        user_money_deposit = int(input("\tDeposit min Rs. 1000: "))
        if user_name not in acc_name_list:
            time.sleep(0.5)
            print(f"\n\tYour account number is {bank+acc_num}.")
            with open(path+f"{bank+acc_num}.txt","a") as an:
                an.write(f"Name: {user_name}\nDOB: {user_dob}\nFather's name: {user_father_name}\nMother's name: {user_mother_name} \nBank Account Number: {bank+acc_num}\nAccount Balance: {user_money_deposit}")
            with open(path+f"Bank_Details.txt","a") as bs:
                bs.write(f"{bank+acc_num} {user_name} ")
        else:
            print(f"\n\t{user_name} already have an account in our bank.\n")
    except ValueError:
        print("\n\tSahi se paise daal text kyu daal rha")

# Funtion to show the balance of existing bank user.
def show_balance():
    user_inp = input("\n\tEnter your account num: ").strip()
    acc_num_list = []
    acc_name_list = []
    with open(path+f"Bank_Details.txt","r") as bsr:
        acc_details = bsr.read().split()
    for i in range(len(acc_details)):
        if i%2==0:
            acc_num_list.append(acc_details[i])
        else:
            acc_name_list.append(acc_details[i])
    if user_inp in acc_num_list:
        
        with open(path+f"{user_inp}.txt","r") as bsr:
            acc_details = bsr.read().split("\n")
        bank_balance = acc_details[5]
        print(bank_balance)
    else:
        print(f"\n\tAccount number: {user_inp} doesn't exist in our bank.\n")

# Function to deposit money by existing bank user.
def deposit_money(amount):
    user_inp = input("\nEnter your account number: ").strip()
    acc_num_list = []
    
    # Load all account numbers
    with open(path+"Bank_Details.txt", "r") as bsr:
        acc_details = bsr.read().split()
        acc_num_list = acc_details[::2]  # Even-indexed items are account numbers
    
    if user_inp in acc_num_list:
        user_file_path = path+f"{user_inp}.txt"

        # Read account file
        with open(user_file_path, "r") as bsr:
            lines = bsr.readlines()
        
        # Extract balance
        bal_line = lines[5].strip()
        key, value = bal_line.split(": ")
        current_balance = int(value)


        new_balance = current_balance + amount
        lines[5] = f"{key}: {new_balance}\n"

            # Write updated balance back
        with open(user_file_path, "w") as bsw:
            bsw.writelines(lines)

        print(f"\n\t₹{amount} credited successfully. Remaining balance: ₹{new_balance}\n")
    else:
        print(f"\n\tAccount number {user_inp} doesn't exist in our bank records.\n")

# Function to debit money by existing bank user. It doesn't debits money if balance is less than the debit amount.
def debit_money(amount):
    user_inp = input("\n\tEnter your account number: ").strip()
    acc_num_list = []
     
    # Load all account numbers
    with open(path+"Bank_Details.txt", "r") as bsr:
        acc_details = bsr.read().split()
        acc_num_list = acc_details[::2]  # Even-indexed items are account numbers
    
    if user_inp in acc_num_list:
        user_file_path = path+f"{user_inp}.txt"

        # Read account file
        with open(user_file_path, "r") as bsr:
            lines = bsr.readlines()
        
        # Extract balance
        bal_line = lines[5].strip()
        key, value = bal_line.split(": ")
        current_balance = int(value)

        if current_balance >= amount:
            new_balance = current_balance - amount
            lines[5] = f"{key}: {new_balance}\n"

            # Write updated balance back
            with open(user_file_path, "w") as bsw:
                bsw.writelines(lines)

            print(f"\n\t₹{amount} debited successfully. Remaining balance: ₹{new_balance}\n")
        else:
            print(f"\n\tInsufficient funds. Account {user_inp} has only ₹{current_balance}.\n")
    else:
        print(f"\n\tAccount number {user_inp} doesn't exist in our bank records.\n")

# Making the new and unique bank account numbers.
bank = "1100001"
list = ["0","1","2","3","4","5","6","7","8","9"]
acc_num_list = []
ran_list = random.choices(list,k=4)
acc_num = "".join(ran_list)

# Loop to ask the user either they want to make a new account/want to their account balance/want to make any transaction/exit the bank system.
while True:
    user_inp = input("\n\tNew Account / Balance / Transaction / Exit: ").strip().lower()
    if user_inp == "n":
        time.sleep(0.5)
        new_account()  
    elif user_inp == "b":
        time.sleep(0.5)
        show_balance()
    elif user_inp == "t":
        time.sleep(0.5)
        user_inp2 = input("\tDeposit or Debit: ")
        if user_inp2 == "dep":
            time.sleep(0.5)
            amount = int(input("\tAmount: "))
            deposit_money(amount)
        elif user_inp2 == "deb":
            time.sleep(0.5)
            amount = int(input("\tAmount: "))
            debit_money(amount)
        else:
            time.sleep(0.5)
            print("\t2 hi option the wo bhi thik se nhi chuna jaa raha...\n")
    elif user_inp == "exit":
        time.sleep(0.5)
        print("\n\tApp closed successfully\n")
        break
    else:
        time.sleep(0.5)
        print("\tOptions ke alwa kyu choose kiya ab dobara choose kar ... \n")
