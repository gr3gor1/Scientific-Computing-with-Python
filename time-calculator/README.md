Write a function named add_time that takes in two required parameters and one optional parameter:

  1. a start time in the 12-hour clock format (ending in AM or PM)

  2. a duration time that indicates the number of hours and minutes
     (optional) 

  3. a starting day of the week, case insensitive

The function should add the duration time to the start time and return the result. You can check the tests in test_module.py .

Some examples of expected outputs and use cases are provided below :

```
add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
```

Check the full description here : https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator

You can check the project on replit : https://replit.com/join/zalsoxhyuz-grigoriospapani
