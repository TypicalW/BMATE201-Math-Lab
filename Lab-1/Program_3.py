#Program 3
#find the root of the Equation x^2-2x-1=0 by Using Newton-Raphson Method near x0=2.

from sympy import *
x=Symbol("x")
f=x**2-2*x-1

x0=2 # initial approximation
df=diff(f,x)
f=lambdify(x,f)
df=lambdify(x,df)
xn=x0-f(x0)/df(x0)
count=1
print(f"x{count} = %.5f"%xn)

while abs(xn-x0)>0.00001:
    x0=xn
    count += 1
    xn=x0-f(x0)/df(x0)
    print(f"x{count}=%.5f"%xn)
print(f"\nx{count}=x{count-1}, by correcting to 4 decimal places")
print("Hence the root of the equation is %.4f"%xn)

