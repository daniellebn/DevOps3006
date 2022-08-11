# A
x = 9
y = 4
if x < y:
    print("small")
else:
    print("BIG")

# B
for i in range(5):
    print(i)

# C
num = 3
if num == 1:
    print("summer")
elif num == 2:
    print("winter")
elif num == 3:
    print("fall")
elif num == 4:
    print("spring")

# D
    # 1. 10 times
    # 2. 10

# E
my_age = 29
first_latter = "D"
ILS_USD = 0.29
flew_abroad = True
apartment_num = 4

print(my_age)
print(first_latter)
print(ILS_USD)
print(flew_abroad)
print(apartment_num)
print(my_age + ILS_USD)

# F
phone_number = input("please enter your phone number ")
print("your phone number is " + phone_number)

# G


def printhello():
    print("Hello")


printhello()


def calculate():
    return 5+3.2


print(calculate())

# H


def my_name(name):
    print(name)


def my_number(r):
    print(r/2)


# I


def add_num(num1, num2):
    return num1 + num2


def add_str(str1, str2):
    return str1 + " " + str2


# K
# for i in range(5):
  #  for j in range(i+1):
   #     print("#", end="")
    # print(" ")


# L
i = 0
j = 6

for row in range(7):
    for colum in range(7):
        if row == i and colum == j:
            print("#", end="")
            j = j - 1
            i = i + 1
        elif row == colum:
            print("#", end="")
        else:
            print(end=" ")
    print()










