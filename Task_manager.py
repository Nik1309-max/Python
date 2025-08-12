def add_task():
    global task_id
    task_id+=1
    user_inp2 = input(f"Task {task_id}: ")
    tasks.append({"Id":task_id ,"Task": user_inp2, "Status": "Incomplete"})
    
def delete_task():
    print(tasks)
    user_inp3 = int(input(f"Enter the id of task to delete it: "))
    if len(tasks)>=user_inp3:
        tasks[user_inp3-1] = ""
    else:
        print("--- Index out of range ---")

def change_status_complete():
    print(tasks)
    user_inp2 = int(input("Choose the id of task to mark it complete: "))
    if len(tasks)>=user_inp2:
        tasks[user_inp2-1]["Status"] = "Completed"
        print(tasks)
    else:
        print("--- Index out of range ---")
    
def show_tasks():
    for i in range(len(tasks)):
        print(f"{tasks[i]["Id"]} | {tasks[i]["Task"]} | {tasks[i]["Status"]}")
    if len(tasks) == 0:
        print("--- No data present ---")

def remove_all_tasks():
    global task_id
    task_id = 0
    tasks.clear()
    print("--- All data removed ---")
    

tasks = []
task_id = 0

print("What to do today?")
while True:
    user_inp = input("Add task/ Delete task/clear/completed tasks/Show task/Exit ").strip().lower()
    if user_inp == "add":
        user_inp2 = int(input("Enter the number of tasks to add: "))
        count = 0
        while user_inp2 != count:
            add_task()
            count+=1
    elif user_inp == "delete":
        pass
    elif user_inp == "exit":
        print("==== Exitted from the program ===")
        break
    elif user_inp == "com":
        change_status_complete()
    elif user_inp == "clear":
        remove_all_tasks()
    elif user_inp == "show":
        show_tasks()
    else:
        print("--- Invalid input ---")

