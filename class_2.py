# class 2 07/07/2022

"""
isTrue = False
a = 2
b = 2.5
strOne = "One"
strThree = "Three"
c = 5
my_list = [1, 2, 3, 4, 5]
my_empty_list = []

if 2 in my_list:
    print("hey")
else:
    print("no")

if a < b and not strOne != strThree:
    print("a is smaller than b")
elif b > a:
    print("b is greater than a")
else:
    print("yo")
    """
other_list = []
names = ["chanan", "tom", "zack", "aharon"]
search_name = "ariel"
if search_name in names:
    print(f"we found", {search_name})

if other_list:

k = 5
f = 5
t = [1, 2, 3]
e = [1, 2, 3]
print(k == e)
print()

if c == 1:
    print("c is one")
elif c == 2:
    print("c is two")
else:
    print("c is greater than two")

x = 5
y = 5
if x == y:
    print("y")
if x is y:
    print("y")

if type(x) is int:
    print("x is a number")

print(len(my_list))

if len(my_list) > 3:
    print("we have enough elements")
if my_empty_list:  # if the list is empty we will get false if it's not empty we will get true
    print("hey")


# Loops

my_str = "hello world"
primes = [1, 2, 3, 5, 7, 11]
a = 0


for prime in primes:  # פה נשתמש בלולאה שהיא יחיד מול רבים לדוגמא for employee in employees נקראת גם for each
    print(prime)

for i in range(len(primes)):
    print(primes[i])


a = 0
while a < 10:
    print(my_str)
    a += 1
else:
    print("---DONE---")


for i in range(10):
    print(i)


while a < 10:
    a = a + 1
    print(a)

  """



