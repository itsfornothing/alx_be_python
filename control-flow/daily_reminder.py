task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"{task} is a high priority task that requires immediate attention today!")
            
        elif time_bound == "no":
            print(f"{task} is a high priority task. Consider completing it when you finish high priority tasks.")
        else:
            print("Invalid time_bound input!")

    case "medium":
        if time_bound == "yes":
            print(f"{task} is a medium priority task that requires attention today!")
            
        elif time_bound == "no":
            print(f"{task} is a medium priority task. Consider completing it when you finish high priority tasks.")

        else:
            print("Invalid time_bound input!")


    case "low":
        if time_bound == "yes":
            print(f"{task} is a low priority task but that requires attention today!")

        elif time_bound == "no":
            print(f"{task} is a low priority task. Consider completing it when you have free time.")

        else:
            print("Invalid time_bound input!")

    case _:
        print("Invalid priority input!")
