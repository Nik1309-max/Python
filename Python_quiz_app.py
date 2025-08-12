import random
def easy_question_fn():
    with open("C:\\Users\\nkofb\\OneDrive\\Desktop\\cii\\hello.py\\Quiz text document\\Questions\\Easy questions.txt","r") as eq:
        easy_list = eq.read().split("\n")
    easy_ques_list = []
    score = 0
    i = 0
    while i<600:
        easy_ques_list.append({"Question": easy_list[i], 
                               "A": easy_list[i+1],
                               "B": easy_list[i+2],
                               "C": easy_list[i+3],
                               "D": easy_list[i+4],
                               "Right Answer": easy_list[i+5]
                               })
        i+=6
    ques_asked = []
    for i in range(5):
        ran_ques = random.choice(easy_ques_list)
        if ran_ques.get("Question") not in ques_asked:
            ques_asked.append(ran_ques.get("Question"))
            print(f"\nQ{i+1}):", ran_ques.get("Question")[3:])
            print( ran_ques.get("A"))
            print( ran_ques.get("B"))
            print( ran_ques.get("C"))
            print( ran_ques.get("D"))
            user_ans = input("Your answer: ").strip().upper()
            if user_ans == ran_ques.get("Right Answer")[4:]:
                score += 1
            elif  user_ans in ["A","B","C","D"]:
                pass
            else:
                print("--- Invalid input ---")
                pass
    print(f"{user_name} have scored {score}/5 in Python's easy quiz.")
    with open("C:\\Users\\nkofb\\OneDrive\\Desktop\\cii\\hello.py\\Quiz text document\\Leaderboard.txt","a") as le:
        le.write(f"\n{user_name} {score}")
def medium_question_fn():
    with open("C:\\Users\\nkofb\\OneDrive\\Desktop\\cii\\hello.py\\Quiz text document\\Questions\\Medium questions.txt","r") as mq:
        medium_list = mq.read().split("\n")
    medium_ques_list = []
    score = 0
    i = 0
    while i<600:
        medium_ques_list.append({"Question": medium_list[i], 
                                "A": medium_list[i+1],
                                "B": medium_list[i+2],
                                "C": medium_list[i+3],
                                "D": medium_list[i+4],
                                "Right Answer": medium_list[i+5]
                                })
        i+=6
    ques_asked = []
    for i in range(5):
        ran_ques = random.choice(medium_ques_list)
        if ran_ques.get("Question") not in ques_asked:
            ques_asked.append(ran_ques.get("Question"))
            print(f"\nQ{i+1}):", ran_ques.get("Question")[3:])
            print( ran_ques.get("A"))
            print( ran_ques.get("B"))
            print( ran_ques.get("C"))
            print( ran_ques.get("D"))
            user_ans = input("Your answer: ").strip().upper()
            if user_ans == ran_ques.get("Right Answer")[4:]:
                score += 1
            elif user_ans in ["A","B","C","D"]:
                pass
            else:
                print("--- Invalid input ---")
                pass
    print(f"{user_name} have scored {score}/5 in Python's medium quiz.")
    with open("C:\\Users\\nkofb\\OneDrive\\Desktop\\cii\\hello.py\\Quiz text document\\Leaderboard.txt","a") as lm:
        lm.write(f"\n{user_name} {score}")
def hard_question_fn():
    with open("C:\\Users\\nkofb\\OneDrive\\Desktop\\cii\\hello.py\\Quiz text document\\Questions\\Hard questions.txt","r") as hq:
        hard_list = hq.read().split("\n")
    hard_ques_list = []
    score = 0
    i = 0
    while i<600:
        hard_ques_list.append({"Question": hard_list[i], 
                                "A": hard_list[i+1],
                                "B": hard_list[i+2],
                                "C": hard_list[i+3],
                                "D": hard_list[i+4],
                                "Right Answer": hard_list[i+5]
                               })
        i+=6
    ques_asked = []
    for i in range(5):
        ran_ques = random.choice(hard_ques_list)
        if ran_ques.get("Question") not in ques_asked:
            ques_asked.append(ran_ques.get("Question"))
            print(f"\nQ{i+1}):", ran_ques.get("Question")[3:])
            print( ran_ques.get("A"))
            print( ran_ques.get("B"))
            print( ran_ques.get("C"))
            print( ran_ques.get("D"))
            user_ans = input("Your answer: ").strip().upper()
            if user_ans == ran_ques.get("Right Answer")[4:]:
                score += 1
            elif user_ans in ["A","B","C","D"]:
                pass
            else:
                print("--- Invalid input ---")
                pass
    print(f"{user_name} have scored {score}/5 in Python's hard quiz.")
    with open("C:\\Users\\nkofb\\OneDrive\\Desktop\\cii\\hello.py\\Quiz text document\\Leaderboard.txt","a") as lh:
        lh.write(f"{user_name} {score}\n")
def mixed_question_fn():
    with open("C:\\Users\\nkofb\\OneDrive\\Desktop\\cii\\hello.py\\Quiz text document\\Questions\\Mixed questions.txt","r") as mq:
        mixed_list = mq.read().split("\n")
    mixed_ques_list = []
    score = 0
    i = 0
    while i<600:
        mixed_ques_list.append({"Question": mixed_list[i], 
                               "A": mixed_list[i+1],
                               "B": mixed_list[i+2],
                               "C": mixed_list[i+3],
                               "D": mixed_list[i+4],
                               "Right Answer": mixed_list[i+5]
                                })
        i+=6
    ques_asked = []
    for i in range(5):
        ran_ques = random.choice(mixed_ques_list)
        if ran_ques.get("Question") not in ques_asked:
            ques_asked.append(ran_ques.get("Question"))
            print(f"\nQ{i+1}):", ran_ques.get("Question")[3:])
            print( ran_ques.get("A"))
            print( ran_ques.get("B"))
            print( ran_ques.get("C"))
            print( ran_ques.get("D"))
            user_ans = input("Your answer: ").strip().upper()
            if user_ans == ran_ques.get("Right Answer")[4:]:
                score += 1
            elif user_ans in ["A","B","C","D"]:
                pass
            else:
                print("--- Invalid input ---")
                pass
    print(f"{user_name} have scored {score}/5 in Python's mixed quiz.")
    with open("C:\\Users\\nkofb\\OneDrive\\Desktop\\cii\\hello.py\\Quiz text document\\Leaderboard.txt","a") as lm:
        lm.write(f"\n{user_name} {score}")   
         
def leaderboard_fn():
    with open("C:\\Users\\nkofb\\OneDrive\\Desktop\\cii\\hello.py\\Quiz text document\\Leaderboard.txt","r") as l:
        leader_list = l.read().split("\n")
    leader_name_list = []
    leader_score_list = []
    leader_dict = []

    count = 1
    for i in range(1,len(leader_list)):
        lead_list = leader_list[i].split(" ")
        leader_name_list.append(lead_list[0])
        leader_score_list.append(lead_list[1])
        leader_dict.append({"Name":leader_name_list[i-1],"Score":leader_score_list[i-1]})
        if int(leader_dict[i-1].get("Score")) == 5:
            print(f"{count}.)",leader_dict[i-1].get("Name"),"::",leader_dict[i-1].get("Score"))
            count+=1
        elif int(leader_dict[i-1].get("Score")) <= 4:
            print(f"{count}.)",leader_dict[i-1].get("Name"),"::",leader_dict[i-1].get("Score"))
            count+=1

while True:
    print("=== PYTHON QUIZ GAME ===")
    print("1. Start Quiz\n2. Leaderboard\n3. Leaderboard reset\n4. Exit")
    user_inp = int(input("Your choice: "))
    if user_inp == 1: 
        user_name = input("Enter your name here: ").strip().upper()
        print("--- QUESTION LEVEL ---")
        print("1. Easy questions\n2. Medium Questions\n3. Hard Questions\n4. Mixed Questions(Includes Easy,Medium and Hard)")
        user_inp2 = int(input("Your choice: "))
        if user_inp2 == 1:
            easy_question_fn()
        elif user_inp2 == 2:
            medium_question_fn()        
        elif user_inp2 == 3:
            hard_question_fn()
        elif user_inp2 == 4:
            mixed_question_fn()
        else:
            print("--- Invalid input ---")
    elif user_inp == 2:
        leaderboard_fn()
    elif user_inp == 3:
        with open("C:\\Users\\nkofb\\OneDrive\\Desktop\\cii\\hello.py\\Quiz text document\\Leaderboard.txt","w") as l:
            l.write("")
        print("--- Leaderboard resetted ---")
    elif user_inp == 4:
        print("=== Exitted from the quiz program ===")
        break
    else:
        print("--- Invalid input ---")