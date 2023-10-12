# Leap Year 

"""
Year % 4 == 0&
Year % 100! =0
Year % 400 == 0

"""
def isLeapYear(Year):
  if (Year % 4 == 0 and Year % 100
      != 0) or Year %  400 == 0:
    return True
  else:
    return False


Year = int(input("Enter a Year:"))

if isLeapYear(Year):
  print('{} is Leap Year.'.format(Year))
else:
  print('{} is not a Leap Year.'.format(Year))
  