import random
from hangman_words import lists_of_words
from hangman_art import logo, stages
from replit import clear

print(logo)
end_of_game = False
lives = 6

word = random.choice(lists_of_words)
word_length = len(word)

# Create blanks
display = []
for _ in range(word_length):
    display += "_"


while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # replit to clear output between guesses
    clear()

    # Guessed letter checked
    for position in range(word_length):
        letter = word[position]

        if letter == guess:
            display[position] = letter

    if guess not in word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # join the list and turn it into a string
    print(f"{' '.join(display)}")

    # Check if user got all letters right
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])