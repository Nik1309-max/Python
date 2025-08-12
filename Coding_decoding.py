def coding_message():
    message = input("Enter your decoded message here to make it in coded: ").strip()
    message_list = message.split()
    code_1 = "asd"
    code_2 = "seu"  
    message_coded = ""

    for i in message_list:
        if len(i)>=3:
            first_letter = i[0]
            i = i[1:]
            i = code_1+i+first_letter+code_2
            message_coded=message_coded+i+" "

        else:
            i = i[::-1]
            message_coded=message_coded+i+" "
    print(message_coded)

def decoding_message():
    message = input("Enter coded message here to decode: ").strip()
    message_list = message.split()
    message_decoded = ""
    for i in message_list:
        if len(i)>=9:
            first_letter = i[-4]
            i =  first_letter+i[3:-4]
            message_decoded= message_decoded+i+" "
        else:
            i=i[::-1]
            message_decoded = message_decoded+i+" "
    print(message_decoded)

while True:
    user_inp = input("Enter 0  for coding and 1 for decoding and exit for exitting: ").strip().upper()
    if user_inp == "EXIT":
        print("Exitted from the program successfully.")
        break
    elif user_inp == "0":
        coding_message()
    elif user_inp == "1":
        decoding_message()
    else:
        print("Enter a valid input.")