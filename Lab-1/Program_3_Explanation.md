<H1>Step-by-Step Explanation</H1>
<H2>Program 3</H2>

<H3>1. Importing Required Libraries: </H3>
<code>from sympy import * </code>
<ul>This imports all functions and classes from the sympy library, which is used for symbolic mathematics in Python.
</ul>

<H3>2. Defining the Symbol and Function: </H3>
<code>x = Symbol("x")
f = x**2 - 2*x - 1
</code>
<ul>x = Symbol("x"): Defines x as a symbolic variable.</ul>
<ul>f = x**2 - 2*x - 1: Defines the function 𝑓(𝑥)=𝑥^2−2𝑥−1</ul>

<H3>3. Initial Approximation and Derivative:</H3>
<code>x0 = 2  # initial approximation
df = diff(f, x)
</code>
<ul>x0 = 2: Sets the initial guess for the root.</ul>
<ul>df = diff(f, x): Computes the derivative of the function 𝑓(𝑥) with respect to x.</ul>

<H3>4. Converting Symbolic Functions to Numeric Functions:</H3>
<code>f = lambdify(x, f)
df = lambdify(x, df)
</code>
<ul>f = lambdify(x, f): Converts the symbolic function f into a numeric function.</ul>
<ul>df = lambdify(x, df): Converts the symbolic derivative df into a numeric function.</ul>

<H3>5. First Iteration:</H3>
<code>xn = x0 - f(x0) / df(x0)
count = 1
print(f"x{count} = %.5f" % xn)
</code>
<ul>xn = x0 - f(x0) / df(x0): Applies the Newton-Raphson formula to compute the next approximation.</ul>
<ul>count = 1: Initializes the iteration counter.</ul>
<ul>print(f"x{count} = %.5f" % xn): Prints the result of the first iteration.</ul>

<H3>6. Iterative Process:</H3>
<code>while abs(xn - x0) > 0.00001:
    x0 = xn
    count += 1
    xn = x0 - f(x0) / df(x0)
    print(f"x{count} = %.5f" % xn)
</code>
<ul>while abs(xn - x0) > 0.00001: Continues iterating until the difference between successive approximations is less than the specified tolerance (0.00001).</ul>
<ul>x0 = xn: Updates the previous approximation to the current one.</ul>
<ul>count += 1: Increments the iteration counter.</ul>
<ul>xn = x0 - f(x0) / df(x0): Computes the next approximation.</ul>
<ul>print(f"x{count} = %.5f" % xn): Prints the result of each iteration.</ul>

<H3>7. Final Output:</H3>
<code>print(f"\nx{count} = x{count - 1}, by correcting to 4 decimal places")
print("Hence the root of the equation is %.4f" % xn)
</code>
<ul>print(f"\nx{count} = x{count - 1}, by correcting to 4 decimal places"): Indicates that the iterations have converged, and the final approximation is displayed.</ul>
<ul>print("Hence the root of the equation is %.4f" % xn): Prints the root of the equation to four decimal places</ul>





