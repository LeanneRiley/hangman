import random


class Hangman:
    '''A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried
        
    Methods:
    -------
    check_guess(guess)
        Checks if the letter is in the word.
    ask_for_input()
        Asks the user for a letter.'''
    
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len([num for num in self.word_guessed if num == '_'])
        self.num_lives = num_lives
        self.list_of_guesses = []


    def check_guess(self, guess):
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        guess: str
            The letter to be checked

        '''
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            self.num_letters = self.num_letters - 1
            for i in range(len(self.word)): #TODO identify index position of the matching letter and update word_guessed list at the corresponding index
                if self.word[i] == guess:
                    self.word_guessed[i] = guess

        else:
            self.num_lives = self.num_lives - 1
            print(f"Sorry, {guess} is not in the word")
            print(f"You have {self.num_lives} lives left")
        print(self.word_guessed) #Temporary check
        print(self.num_letters) #Temporary check

    def ask_for_input(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the character is a single alphabetical character
        2. If the letter has already been tried
        If it passes both checks, it calls the check_guess method.
        '''
        while True:
            guess = input("Please enter a single letter: ")
            if len(guess) != 1 or guess.isalpha() != True:
                print("Invalid Letter. Please, enter a single alphabetical character")
            elif guess in self.list_of_guesses:
                print("You already tried that letter")
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)
                
word_list = ['apple', 'playdough', 'carrots', 'ambulance', 'Hannah']
game = Hangman(word_list)
game.ask_for_input()
        
