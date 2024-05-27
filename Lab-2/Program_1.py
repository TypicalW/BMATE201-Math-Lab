''' Program to find the interpolating polynomial and y(4) using the data mentioned in the .pdf file'''


#Newton forward difference formula

from sympy import *
from numpy import *
n=int(input( 'Enter the number of data points: '))
x=zeros(n)
y=zeros((n,n))
f=[]

for i in range(0,n):
    x[i]=float(input(f'x{i}='))
    y[0][i]=float(input(f'y{i}='))

for j in range(0,n-1):
    for i in range(0,n-1-j):
        y[j+1][i]=y[j][i+1]-y[j][i]

for i in range(0,n):
    print(x[i], end=' ')
    for j in range(0,n-i):
        print("\t \t ",y[j][i], end = " ")
    print()

h=x[1]-x[0]
t=Symbol('t')
p=(t-x[0])/h
pterms = 1
for k in range (0,n-1):
    pterms=((p-k)/(k+1))*pterms
    f.append(pterms)
rhs=y[0][0]

for i in range (1,n):
    rhs=(rhs+f[j-1]*y[j][0])

print('The interpolating polynomial is: ')
display(simplify(rhs))
xi-float(input('Enter value of x at which y should be determined: '))
print(f'y({xi}) = %0.4f' % rhs.subs(t,xi))