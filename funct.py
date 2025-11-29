#assignment 1
def fact(num):
    """Return factorial of number."""
    if num == 1 :
        return 1
    else:
        return num * fact(num - 1)

f=int(input('enter the number you want factorial for :'))
a=fact(f)
print('factorial of',f,'is',a)


#assignment2

import math as mt
a=int(input('enter the number you want calculations of :'))

print('squareroot : ',mt.sqrt(a))
print('logarithm : ', mt.log(a))
print('sine: ', mt.sin(a))