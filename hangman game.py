import random


words = (
    "Elephant",
    "Bicycle",
    "Computer",
    "Mountain",
    "Oxygen",
    "Kangaroo",
    "Rainbow",
    "Hospital",
    "Universe",
    "Library"
)

def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        --------
        """
    ]
    return stages[tries]

def hangman_game():
    tries = 6 # Only 6 tries
    x = random.randint(0,len(words)) 
    word = words[x].lower() # Random word is chosen
    word_dict = {} # hash key of the word, to make it easier to fill
    for i in range(len(word)):
        char = word[i]
        if char in word_dict:
            word_dict[char].append(i)
        else:
            word_dict[char] = [i]
    full_word = ['_']*len(word) # Check the final word
    print(display_hangman(tries)) #For start
    print(full_word) # For start
    while True:
        char = str(input("Guess:"))
        if char in word: # Correct guess
            for i in word_dict[char]:
                full_word[i] = char
            print(display_hangman(tries))
            print(full_word)
            
        else: # Wrong guess
            tries -= 1
            print(display_hangman(tries))
            print(full_word)
            
        if tries == 0: # You lose when you have no tries left
            print(display_hangman(tries))
            print("You lose!")
            choice = input('Know the word(1) or skip(any key):')
            if choice == '1':
                print('The word is', word)
            else:
                print('No words shown')
            break
             
        if ''.join(full_word) == word: # Check the final word
            print(display_hangman(tries))
            print(full_word)
            print(f'Correct, the word is {word}!')
            break

#hangman_game() (# Start the game)
