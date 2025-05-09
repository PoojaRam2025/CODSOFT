todo_list = []

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        if len(todo_list) == 0:
            print("No tasks yet!")
        else:
            print("Your Tasks:")
            for i in range(len(todo_list)):
                print(str(i+1) + ". " + todo_list[i])

    elif choice == '2':
        task = input("Enter a new task: ")
        todo_list.append(task)
        print("Task added!")

    elif choice == '3':
        if len(todo_list) == 0:
            print("No tasks to remove.")
        else:
            for i in range(len(todo_list)):
                print(str(i+1) + ". " + todo_list[i])
            num = int(input("Enter task number to remove: "))
            if num > 0 and num <= len(todo_list):
                removed = todo_list.pop(num - 1)
                print("Removed:", removed)
            else:
                print("Invalid number.")

    elif choice == '4':
        break
    else:
        print("Invalid choice!")
