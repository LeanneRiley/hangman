import random

def ask_for_input():#checks the length of input and that it is not numeric + also generates random word from list
    global guess
    guess = input("Please enter a single letter: ")
    if len(guess) == 1 and guess.isalpha() == True: 
        word_list = ['banana', 'mango', 'guinep', 'grapes', 'watermelon']
        global word
        word = random.choice(word_list)
        print(word)
        check_guess(guess)
        return True
    else:
        return False

def check_guess(guess): #identifies if user input is in the random generated word
    guess = guess.lower()
    if guess in word:
        return True
    else:
        return False

while True: #While loop that will check the outcome of the functions to determine whether to continue or break out of the loop
    if ask_for_input() == False:
        print("Invalid letter. Please, enter a single alphabetical character.")
        continue
    if check_guess(guess) == False:
        print(f"Sorry, {guess} is not in the word. Try again.")
        continue
    if check_guess(guess) == True:
        print(f"Good guess! {guess} is in the word")
        break

    
        
