''''
Project Description: Create a simple to-do list manager using Python. The program will allow users to add tasks, mark tasks as completed, list tasks, and remove tasks.

Requirements:

    Basic User Interface:
        Upon starting the program, display a welcome message and a list of available actions: 
        "1. Add Task", "2. Mark Task as Completed", "3. List Tasks", "4. Remove Task", and "5. Quit".
    Task List:
        Implement a way to store tasks. You can use a list or any other appropriate data structure.
    Add Task:
        When the user selects the "Add Task" option, prompt them to enter the task description.
        Add the task to the task list.
    Mark Task as Completed:
        Allow the user to mark a task as completed by entering its index in the task list.
        If the task is already marked as completed, display an appropriate message.
    List Tasks:
        Display a numbered list of tasks along with their completion status.
    Remove Task:
        Allow the user to remove a task by entering its index in the task list.
    Quit:
        When the user selects the "Quit" option, display a goodbye message and terminate the program.

Testing and Submission:

    Testing:
        Run the program and test all menu options to ensure they work correctly.
        Test edge cases (e.g., trying to mark or remove a task that doesn't exist).
    Documentation:
        Provide a brief README in your GitHub repository explaining how to run your program and its basic functionalities.
    Submission:
        Submit the link to your GitHub repository for grading8
'''
tasks = []
def add_tasks() -> list:
    task = input('Enter the task description: ')
    tasks.append(task)   
    return tasks

def mark_completed():
    return None
def get_tasks():
    return None
def remove_task():
    return None


def welcome():
    print(f'Please select an action\n "1. Add Task"\n "2. Mark Task as Completed"\n "3. List Tasks"\n "4. Remove Task"\n "5. Quit"\n')

def prompt():
    options = [1, 2, 3, 4, 5]
    while True:
        welcome()
        option = int(input("Please select an action: "))
        if option in options:
            match option:
                case 1: 
                    add_tasks()            
                case 2:
                    mark_completed()
                case 3:
                    list_tasks()
                case 4:
                    remove_tasks()
                case 5:
                    exit
        else:
            print("Invalid option")

def main():
    prompt()
if __name__ == "__main__":
    main()