print(" ******* Welcome to tip calculator ******* ")

total_bill =float (input("What is your total bill : "))
tip_percentage =float(input("How much percentage tip you want to give 5 , 10 and 12 : "))
number_Of_person =int( input("In how many people you want to divide the bill : "))
amount_need_to_Pay = (total_bill+(total_bill*(tip_percentage/100)))/number_Of_person

print(amount_need_to_Pay)