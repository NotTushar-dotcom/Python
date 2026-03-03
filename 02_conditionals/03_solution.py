# Grade Calculator

# Assign a letter grade based on a student"s score: A(90-100), B(80-89), C(70-79), D(60-69), F(below 60)

Score =int(input("Enter Total Score:"))

if Score >=101:
    print("Please Check Score Again !!")
    exit()

if Score >= 90:
    print("Grade A")
elif Score >= 80:
    print("Grade B")
elif Score >= 70:
    print("Grade C")
elif Score >= 60:
    print("Grade D")
else:
    print("Grade F")

