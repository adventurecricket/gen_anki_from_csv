import os
from anki import anki
import pandas as pd

def read_csv(file_path):
    df = pd.read_csv(file_path)

    return df

def write_error_word(error_words):
    with open('error_words.txt', 'w') as f:
        f.writelines(error_words)

def main(file_path, deck_name, note_type):
    df = read_csv(file_path)
    error_words = anki.gen_anki_apkg_file(deck_name, note_type , df)
    words_len = df.shape[0]
    error_words_len = len(error_words)
    if error_words_len > 0:
        write_error_word(error_words) 
        print(f'Successly {words_len - error_words_len}/{words_len}.')
        print(f'Error {error_words_len}/{words_len}: Some words have eror during execution, pls check the error_words.txt file for datails.')
    else:
        print(f'Complete {words_len} words.')

if __name__ == '__main__':
    while True:
        file_path = input('Please enter the path of your words file: ')
        file_path = file_path.strip()
        if file_path.strip() == "":
            print("File path cannot be empty.")
            continue
        elif not os.path.isfile(file_path):
            print("This file is unavailable.")
            continue
        else:
            break
    print('-------------------------------')
        
    while True:
        deck_name = input('Pls enter your the deck name that do you want: ')
        deck_name = deck_name.strip()
        if deck_name.strip() == "":
            print("Deck name cannot be empty")
            continue
        else:
            break
    print('-------------------------------')
        
    while True:
        note_type = input('Pls enter your the note type that do you want: ')
        note_type = note_type.strip()
        if note_type.strip() == "":
            print("Note type cannot be empty")
            continue
        else:
            break
    print('-------------------------------')

    main(file_path, deck_name, note_type)
    input()