def save_note():
    try:
        note=input("Enter your note:")
        with open("notes.txt","a") as file:
            file.write(note+"\n")
            print("note saved succesfully!")
    except Exception as e:
        print("Error:",e)
def view_notes():
    try:
        with open("notes.txt","r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No notes")
while True:
        print("\n1.Save note")
        print("2.view Notes")
        print("3.Exit")
        choice=input("Enter your choice:")
        if choice=="1":
            save_note()
        elif choice=="2":
            view_notes()
        elif choice=="3":
            print("Thank you!")
            break
        else:
            print("Invali choice")
