'''
    This script runs the makelist() function
    such that it recieves input from the user

'''


from typing import Optional



def makelist(listo: Optional[list[str]]=None) -> int:
    '''
    Asks the user if they want to add items to 
    their list via input()

    Args:
        listo - List of strings (Optional)
    
    Returns:
        int - last option selected

    '''

    listo = listo or []
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")
    print("="*50)
    x : int = int(input("Enter your choice: "))
    if x == 1:
        tsk : str = input("Enter task: ")
        listo.append(tsk)
        print("-"*50)
    elif x == 2:
        print("Tasks:")
        for i, t in enumerate(listo):
            print(f"{i+1}. {t}")
        print("-"*50)
    elif x == 3:
        usr_input = input("Enter task number to mark as done: ")
        if 0 <=  int(usr_input) - 1 < len(listo): 
            listo.pop(int(usr_input) - 1)
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    elif x == 4:
        print("Exiting.")
        print("-"*50)
    else:
        print("Invalid choice.")
        print("-"*50)
    return x

if __name__ == "__main__":
    input_list: Optional[list[str]] = list(input('Press Enter to Start (Optional: input your list)'))

    while makelist(input_list) != 4:
        pass

