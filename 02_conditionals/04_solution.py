# Fruit Ripeness Checker

# Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

Fruit = input("Enter the fruit you want to check: ")
color = input("Enter the color of the fruit: ")

if Fruit == "Banana":
    if color == "Green":
        print("Unripe")
    elif color == "Yellow":
        print("Ripe")
    elif color == "Brown":
        print("Overripe")
else:
    print("No Info About Fruit!!")