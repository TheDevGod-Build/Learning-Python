weight = float(input("Enter your weight: "))
unit = input("Is your weight in Kg or Lb (K or L): ")

if unit == "K":
    weight = weight * 2.205
    print(f"Your weight is {weight} in lbs.")
elif unit == "L":
    weight = weght / 2.205
    print(f"Your weight is {weight} in kgs.")
else:
    print("Invalid unit")