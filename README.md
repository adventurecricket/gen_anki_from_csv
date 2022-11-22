#SUMMARY
This app allows you to import a list from a .csv file to create cards for Anki.
The .csv file must have the format with 3 cols: Word, Ipa, and Meaning. You can refer to the words.csv file in the project.


# genanki: A Library for Generating Anki Decks

`genanki` allows you to programatically generate decks in Python 3 for Anki, a popular spaced-repetition flashcard
program. Please see below for concepts and usage.

* This genanki library is by Rob Sanek author, you can visit this project for more https://github.com/kerrickstaley/genanki


# To run application

1. Turn on cmd promot and run this commandline: py main.py
2. Enter the path of your words file (.csv).
3. Enter your the deck name that do you want.
4. Enter your the note type that do you want.
5. You can then load `{deck_name}.apkg` into Anki using File -> Import...
6. If it has some words have eror during execution, pls check the error_words.txt file for datails.
