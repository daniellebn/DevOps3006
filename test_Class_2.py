
my_str = "hello world"
a = 0
while a < 5:
    print(my_str)
    a += 1

names = ["chanan", "tom", "zack", "aharon"]

for i in range(len(names)): #
    print(names[i])

for name in names:
    if name == "zack":
        break
    print(name)
