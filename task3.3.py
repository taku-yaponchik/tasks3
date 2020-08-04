print('Enter the number of students for each class:')
A=int(input('A: '))
B=int(input('B: '))
C=int(input('C: '))
from math import ceil
a=ceil(A/2)
b=ceil(B/2)
c=ceil(C/2)
sum=a+b+c
print(a,b,c)
print('need to purchase',sum,"school desks.")
