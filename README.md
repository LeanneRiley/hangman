# Hangman

## Project Description

### Project Aim
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess the word, by entering one letter at a time. 
The user is given a total of 5 lives. Each time they guess a letter incorrectly, they lose a life. If they lose all their lives then the program will terminate.
Should the user guess all letters in the randomly generated word (from a pre-defined list) correctly without losing all their lives, then this will be considered a win and the program is terminated. 

### What does the program do?

#### Program Overview:
(1) If the user does not guess the letter correctly then they lose a life, after 5 incorrect guesses, the program will print that the user has lost and will terminate.
(2) If the user guesses the letter correctly, then they are prompted that their guess was correct and the users progress is printed e.g. ['p', 'e', 'a', '_']
(3) If the user is able to guess all letters in the randomly generated word correctly before losing 5 lives, then the program terminates and this is considered a win. 
(4) If the user guesses the same letter then they are prompted that they have guessed this letter already and to enter a single letter. 
(5) If the user enters an invalid character, i.e. the guess is not a single alphabetical character then the user is prompted that it is an invalid guess and is then asked to enter a single letter. 

#### This program uses functions to:
(a) check the user input (validating the user entered response)
(b) check that the entered letter is in the random generated word (the word is randomly generated from a pre-defined list).
(c) Initiate the hangman game and determine whether the player has won or lost.




