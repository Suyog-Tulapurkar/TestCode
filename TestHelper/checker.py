import sys
import helper

def loop(n):
    for i in range(n):
        print("The Value is: ", i*2)
    print (helper.foo('complete'))

loop(2)
loop(4)
loop(8)