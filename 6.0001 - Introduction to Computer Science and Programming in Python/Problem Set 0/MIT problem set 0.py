import numpy
import sys


def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

def get_number(label):
    
    value = input("Enter number " + label + ": ")
    while not is_number(value):
        value = input("Previous entry was not a number. Enter 'q' to quit or enter number " + label + ": ")
        if value=='q':
            sys.exit()
    return float(value)        

if __name__ == '__main__':
    
    x = get_number('x')
    y = get_number('y')
    print("x**y is", x**y)
    print("log (base two) of x is", numpy.log2(x))



    