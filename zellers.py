print "This program will allow you to find the week day of any date you want!"
month = raw_input("Choose a month: ")
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
months = ["MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER", "JANUARY",
          "FEBRUARY"]
months_ABBR = ["MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC", "JAN", "FEB"]
if month in numbers:
    month = int(numbers.index(month) + 1)
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
B = input("Choose a day: ")
C = input("Choose a Year: ")
if A == 11 or A == 12:
    C = C - 1
if C > 99:
    D = C / 100
    C = C % 100
W = (13 * A - 1) / 5
X = C / 4
Y = D / 4
Z = W + X + Y + B + C - 2 * D
R = Z % 7
Wdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print Wdays[R]