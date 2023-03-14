import random

# Define a list of Valentine's Day words
words = ['pretty eyes', 'sthandwa sami', 'always and forever', 'pinky promise', 'maGumede', 'the light', 'the vibe manual', 'arcade', 'vanilla chai', 'umkhokha']

# Select a random word from the list
word = random.choice(words)

# Hide the letters of the word
hidden_word = ['_' for letter in word]

# Set the number of guesses
num_guesses = 10

# Start the game loop
while num_guesses > 0:
    # Print the hidden word
    print(' '.join(hidden_word))
    
    # Get a guess from the user
    guess = input('Guess a letter: ')
    
    # Check if the guess is correct
    if guess in word:
        # Update the hidden word with the guess
        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess
        # Check if the word is fully revealed
        if '_' not in hidden_word:
            print('Congratulations, you revealed the word', word)
            break
    else:
        # Decrease the number of guesses
        num_guesses -= 1
        print('Wrong guess! You have', num_guesses, 'guesses left.')
        
# End the game
if num_guesses == 0:
    print('Sorry, you ran out of guesses. The word was', word)
