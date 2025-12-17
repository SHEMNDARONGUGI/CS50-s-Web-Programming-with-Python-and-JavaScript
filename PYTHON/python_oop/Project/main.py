import sys

for i in range(10):
    name = input(f"{i+1}. Name: ")
    try:
        phone_number = int(input("Phone Number: "))
    
        print(f"\nName: {name} & Phone number: {phone_number} Added Successfully!!! \n")
    except ValueError:
        print("Input an Integer!!!")
        sys.exit(1)
        
    