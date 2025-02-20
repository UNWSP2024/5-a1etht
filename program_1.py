#Programmer: Alethea Lo
#Date: 2/19/25
#Title: Kilometer Converter

def convert_km_to_miles(km):
    """Converts kilometers to miles."""
    miles = km * 0.6214
    return miles

# Get user input
distance_km = float(input("Enter distance in kilometers: "))

# Convert to miles
distance_miles = convert_km_to_miles(distance_km)

# Display the result
print(f"{distance_km} kilometers is equal to {distance_miles:.2f} miles.")