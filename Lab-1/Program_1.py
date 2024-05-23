#Regula-Falsi Method

'''Program 1: Program to find the root of the Equation x^2-2x-1=0, Which lies (2,3), Using Regula Falsi Method'''
import sys 
f= lambda x: x**2 - 2*x - 1                    #Question-Equation
error_tolerance = 0.0001
max_iterations = 50
a = 2                                          #lower limit of range in question
b = 3                                          #upper limit of range in question

#Case for when Root isnt in Range, Displays given Data
if f(a)*f(b)>0:
    sys.exit("The root does not lie in the given range")
    print("f(%0.5f)=%0.5f and f(%0.5f)=%0.5f"%(a,f(a),b,f(b)))
    print("The root lies between %0.5f and %0.5f"%(a,b))

#Finding the root by Regula-Falsi Iterative method
for i in range(max_iterations):
    x=(a*f(b)-b*f(a))/(f(b)-f(a))              #Regula-Falsi Formula
    print(f"The approximate root obtained in itreation {i+1} is %0.5f"%x)  
    print("\nf(%0.5f)=%0.5f"%(x,f(x)))
    
    if abs(f(x))< error_tolerance:              #displays final answer
        print("\nThe root of the equation is: %.4f"%x)
        break
   
    if f(x)<0:
        a=x
    else:
        b=x
    print("The root lies between %0.5f and %0.5f"%(a,b))
