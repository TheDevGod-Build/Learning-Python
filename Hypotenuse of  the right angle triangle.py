import math

height = float(input("Enter the height of the triangle: "))
base = float(input("Enter the base of the triangle: "))

hypotenuse = math.sqrt(pow(height , 2)+ pow(base , 2))

print(f"Hypotenuse of the triangle is {round(hypotenuse , 3)}")