# 🎮 Hangman Game

A classic Hangman word-guessing game implemented in Python with an interactive console interface.

## 📋 Description

This is a fun, terminal-based implementation of the popular Hangman game. Players try to guess a hidden word by suggesting letters one at a time. You have 6 incorrect guesses before the game ends.

## 🎯 How to Play

1. Run the game script
2. A random word is selected from the word list
3. Guess letters one at a time when prompted
4. Each correct guess reveals the letter(s) in the word
5. You have 6 attempts to guess incorrect letters
6. Win by guessing all letters before running out of attempts
7. Lose if you exhaust all 6 attempts before completing the word

## 📝 Features

- **Random Word Selection**: Each game picks a random word from a predefined list
- **Input Validation**: Only accepts single alphabet letters
- **Duplicate Prevention**: Prevents re-guessing the same letter
- **Game Status Display**: Shows current progress, guessed letters, and remaining attempts
- **Visual Feedback**: Uses emojis for better user experience
  - ✅ Correct Guess
  - ❌ Wrong Guess / Invalid Input
  - ⚠️ Duplicate Guess Warning
  - 🎉 Victory Message
  - 💀 Game Over Message

## 🚀 Requirements

- Python 3.x
- No external dependencies (uses only built-in modules)

## 💻 Running the Game

```bash
python task2.py

