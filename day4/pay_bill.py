import random

friends = ['Ram','Shyam','Manoj','Raju']
random_number = random.randint(0,len(friends)-1)
print(random.choice(friends))
print(friends[random_number])