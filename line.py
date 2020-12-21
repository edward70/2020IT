x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

m = (y2 - y1) / (x2 - x1)

print("Gradient is {:g}".format(m))

c = y1 - (m * x1)

print("y-int is {:g}".format(c))

print("Equation: y = {:g}x + {:g}".format(m,c))