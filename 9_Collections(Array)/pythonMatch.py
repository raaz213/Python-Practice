#The match statement allows you to match a variable against different patterns and execute code based on the matched case. Instead of writing many if..else statements, you can use the match statement.

day = int(input('Enter a day of the week (1-7): '))
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
  case _:
    print("Invalid day")
    
#Combine Values
#Use the pipe character | as an or operator in the case evaluation to check for more than one value match in one case:

day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")
  
# If Statements as Guards
# You can add if statements in the case evaluation as an extra condition-check:

# The if statement is called a guard. If the guard is true, the case is matched.
# If the guard is false, the case is skipped.

month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")