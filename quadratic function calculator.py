#quadratic function calculator
import math
from fractions import *

a=float(input('a= '))
b=float(input('b= '))
c=float(input('c= '))

user=input('If you want to get the answer in fraction, type yes, otherwise press any key'+'\n')
if user=='yes':
    fraction=True
else:
    fraction=False

while a==0:
    print('Not even a quadratic function, reteach your math please.')
    a=float(input('a= '))
    
if b**2-4*a*c>0:
    x1=(-b+math.sqrt(b**2-4*a*c))/2*a
    x2=(-b-math.sqrt(b**2-4*a*c))/2*a
    if fraction:
        a=Fraction(x1)
        b=Fraction(x2)
        print('x1=',a)
        print('x1=',b)
    else:
        print('x1=',x1)
        print('x2=',x2)
elif b**2-4*a*c==0:
    x=(-b+math.sqrt(b**2-4*a*c))/2*a
    if fraction:
        a=Fraction(x)
        print('x1=x2=',a)
    else:
        print('x1=x2=',x)
    
else:
    print('no scolution')
