from datetime import datetime, timedelta

def get_start_end_of_month(year, month):
    # Calculate the first day of the month
    start_date = datetime(year, month, 1).date()

    # Calculate the last day of the month
    if month == 12:
        end_date = (datetime(year + 1, 1, 1) - timedelta(days = 1)).date()
    else:
        end_date = (datetime(year, month + 1, 1) - timedelta(days = 1)).date()

    # start_date = str(start_date).split("-")[2]
    # end_date = str(end_date).split("-")[2]

    return start_date, end_date

# Example usage:
# start_day, end_day = get_start_end_of_month(2024, 12)
# print(f"Start day: {start_day}")
# print(f"End day: {end_day}")