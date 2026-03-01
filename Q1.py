# AGE GROUP CATEGORIZATION:

# classify a person's age group: Child (<13), Teenager(13-19), Adult (20-64), Senior (65+)

age = int(input("Enter the age:"))

if age < 13:
    print("child")
elif age < 20:
    print("Teenager")
elif age < 64:
    print("Adult")
else:
    print("Senior")