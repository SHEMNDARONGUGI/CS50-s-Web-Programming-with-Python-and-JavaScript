first_name = input("Input your first name: ")
second_name = input("Input you second name: ")

age = int(input("Input your age: "))
if(age >= 18 ):
    print(f"Hello { first_name } {second_name},\nYour age:{age}\nYou are eligible for the program")

else:
    print("Not qualified")
    
    