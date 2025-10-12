Hangman/ Wisielec 

A classic word guessing game implemented in Python. Version with categories, difficulty levels, and a hint system.

Requirement:
-> Python 3.13

Install and Start:
-> python wisielec.py
-> git clone https://github.com/Magdaa1/hangman.git

Rules of the Game 📖
-> The game consists of guessing a word letter by letter.
-> The number of allowed mistakes depends on the selected **difficulty level**.
-> Enter letters and then press Enter.
Special commands** (when available):
 -> `HINT`: Uses one of the hints (if available).
 -> `GIVE UP`: Ends the game and reveals the word.


Programming Concepts 💡
The project was created for educational purposes and demonstrates the use of the following concepts:

->Lists & Dicts:** Storing the word base (`CATEGORIES`) and configuration (`LEVELS`).
-> Sets: Efficient tracking of guessed and incorrect letters.
-> Input Validation:** Using `.isalpha()` and error handling (`try-except`).
-> Randomness:** Using the `random` module to select categories and words.
-> List Comprehension:** Short and efficient creation of the game state view (`display_state`).
