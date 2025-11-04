"""
This script runs the makelist() function
such that it recieves input from the user

"""

from typing import Optional
from logger.logging import default_logger


def makelist(listo: list[str]) -> int:
    """
    Asks the user if they want to add items to
    their list via input()

    Args:
        listo - List of strings

    Returns:
        int - last option selected

    """

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")
    print("=" * 50)
    x: int = int(input("Enter your choice: "))
    if x == 1:
        tsk: str = input("Enter task: ")
        listo.append(tsk)
        print("-" * 50)
    elif x == 2:
        print("Tasks:")
        for i, t in enumerate(listo):
            print(f"{i+1}. {t}")
        print("-" * 50)
    elif x == 3:
        usr_input = input("Enter task number to mark as done: ")
        if 0 <= int(usr_input) - 1 < len(listo):
            listo.pop(int(usr_input) - 1)
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    elif x == 4:
        print("Exiting.")
        print("-" * 50)
    else:
        print("Invalid choice.")
        print("-" * 50)
    return x


if __name__ == "__main__":

    logger = default_logger(level='WARNING', filename='.\\logger\\main_output.log')

    logger.debug("This is a debug message")
    logger.info("This is a info message") 
    logger.warning("This is a warning message") 
    logger.error("This is a error message") 
    logger.critical("This is a critical message") 

    input_list: Optional[list[str]] = list(
        item.strip() for item in input("Press Enter to Start (Optional: input your comma separated list)").split(",") if item.strip() != ""
    )

    while makelist(input_list) != 4:
        pass
