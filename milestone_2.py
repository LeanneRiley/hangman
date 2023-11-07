import random
guess = input("Please enter a single letter: ")

if len(guess) == 1 and guess.isalpha() == True:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")

word_list = ['Banana', 'Mango', 'Guinep', 'Grapes', 'Watermelon']

word = random.choice(word_list)

print(word)