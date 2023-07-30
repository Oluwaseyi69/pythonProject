gallons = 0
miles = 0
counter = 0

while gallons != -1:

    gallons = int(input("Enter the gallons used (-1 to end): "))
    miles = int(input("Enter miles the driven:  "))
    miles_gallon = miles / gallons
    counter = counter + 1

    if gallons != -1:
        print("mile_gallon", miles_gallon)
    else:
        overall_average = miles_gallon / counter
        print("overall_average", overall_average)
