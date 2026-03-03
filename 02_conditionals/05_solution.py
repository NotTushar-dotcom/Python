# Weather Activity Suggestion

# Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman)

Weather = input ("Enter today's Weather:")

if Weather == "Sunny":
    activity = "Go for a walk"
elif Weather == "Rainy":
    activity = "Read a book"
elif Weather == "Snowy":
    activity = "Build a snowman"

print("Today's Weather is",Weather,"\nActivity You Should Do:",activity)