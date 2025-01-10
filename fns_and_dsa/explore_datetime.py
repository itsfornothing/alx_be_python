from datetime import timedelta, datetime


def display_current_datetime():
    current_date = datetime.now()
    print(current_date)


def calculate_future_date(days):
    date = datetime.today()
    future_date = date + timedelta(days=days)
    future_date = future_date.strftime("%Y-%m-%d")
    print(datetime.strptime(future_date,future_date))


if __name__ == "__main__":
    display_current_datetime()
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(number_of_days)
