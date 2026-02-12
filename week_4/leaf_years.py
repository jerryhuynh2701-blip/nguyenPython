year = int(input("Enter number year: "))

if year % 400 == 0:
    print("Leaf year")
elif year % 100 == 0:
    print("Not leaf year")
elif year % 4 == 0:
    print("Leaf year")
else:
    print("False")