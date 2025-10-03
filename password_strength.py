def check_strength(password):
    letters = "abcdefghijklmnopqrstuvwxyz"
    lowercase_count = 0
    uppercase_count = 0
    num = 0
    special_char = 0
    special_chars = "!@#$%^&*"
    for i in password:
        if i.isdigit() and num<1:
            num+=1
        elif i in letters and lowercase_count<1:
            lowercase_count+=1
        elif i in letters.upper() and uppercase_count<1:
            uppercase_count+=1
        elif i in special_chars and special_char<1:
            special_char+=1

    
    if len(password)>=8 and num and special_char and lowercase_count and uppercase_count:
        return "Strong"
    elif len(password)+num>=9 or len(password)+special_char>=9 or len(password)+lowercase_count+uppercase_count>=10 or uppercase_count+lowercase_count+special_char>=3 or uppercase_count+lowercase_count+num>=3 or num+special_char>=2 or len(password)+uppercase_count+lowercase_count+num>=11 or uppercase_count+lowercase_count+num+special_char>=4 or len(password)+uppercase_count+lowercase_count+special_char>=11:
        return "Medium"
    else:
        return "Weak"
    
    
while True:
    n = input("Enter your password: ")
    print(f"Your password is {check_strength(n)}")