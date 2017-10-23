month = raw_input("What is the month of your birth?")
numbers = ["1","2","3","4","5","6","7","8","9","10","11","12"]
months = ["MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER", "JANUARY",
          "FEBRUARY"]
months_ABBR = ["MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC", "JAN", "FEB"]
if month in numbers:
    month = int(numbers.index(month) + 1)
if type(month) == int:
    A = (month + 9) % 12 + 1
if type(month) == str:
    month = month.upper()
    if month in months:
        if month not in months:
            exit(404)
        else:
            A = months.index(month) + 1
    else:
        if month not in months_ABBR:
            exit(404)
        else:
            A = months_ABBR.index(month) + 1
B = input("What was day of your birth?")
C = input("What year were you born?")
if A == "January" or A == "january" or A == "Jan" or A == "jan":
    C = C - 1
elif A == "January" or A == "january" or A == "Jan" or A == "jan":
    C = C - 1
if C > 99:
    D = C / 100
    C = C % 100
W = (13 * A - 1) / 5
X = C / 4
Y = D / 4
Z = W + X + Y + B + C - 2 * D
R = Z % 7
if R == 0:
    Day = "Sunday"
if R == 1:
    Day = "Monday"
if R == 2:
    Day = "Tuesday"
if R == 3:
    Day = "Wednesday"
if R == 4:
    Day = "Thursday"
if R == 5:
    Day = "Friday"
if R == 6:
    Day = "Saturday"
# Run some test cases- try today's date, your birth date, and whatever else interests you!
print Day
