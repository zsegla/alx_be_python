import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    days = input("Enter the number of days to add to the current date: ")
    future_date = datetime.datetime.now() + datetime.timedelta(days=int(days))
    print("Future date:", future_date.strftime("%Y-%m-%d "))

display_current_datetime()
calculate_future_date()