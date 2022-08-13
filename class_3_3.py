
def save_names(name_file):
    my_file = open(name_file, "a")
    current_name = input("enter your name: ")
    my_file.write(current_name + "\n")
    my_file.close()


def show_name(name_file):
    my_file = open(name_file, "r")
    for name in my_file.readlines():
        print(name, end='')
    my_file.close()


for i in range(5):
show_name("names.txt")