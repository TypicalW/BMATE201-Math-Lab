import sys 
from sympy import *
var("x")
f=1/(1+x**2)
x0=float(input("Enter the lower limit "))
xn=float(input("Enter the upper limit "))
n=int(input("Enter number of sub intervals "))
if n%2!=0:
    sys.exit("The value of x should be divisble by 2")
print("Value of integration  by regular method is %.3f"%integrate(f,(x,x0,xn)))
f=lambdify(x,f)
h=(xn-x0)/n
sum=0
for i in range(0,n+1):
    xi=x0+i*h
    print(f"x{i}=%.2f\t\tf(%.2f)=%.2f"%(xi,xi,f(xi)))
    if i==0 or i==n:
        sum=sum+f(xi)
    elif i%2==0:
        sum=sum+2*f(xi)
    else:
        sum=sum+4*f(xi)
print("Value of the integral by Simpson's (1/3)rd Rule is %0.3f" % (sum*h/3))