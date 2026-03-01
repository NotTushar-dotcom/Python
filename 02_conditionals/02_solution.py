# MOVIE TICKET PRICING

# Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children.Everyone gets $2 discount on Wednesday.

age = int(input("Enter Your Age:"))
day = input("Enter Today's Day:")

price = 12 if age >= 18 else 8

if day == "Wednesday":
    price -= 2

print("Ticket price is $",price)