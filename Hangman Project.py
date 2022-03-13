import random
import time

#   Initial game sequence:
print("Welcome to H A N G M A N :)")
name = input("Enter your name: ")
time.sleep(5)
print("Hope you survive. . . " + name)

def main_function():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess =
    ["farts"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""

#   Loop

def play_loop():
    global play_game
    play_game = input("Do you want to play? Y = yes, you don't get to say no \n")
    while play_game not in ["y", "Y"]
        play_game = input("Wrong answer buddy... ")
        if play_game == "y":
            main()
            else print("What the heck, fine bye")
            exit()

def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("This is all you get punk: " + display + "\n What's your guess stupid?: ")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >=2 or guess <= "9":
        print("Hey Dummy, you can't guess that\n")
        hangman()
    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
