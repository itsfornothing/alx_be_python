task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

reminder = ""
match priority:
    case "high":
        reminder = f"The task '{task}' is of HIGH priority."

    case "medium":
        reminder = f"The task '{task}' is of MEDIUM priority."

    case "low":
        reminder = f"The task '{task}' is of LOW priority."

    case _:
        reminder = f"The task '{task}' has an UNKNOWN priority."

if time_bound == "yes":
    reminder += " It requires immediate attention today!"
    print(f"\nREMINDER: {reminder}")

else:
    reminder += " Consider completing it when you have free time."
    print(f"\nNote: {reminder}")
