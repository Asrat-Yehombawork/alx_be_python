task = input("Enter your task: ").lower()
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is the task time-bound? (yes/no): ").lower()
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task} is a high priority task that requires immedate attention today!")
        else:
            print(f"Note: {task} is a high priority task but you can commplete it when you have a free time! ")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: {task} is a medium priority task that requires immedate attention today!")
        else:
            print(f"Note: {task} is a medium priority task but you can commplete it when you have a free time! ") 
    case "low":
        if time_bound == "yes":
            print(f"Reminder: {task} is a low priority task that requires immedate attention today!")
        else:
            print(f"Note: {task} is a low priority task but you can commplete it when you have a free time! ")
    case _:
        print("Wrong input!")        