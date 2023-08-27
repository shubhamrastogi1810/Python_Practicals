""" Day 42: Spelling Checker
Write a function called spelling_checker. This code asks the
user to input a word and if a user inputs a wrong spelling it
should suggest the correct spelling by asking the user if they
meant to type that word. If the user says no, it should ask the
user to enter the word again. If the user says yes, it should
return the correct word. If the word entered by the user is
correctly spelled the function should return the correct word.
Use the module textblob. """
from textblob import TextBlob as tb
def spelling_checker():
    while True:
        x = input(' Enter a word. ')
        word = tb(x)
        right_word = str(word.correct())
        user = input('Did you mean '+ right_word +' y/n')
        if user == 'y':
            return right_word
            break
    	



print('You entered. ',spelling_checker())
