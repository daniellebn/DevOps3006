import Fibonacci
Fibonacci.fib(100)

# הקטע קוד התחתון יביא רק את הפונקציה שאנחנו צריכים מתוך כל הקובץ ולא את כל הקובץ עצמו
from Fibonacci import fib as my_fib
from Fibonacci_aharon import fib as aharon_fib
from Fibonacci import a

aharon_fib(1000)
my_fib(1000)
print(a)


