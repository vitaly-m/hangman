# Write your code here
import random
import string

print("H A N G M A N")
command = input('Type "play" to play the game, "exit" to quit:')
words = ("python", "java", "kotlin", "javascript")
word = random.choice(words)
word_arr = list("-" * len(word))
guess_word = ''.join(word_arr)
typed = set()

while command == "play":
    lives = 8
    while lives > 0:
        found = False
        guess_word = ''.join(word_arr)
        print(f"\n{guess_word}")
        guess = input("Input a letter:")
        if len(guess) != 1:
            print("You should print a single letter")
            continue
        if guess not in string.ascii_lowercase:
            print("It is not an ASCII lowercase letter")
            continue
        if guess in typed:
            print("You already typed this letter")
            continue
        typed.add(guess)
        for c in range(len(word)):
            if word[c] == guess:
                found = True
                word_arr[c] = guess
        if not found:
            lives -= 1
            print("No such letter in the word")
        elif guess_word == word:
            break

    if guess_word == word and lives > 0:
        print(f"\n{word}")
        print("You guessed the word!")
        print("You survived!")
    else:
        print("You are hanged!")
    command = input('\nType "play" to play the game, "exit" to quit:')
