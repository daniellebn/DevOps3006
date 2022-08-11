from class_3_arit import addition, sub
from class_3_get_data import get_number
import datetime
def dec():
    print(datetime.datetime.now())
    addition()

a = get_number()
b = get_number()
c = addition(a, b)
d = sub(c, a)

print(c)
print(d)
