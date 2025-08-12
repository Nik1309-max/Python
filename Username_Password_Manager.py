# User's App/Site name, Site Username and Site Password is been stored in dictionaries which are in a list.
user_pass = [
    {"App/Site name":"UMS","Username":"25113506","Password":"Nik130906"},
    {"App/Site name":"Hostel Wifi","Username":"125134","Password":"Nikhil@123"},
    {"App/Site name":"Laptop PIN","Username":"nkofbr@gmail.com","Password":"121206"}]

# App/sites names are stroed in this list to print it while user is entering any value.
app_names = ["UMS","Hostel Wifi","Laptop PIN"]

# This function helps in Adding/Extending user's username and password data.
def write_user_pass():
        app_name = input("Enter the app/site name: ")
        user_name = input("Enter the Username/Phone number/Email here: ")
        pass_word = input("Enter the password of Username/Phone number/Email here:")
        user_pass.append({"App/Site name":app_name,"Username":user_name,"Password":pass_word})
        app_names.append(app_name)

# This function helps in Searching user's username and password data using site/app name.
def search_app_pass():
    find_app = input(f"Choose the App/site from list {app_names} name to get its username and password: ").strip().upper()
    found = False
    for app in user_pass:
        res = app.get("App/Site name")
        if res==find_app:
            print(app)
            found = True
            break
    if not found:
        print("App/site's username and password not present in list maybe deleted or never entered, update it.")

# This function helps in Deleting/Removing user's username and password data using site/app name.
def delete_app_pass():
    delete_app = input(f"Which app details you want to delete?{app_names}:")
    found = False
    for app in user_pass:
        if app.get("App/Site name") == delete_app:
            user_pass.remove(app)
            found = True
            for app_namee in app_names:
                if app_namee == delete_app:
                    app_names.remove(app_namee)
            print(f"{delete_app} was deleted successfully")
    if not found:
        print(f"{delete_app} was not found. Enter a valid entry")

# This loop will provide input until user doesn't choose to Exit from this program
while True:
    inp = input("What do you want to?(Search/Write/Delete/Update/Exit) ").strip().upper()

    if inp=="SEARCH":
        search_app_pass() # Seaching app/site name and it's details.

    elif inp=="WRITE":
        write_user_pass() # Adding app/site name and it's details.

    elif inp=="DELELTE":
        delete_app_pass() # Removing app/site name and it's details.
    
    elif inp=="UPDATE":
        up_app_name = input(f"Enter the Site/App name from the list: {app_names} ")
        found = False
        for app in user_pass:
            if app.get("App/Site name")==up_app_name:
                new_password = input("Enter the new updated password: ").strip()
                app["Password"] = new_password
                found = True
                print("Password Updated Successfully.")
                inpp = input("Do you want to see your new updated details?(Yes or No):")
                if inpp=="Yes":
                    print(app)
                else:
                    continue
        if not found:
            print("Wrong Value entered")
    
    elif inp=="EXIT":
        print("You exited successfully") # It will exit user from program.
        break

    else:
        print("Invalid input. Select any of 4") # For invalid entry.

    