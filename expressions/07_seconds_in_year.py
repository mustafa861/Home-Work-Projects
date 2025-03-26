# Use Python to calculate the number of seconds in a year, 
# and tell the user what the result is in a nice print statement that looks like this
#  (of course the value 5 should be the calculated number instead):

# There are 5 seconds in a year!

# You should use constants for this exercise -- there are 365 days in a year, 24 hours in a day,
#  60 minutes in an hour, and 60 seconds per minute.



days_in_year:int=365
hours_in_day:int=24
minutes_in_hour:int=60
seconds_in_minute:int=60

total_hours_in_year=(days_in_year*hours_in_day)
print(f"Hours in a year :{total_hours_in_year}")
total_minutes_in_year=(total_hours_in_year*minutes_in_hour)
print(f"Minutes in a year :{total_minutes_in_year}")
total_seconds_in_year=(total_minutes_in_year*seconds_in_minute)
print(f"Seconds in a year :{total_seconds_in_year}")

