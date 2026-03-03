# Coffee Customization

# Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

order_size = input("Enter oder size from Small, Medium, Large:")
extra = input("Need Extra Shot Espresso? (yes/no):")

if extra == "yes":
    coffee = order_size + " Coffee with extra shot"
else:
    coffee = order_size + "Coffee"

print("Order:",coffee)