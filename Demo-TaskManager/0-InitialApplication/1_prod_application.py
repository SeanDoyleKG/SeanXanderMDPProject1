listo = []

while True:
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")
    print("="*50)
    x = input("Enter your choice: ")
    if x == '1':
        tsk = input("Enter task: ")
        listo.append(tsk)
        print("-"*50)
    elif x == '2':
        print("Tasks:")
        for i, t in enumerate(listo):
            print(f"{i+1}. {t}")
        print("-"*50)
    elif x == '3':
        usr_input = input("Enter task number to mark as done: ")
        if 0 <=  int(usr_input) - 1 < len(listo): 
            listo.pop(int(usr_input) - 1)
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    elif x == '4':
        print("Exiting.")
        print("-"*50)
        break
    else:
        print("Invalid choice.")
        print("-"*50)