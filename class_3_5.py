import requests
print("moshe")
try:
    f = int(input("enter number: "))
    r = 5 / 5
except ZeroDivisionError:
    print("could not divide by zero")
except ValueError:
    print("enter a legal number")
except BaseException as e:
    print("something went wrong")
    print(e.args)
print("haim")
