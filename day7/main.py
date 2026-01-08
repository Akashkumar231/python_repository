import random
word_list = ["camel","baboon","racoon"]

# Randomly choose a word from the list and print it.
random_word = random.choice(word_list)
print(f"The random word is : {random_word}")

# Ask the user to enter a letter ,let make the user to guess a letter.
guess = (input("Guess a letter : ")).lower()
print("The letter selected : " + guess)

# If the guess is wrong print wrong else right.
for letter in random_word:
    if guess == letter:
        print("Right")
    else:
        print("Wrong")