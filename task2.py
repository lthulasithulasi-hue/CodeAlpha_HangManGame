import random


words = ["python", "computer", "coding", "developer", "program"]


word = random.choice(words)


guessed_word = ["_"] * len(word)

guessed_letters = []


attempts = 6

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.\n")

while attempts > 0 and "_" in guessed_word:
    print("Word:", " ".join(guessed_word))
    print("Guessed Letters:", ", ".join(guessed_letters))
    print("Remaining Attempts:", attempts)

    guess = input("Enter a letter: ").lower()

  
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single alphabet letter.\n")
        continue

   
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    
    if guess in word:
        print("✅ Correct Guess!\n")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        attempts -= 1
        print("❌ Wrong Guess!\n")


if "_" not in guessed_word:
    print("🎉 Congratulations! You guessed the word:", word)
else:
    print("💀 Game Over!")
    print("The correct word was:", word)