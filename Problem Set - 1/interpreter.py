expression = input("Expression: ")

x,y,z = expression.split()
x = float(x)
z = float(z)

if y == "+":
        math =  x + z
elif y == "-":
        math =  x - z
elif y == "*":
        math = x * z
elif y == "/":
    if z != 0:
            math = x / z
    else:
            math = "Denominator cannot be Zero"
else:
        math = "Enter a valid operator"


print(f"{math:.1f}") if isinstance(math, float) else print(math) #This handles both cases where the output might be a numeric value or a string.
