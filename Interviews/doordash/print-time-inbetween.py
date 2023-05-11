"""
Input - ("mon 10:00 am", mon 11:00 am)
Output - [11005, 11010, 11015...11100]
Output starts with 1 if the day is monday, 2 if tuesday and so on till 7 for sunday
Append 5 min interval times to that till the end time
So here it is 10:05 as first case, so its written as 11005
2nd is 10:10 so its written as 11010
...
...
Stop at 11100
"""
from datetime import datetime, timedelta

def add_five_minutes(start_timestamp, end_timestamp):
    # Parse the start and end timestamps
    start = datetime.strptime(start_timestamp, '%a %I:%M %p')
    end = datetime.strptime(end_timestamp, '%a %I:%M %p')
    
    # Add 5 minutes to the start timestamp until it reaches the end timestamp
    while start < end:
        print(start.strftime('%a %I:%M %p'))
        start += timedelta(minutes=5)
    print(end.strftime('%a %I:%M %p'))

add_five_minutes("mon 11:00 am", "mon 11:00 pm")