# Read the coefficients a, b, c, d, e
a, b, c, d, e = map(int, input().split())

# Define the polynomial function


def polynomial(x):
    return a * x**4 + b * x**3 + c * x**2 + d * x + e


# Try integer values of x in a reasonable range around zero
for x in range(-10000, 10001):
    if polynomial(x) == 0:
        print(x)
        break

