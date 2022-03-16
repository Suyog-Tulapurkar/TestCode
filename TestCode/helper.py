import sys
import main

def check(a,b):

    print (a, ' + ', b, ' = ' ,main.add(a,b))
    print(a, ' - ', b, ' = ' ,main.subtract(a,b))
    print(a, ' * ', b, ' = ' ,main.multiply(a,b))
    print(a, ' / ', b, ' = ' ,main.divide(a,b))

check(20,10)
check(-20, -10)
check(-20.0, 10.0)
check(10.0,0)
check(10.0,-20.0)
