name = input("What is your name : ")
age  = int(input("Enter your age : "))
married_input = input("Are you married? Enter True or False: ").strip().lower()
married = married_input == "true"
print(f"Hi ! {name} , you are {age} years old and married {married} ")
