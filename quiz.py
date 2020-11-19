import sys
import random
from utils import CreateDeck, my_model, AddNoteToDeck, WriteDeckToFile

dictionary = []

for line in open('/home/samuele/Downloads/TEDESCO.txt'):  # opened in text-mode; all EOLs are converted to '\n'
    line = line.rstrip('\n')
    dictionary.append(line)

indeces = []
for i in range(len(dictionary)):
    indeces.append(i)

random.shuffle(indeces)

print("Choose your Deck question to answer order \n German to translation -> select 1 \nTranslation to German -> select 2 \n")

selection = input()
selection = int(selection)

while ((selection != 1) & (selection != 2)):
    print("You didn't select 1 or 2, try again \n")
    selection = input()
    selection = int(selection) 

my_deck = CreateDeck(selection)

for random_index in indeces:
    line = dictionary[random_index]
    german_words = ""
    translation_attempt = ""
    german_attempt = ""
    translation = ""
    is_there_an_equal = False
    there_was_an_equal = False
    for char_index in range(len(line)):
        german_words += line[char_index]
        if selection == 1:
            if line[char_index] == "=":
                #translation_attempt += input(german_words + "\n")
                is_there_an_equal = True
                there_was_an_equal = True
            if is_there_an_equal:
                translation += line[char_index + 1:]
                #print(translation + "\n")
                is_there_an_equal = False
                AddNoteToDeck( german_words , translation, my_deck)

        elif selection == 2:
            if line[char_index] == "=":
                translation += line[char_index + 1 :]
                #german_attempt += input(translation + " = \n")
                is_there_an_equal = True
                there_was_an_equal = True
    
            if is_there_an_equal:
                german_words = german_words[:-2]
                #print(german_words + "\n")
                is_there_an_equal = False
                AddNoteToDeck( translation , german_words, my_deck)
    if there_was_an_equal == True:
        #input("Press Enter to continue...")
        there_was_an_equal = False

WriteDeckToFile(my_deck, "/home/samuele/Desktop")              