#  Tansportation Mode Selection

# Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car)

Distance = int(input("Enter the Distance:"))

if Distance < 3:
    transport = "WAlk"
elif Distance <= 15:
    transport = "Bike"
else:
    transport = "Car"

print("Mode of trnasport you should choose acc. to your distance is:",transport)