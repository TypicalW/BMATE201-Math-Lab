<H1>Step-by-Step Explanation</H1>
<H2>Program 1</H2>
<H3> 1. Imports and Function Definition: </H3>
<code>import sys
    f = lambda x: x**2 - 2*x - 1
    error_tolerance = 0.0001
    max_iterations = 50
    a = 2
    b = 3
</code>
<ul>f = lambda x: x**2 - 2*x - 1: Defines a lambda function f that represents the equation 𝑓(𝑥)=𝑥^2−2𝑥−1</ul>
<ul>error_tolerance = 0.0001: Sets the acceptable error tolerance for the root approximation.</ul>
<ul>max_iterations = 50: Sets the maximum number of iterations for the root-finding process.</ul>
<ul>a = 2 and b = 3: Set the initial lower and upper bounds of the range within which the root is expected to lie.</ul>

<H3>2. Checking if Root Lies in the Given Range: </H3>
<code>if f(a)*f(b) > 0:
    sys.exit("The root does not lie in the given range")
    print("f(%0.5f)=%0.5f and f(%0.5f)=%0.5f"%(a,f(a),b,f(b)))
    print("The root lies between %0.5f and %0.5f"%(a,b))
</code>
<ul>This section checks if the function values at points a and b have the same sign (f(a) * f(b) > 0). If they do, it implies that there is no root in the interval [a, b], so the program exits with a message.</ul>
<ul>Note: The print statements after sys.exit will not execute because sys.exit terminates the program.</ul>

<H3>3. Finding the Root Using Regula-Falsi Method: </H3>
<code>for i in range(max_iterations):
    x = (a*f(b) - b*f(a)) / (f(b) - f(a))
    print(f"The approximate root obtained in iteration {i+1} is %0.5f"%x)
    print("\nf(%0.5f)=%0.5f"%(x,f(x)))
</code>
<ul>This loop runs for a maximum of max_iterations times.</ul>
<ul>x = (a*f(b) - b*f(a)) / (f(b) - f(a)): This is the Regula-Falsi formula to compute the next approximation of the root.</ul>
<ul>print(f"The approximate root obtained in iteration {i+1} is %0.5f"%x): Prints the approximate root found in the current iteration..</ul>
<ul>print("\nf(%0.5f)=%0.5f"%(x,f(x))): Prints the value of the function at the approximate root.</ul>

<H3>4. Checking for Convergence: </H3>
<code>if abs(f(x)) < error_tolerance:
    print("\nThe root of the equation is: %.4f"%x)
    break
</code>
<ul>if abs(f(x)) < error_tolerance: Checks if the absolute value of the function at x is less than the specified error tolerance.</ul>
<ul>print("\nThe root of the equation is: %.4f"%x): If the condition is met, it prints the root of the equation.</ul>
<ul>break: Exits the loop if the root is found within the desired tolerance.</ul>

<H3>5. Updating the Interval: </H3>
<code>if f(x) < 0:
    a = x
else:
    b = x
print("The root lies between %0.5f and %0.5f"%(a,b))
</code>
<ul>Depending on the sign of f(x), updates either a or b to x, narrowing the interval where the root is believed to be.</ul>
<ul>print("The root lies between %0.5f and %0.5f"%(a,b)): Prints the new interval for the next iteration.</ul>


