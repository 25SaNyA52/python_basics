#Task 1: Calculating addition,substraction & multiplication for 2 numbers
print("Task 1: Calculating arithmetic mean")
a = float(input("a = "))
b = float(input("b = "))
print("Addition result = ", a+b)
print("Substraction result = ", a-b)
print("Multiplication result = ",a*b)

#Task 2: Calculating x - (y / (1 + x * y)
print("Task 2: Calculating x - (y / (1 + x * y)")
x = float(input("x = "))
y = float(input("y = "))
result = x - (y / (1 + x * y))
print("x - (y / (1 + x * y)= ",result)

#Task 3: Calculating arithmetic & geometric mean for 2 numbers
print("Task 3: Calculating arithmetic & geometric mean for 2 numbers")
a = float(input("a = "))
b = float(input("b = "))
arith_mean = (a + b) / 2
geo_mean = (a * b) ** 0.5
print("Arithmetic mean: ", arith_mean)
print("Geometric mean: ", geo_mean)

#Task 4: Calculating the area and hypotenuse of a right triangle
print("Task 4: Calculating the area and hypotenuse of a right triangle")
a = float(input("1st side length = "))
b = float(input("2nd side length = "))
hypotenuse  = (a**2 + b**2) ** 0.5
area = (a * b) / 2
print("Hypotenuse result = ", hypotenuse)
print("Area result = ", area)