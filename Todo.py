# =================Todo list ====================
task_db = []
task_id_container = 1
def add_new_task(task_name):
    #  Add a new task to the list.
    # Each task is stored as a dictionary.
    global task_id_container
    new_task = {
    "id": task_id_container,
    "task": task_name
}
    task_db.append(new_task)
    task_id_container +=1
    return new_task
def get_all_tasks():
    # return al stored tasks
    return task_db

def display_menu():
    # =========Display the main menu
    print("\n" + "=" *35)
    print("              DECODELABS TODO LIST")
    print("=" *35)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")
    print("=" *35)


def handle_add_task():
    # Get task from user and save it
    task_name = input("\n Enter Task: ").strip()
    if task_name:
        task = add_new_task(task_name)
        print("✅Task Added successfully")
        print(f"ID: {task['id']}")
        print(f"task: {task['task']}")
    else:
        print("\n❌ Task cannot be empty.")


def handle_view_tasks():
    # View Tasks to the user
    tasks = get_all_tasks()
    if not tasks:
        print("\nNo tasks available.")
        return
    print("\n=====================Tasks List============")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. [ID: {task['id']}] {task['task']}")
        print("=" *35)



def main():
    # Main Application lOOp=============
    while True:
        display_menu()
        choice = input("Enter your choice(1-3): ")
        if choice == "1":
            handle_add_task()
        elif choice =="2":
            handle_view_tasks()
        elif choice == "3":
            print("\nThank you for using DecodeLabs To-Do List.")
            break
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")


if __name__=="__main__":
    main()