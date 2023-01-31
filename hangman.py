from random_word import RandomWords
print("Hangman V0.1")
print("\nWelcome To A Basic Hangman Game")
print('''
Rules:
1. You Have 6 Chances To Guess All The Missing Characters
2. Guess All The Characters Before You Run Out Of Chances
''')
attempts = 6
userName = input("Enter Your Name: ")
objectWord = RandomWords()
guessWord = objectWord.get_random_word()
guessWord = guessWord.upper()
displayWord = '_'*len(guessWord)
displayWordList = list(displayWord)
#displayWordList[1] = '2' #This Works
print("This Is The Word To Be Guessed: " + displayWord)
print(guessWord)
while(attempts!=0):
    userGuess = input("Enter Guess: ").upper()
    if (not userGuess.isalpha()):
        print("Enter A Valid Letter")
    elif userGuess in guessWord:
        for i in range(len(guessWord)):
            if (guessWord[i]==userGuess):
                displayWordList[i]=userGuess #Here
                print(displayWordList[i])
        print(''.join(displayWordList))
    else:
        print("Input Not In Word. Try Again")
        attempts-=1
    if (''.join(displayWordList)==guessWord):
        print("Guessed Word!")
        exit()
print("Word Not Guessed. Try Again")