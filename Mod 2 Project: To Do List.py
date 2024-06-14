# App Initialization
# need to work out how the date gets verified...

task_list = []


def add_task():
    #task shown as [importance, name, due date]
    task = []
    
    #add importance
    while True:
        try:
            importance = int(input("On a scale of 1-5 (1 is very important and 5 is not very important) how important is this task? "))
            if importance < 1 or importance > 5:
                raise ValueError
        except ValueError:
            print("That is not a valid importance level.  Please try again.")
            continue
        else:
            task.append(importance)
            break

    #add name
    while True:
        try:
            name = input("What is the name of this task?")
        except Exception as e:
            print("Error: {e} Please select a different name.")
            continue
        else:
            task.append(name)
            break

    #add date
    while True:
        try:
            date = input("What is the due date for this task? (mm/dd/yyyy) ")
            if len(date) != 10:
                raise ValueError
            if date[2] != "/" or date[5] != "/":
                raise ValueError
            
            split_date = date.split("/")
            if int(split_date[0]) > 12:
                raise ValueError
            if int(split_date[1]) > 31:
                raise ValueError
            if int(split_date[2]) < 2024 or int(split_date[2]) > 3000 :
                raise ValueError

        except ValueError:
            print(date)
            print("This is not a valid date or date format.  Please try again.")
            continue
        else:
            task.append(date)
            break

    task.append("incomplete")
    task_list.append(task)
    print(f"Task {task[1]} added successfully")


def view_tasks():
    print(f"\nYou currently have {len(task_list)} tasks.\nHow would you like to view your tasks?: ")

    task_view_input = input("1. View All Tasks \n2. View Incomplete Tasks \n3. View Completed Tasks \n4. View Todays Tasks \n ")
    while True:

        if task_view_input == "1":
            task_number = 0
            for task in task_list:
                task_number += 1
                print("------------------------------------------------------------------")
                print(f"{task_number}. \n   Importance: {task[0]} \n   Name: {task[1]} \n   Due Date: {task[2]}\n   {task[3]}")
            if task_number == 0:
                print("You don't have any tasks currently.")
            else:
                print("------------------------------------------------------------------")
            break

        elif task_view_input == "2":
            task_number = 0
            for task in task_list:
                if task[3] == "incomplete":
                    task_number += 1
                    print("------------------------------------------------------------------")
                    print(f"{task_number}. \n   Importance: {task[0]} \n   Name: {task[1]} \n   Due Date: {task[2]}\n   {task[3]}")
            if task_number == 0:
                print("You don't have any incomplete tasks currently.")
            else:
                print("------------------------------------------------------------------")
            break

        elif task_view_input == "3":
            task_number = 0
            for task in task_list:
                if task[3] != "incomplete":
                    task_number += 1
                    print("------------------------------------------------------------------")
                    print(f"{task_number}. \n   Importance: {task[0]} \n   Name: {task[1]} \n   Due Date: {task[2]}\n   {task[3]}")
            if task_number == 0:
                print("You don't have any completed tasks currently.")
            else:
                print("------------------------------------------------------------------")
            break

        elif task_view_input == "4":
            task_number = 0
            today = input("What is today's date (mm/dd/yyyy)? ")
            for task in task_list:
                if task[2] == today:
                    task_number += 1
                    print("------------------------------------------------------------------")
                    print(f"Today's tasks are:\n{task_number}. \n   Importance: {task[0]} \n   Name: {task[1]} \n   Due Date: {task[2]}\n   {task[3]}")
            if task_number == 0:
                print("You don't have any tasks due today.")
            else:
                print("------------------------------------------------------------------")
            break

        else:
            print("That is not a valid View Method,  Please try again.")



def mark_complete():
    print("Here are your uncompleted tasks:")
    for task in task_list:
        if task[3] != "complete":
            print(task[1])
    complete_input = input("What is the name of the task that you would like to mark as complete?").lower()
    for task in task_list:
        if complete_input == task[1]:
            task[3] = "complete"
            print(f"{task[1]} successfully marked complete!")
    

def delete_task():
    print("Here are your tasks:")
    for task in task_list:
        print(task[1])

    delete_input = input("What is the name of the task that you would like to delete? ").lower()
    for task in task_list:
        if delete_input == task[1]:
            print(f"Task ({task[1]}) removed successfully")
            task_list.remove(task)



print("Welcome to the To-Do List App!")

while True:

    operation = input("Main Menu: \n1. Add a Task\n2. View Tasks\n3. Mark a Task as Complete\n4. Delete a Task\n5. Quit\nPlease select a function:")

    if operation == "1":
        add_task()
    elif operation == "2":
        view_tasks()
    elif operation == "3":
        mark_complete()
    elif operation == "4":
        delete_task()
    elif operation == "5":
        break
    else:
        print("That is not a currently supported function.  Please select 1-5.")

print("Thank you for using the To-Do List App!  Have a productive day!")