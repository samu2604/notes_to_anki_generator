import random
import genanki

model_id = random.randrange(1 << 30, 1 << 31)
my_model = genanki.Model(
  model_id,
  'Simple Model',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Question}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
    },
  ]) 

def CreateDeck(selection):
    deck_title = ""
    if selection == 1:
        deck_title += "German to Translation"
    elif selection == 2:
        deck_title += "Translation to German"  
    deck_id = random.randrange(1 << 30, 1 << 31)
    my_deck = genanki.Deck(
    deck_id,
    deck_title)
    return my_deck

def AddNoteToDeck( question , answer, my_deck):
    my_note = genanki.Note(
    model=my_model,
    fields=[question, answer])
    my_deck.add_note(my_note)

def WriteDeckToFile(my_deck, file_path):
    file_path += "/my_german_learning_deck.apkg"
    genanki.Package(my_deck).write_to_file(file_path)



