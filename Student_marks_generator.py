'''
This Python program makes a temporary list of dictionary of data of the student provided by the school staff/teacher and it also calculates the percentage, 
grade and total marks scored by student. It also verify the teacher/staff name and it's password otherwise they can't access the data.

This program can more beneficiary by adding some features:
1. Add the main positions of staff and make a hierarchy like principal can delete or add teacher, but teacher can only add student or delete it.
2. Convert the student temporary data in permanent data by using file I/O.
3. We can divide the students according to their classes and compare their marks by the topper of the class and also give the average score of their class
   in all the subjects and total marks.

Now let's move to the real code and try to understand it. 
'''




# Temporary list of dictionary keys with all the data of student
student_data=[{"Name":"NIK","Science Grades":89,"Maths Grades": 99, "Sst Grades":93,"Computer Grades":81,"Evs Grades":90}]
total_marks=0

# Function to add student data by adding his/her name in student_data list.
def student_data_inp():
    n = int(input("Number of students: "))
    for i in range(1, n + 1):
        student_name = input(f"Student {i} Name: ").strip().upper()
        found = any(student_name == j.get("Name") for j in student_data)

        if found:
            print(f"{student_name}'s details are already entered in server.")
            continue

        # Input and validate each subject grade
        try:
            science_grade = int(input("Science Grade: "))
            maths_grade = int(input("Maths Grade: "))
            sst_grade = int(input("Sst Grade: "))
            evs_grade = int(input("Evs Grade: "))
            computer_grade = int(input("Computer Grade: "))

            grades = [science_grade, maths_grade, sst_grade, evs_grade, computer_grade]
            if not all(0 <= grade <= 100 for grade in grades):
                raise ValueError("Each subject mark must be between 0 and 100.")

            total = sum(grades)
            if total > 500:
                raise ValueError("Total marks cannot exceed 500.")

        except ValueError as e:
            print("Error:", e)
            print("Please re-enter all details for this student.")
            continue  # Skip this student and go to next

        student_data.append({
            "Name": student_name,
            "Science Grades": science_grade,
            "Maths Grades": maths_grade,
            "Evs Grades": evs_grade,
            "Sst Grades": sst_grade,
            "Computer Grades": computer_grade
        })

        print(f"{student_name} details entered successfully.")

# Function to search strudent from student data list if it exists then it returns the info else it returns no data of given student present.
def search_student():
    student_searched = input("Enter the Student Name: ").upper().strip()
    found = False
    for j in student_data:

        science_grade =j.get("Science Grades")
        maths_grade = j.get("Maths Grades")
        evs_grade=j.get("Evs Grades")
        sst_grade=j.get("Sst Grades")
        computer_grade=j.get("Computer Grades")
        total_marks= science_grade + maths_grade + evs_grade + sst_grade + computer_grade
        percent_mark=(total_marks/500)*100
        
        if j.get("Name").upper().strip() == student_searched:
            found = True
            if percent_mark>=95 and percent_mark<=100:
                print(j.get("Name")+f" >> Total marks: {total_marks}, Marks Percentage:{percent_mark}%, Grade:A")
            elif percent_mark>=90:
                print(j.get("Name")+f" >> Total marks: {total_marks}, Marks Percentage:{percent_mark}%, Grade:B")
            elif percent_mark>=70:
                print(j.get("Name")+f" >> Total marks: {total_marks}, Marks Percentage:{percent_mark}%, Grade:C")
            elif percent_mark>=60:
                print(j.get("Name")+f" >> Total marks: {total_marks}, Marks Percentage:{percent_mark}%, Grade:D")
            else:
                print(j.get("Name")+f" >> Total marks: {total_marks}, Marks Percentage:{percent_mark}%, Grade:Fail")
    if not found:
        print(f"{student_searched}'s details not available in our server.")

# Validation code of teachers/staff of school for accessing the data of students.
with open("C:\\Users\\nkofb\\OneDrive\\Desktop\\cii\\hello.py\\practice.txt","r") as f:

    list =  f.read().split("\n")
    list2 = []
    list3 = {}
    for i in range(len(list)):
        list2.append(list[i].split(" "))
    for i in range(len(list2)):
        username = [list2[i][0]]
        password = [list2[i][1]]
        list3[username[0].upper().strip()]=password[0]
    print(list3)

# Loop where all the real program runs by using all the above functions or validation code.
while True:
    user_inp = input("Type `login` to login or `exit` for Exitting from program ").strip().upper()
    if user_inp=="LOGIN":
         
        username_inp = input("Enter you name here: ").upper().strip()
        password_inp = input("Enter your password here: ")      
        found = False 
        if (username_inp in list3) and password_inp==list3.get(f"{username_inp}"):
            print(f"Welcome {username_inp}!")
            found = True
            while True:
                user_inp = input("Type `Search` to get results by entering name or Type `Enter` for data entry of students or Type `Exit` to exit from program.")
                if user_inp.upper().strip() == "SEARCH":
                    search_student()
                elif user_inp.upper().strip() == "ENTER":
                    student_data_inp()
                elif user_inp.upper().strip() == "EXIT":
                    print("Exitted from the program successfully.")
                    break
                else:
                    print("Invalid input. Select one of the given options.")
        if not found:
            print("Invalid credentials provided.") 
            continue
       
    elif user_inp=="EXIT":
        print("Exitted from program successfully.")
        break
    else:
        print("Invalid input passed.")
