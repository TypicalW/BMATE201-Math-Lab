from sympy import *
from numpy import *

# Input the number of data points
n = int(input('Enter the number of data points: '))
x = zeros(n)
y = zeros((n, n))

# Input the x and y values
for i in range(n):
    x[i] = float(input(f'x{i} = '))
    y[i][0] = float(input(f'y{i} = '))

# Calculate the backward differences
for j in range(1, n):
    for i in range(n-1, j-1, -1):
        y[i][j] = y[i][j-1] - y[i-1][j-1]

# Display the backward difference table
print("\nBackward Difference Table:")
for i in range(n):
    print(f'{x[i]:.4f}', end='')
    for j in range(i+1):
        print(f'\t{y[i][j]:.4f}', end='')
    print()

# Newton's backward difference formula
h = x[1] - x[0]
t = Symbol('t')
p = (t - x[n-1]) / h
pterms = 1
f = []

# Compute the interpolating polynomial terms
for k in range(n-1):
    pterms = pterms * (p + k) / (k + 1)
    f.append(pterms)

rhs = y[n-1][0]
for j in range(1, n):
    rhs = rhs + f[j-1] * y[n-1][j]

print('The interpolating polynomial is:')
display(simplify(rhs))

# Evaluate the interpolating polynomial at a given value of x
xi = float(input('Enter the value of x at which y should be determined: '))
result = rhs.subs(t, xi)
print(f'y({xi}) = {result.evalf():.4f}')
