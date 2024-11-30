import random

hangman_graphics = [
    '''
     _______
    |/      |
    |      
    |     
    |       
    |      
    |     
    |______|
    ''', '''
     _______
    |/      |
    |      ( )
    |     
    |       
    |      
    |     
    |______|
    ''', '''
     _______
    |/      |
    |      ( )
    |      \|
    |       
    |      
    |     
    |______|
    ''', '''
     _______
    |/      |
    |      ( )
    |      \|/
    |       
    |      
    |     
    |______|
    ''', '''
     _______
    |/      |
    |      ( )
    |      \|/
    |       |
    |      
    |     
    |______|
    ''', '''
     _______
    |/      |
    |      ( )
    |      \|/
    |       |
    |      / 
    |     
    |______|
    ''', '''
     _______
    |/      |
    |      ( )
    |      \|/
    |       |
    |      / \ 
    |     
    |______|
    '''
]

def display_hangman(tries):
    print(hangman_graphics[6 - tries])  


easy_words = ['cat', 'dog', 'fish', 'bird']
medium_words = ['apple', 'banana', 'cherry', 'grape']
hard_words = ['pineapple', 'watermelon', 'strawberry', 'blueberry']


def choose_difficulty():
    print("Choose Difficulty Level: ")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    while True:
        try:
            choice = int(input("Enter 1, 2, or 3: "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid number.")


difficulty = choose_difficulty()
if difficulty == 1:
    words = easy_words
    number_of_tries = random.randint(8, 10)
elif difficulty == 2:
    words = medium_words
    number_of_tries = random.randint(5, 8)
else:
    words = hard_words
    number_of_tries = random.randint(3, 5)

chosen_word = words[random.randint(0, len(words)-1)]
# print(chosen_word)

hidden_word = ['_'] * len(chosen_word)#list abrunebs
wrong_guesses = []
correct_guesses = []
guesses = 0

while number_of_tries > 0 and '_'  in hidden_word:
    print(' '.join(hidden_word)) # gamosaxuleb defisebit
    print(f'{number_of_tries} tries left:')
    print(f'Incorrect guesses: {", ".join(wrong_guesses)}')

    if number_of_tries <= 6:
        display_hangman(number_of_tries)

    try:
        guess = input("Enter the letter or word: ").lower()
        print()

        if (len(guess) != 1 and len(guess) != len(chosen_word)) or not guess.isalpha():
            raise ValueError("Please enter a valid single letter.")
        
        if guess in correct_guesses or guess in wrong_guesses:
            print("you already guessed that letter.")
            continue
        
        if guess == chosen_word:
            correct_guesses.append(guess)
            guesses += 1
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess[i]:
                    hidden_word[i] = guess[i]
        elif guess in chosen_word:
            correct_guesses.append(guess)
            guesses += 1
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    hidden_word[i] = guess
        else:
            number_of_tries -= 1
            wrong_guesses.append(guess)
            print(f"Wrong guess! Tries left: {number_of_tries}")

    except ValueError as e:
        print(e)
        continue

if '_' not in hidden_word:
    print(f"Congratulations! you guessed the word {chosen_word}")
    print(f"You guessed the word in {guesses} tries.")
else:
    print(f"Game Over! The word was: {chosen_word}")




