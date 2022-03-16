import sys
import helper

def time(hr, min, sec):
    helper.convertHr(hr)
    print('The time is ', hr, ' ', min, ' ', sec)


time(10,20,20)
time(20,30,40)
time(10,22,22)
time(100,200,300)
time(-1,-1,-1)