from datetime import timedelta, datetime


def display_current_datetime():
    current_date = datetime.now()
    print("Current Date and Time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))


def calculate_future_date(days):
    date = datetime.today()
    future_date = date + timedelta(days=days)
    # Format the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    # Convert the formatted string back to a datetime object
    future_date_obj = datetime.strptime(formatted_future_date, "%Y-%m-%d")
    print("Future Date Object:", future_date_obj)


if __name__ == "__main__":
    display_current_datetime()
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(number_of_days)
