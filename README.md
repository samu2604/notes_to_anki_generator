# notes_to_anki_generator
This is a script able to automatically transform your notes from a language lesson in an Anki deck useful to learn the existing vocabulary.

Your notes shall be written in a .txt format and your specific paths shall be updated in the open function inside quiz.py and in the WriteDeckToFile function

To use it you need to import the [genanki](https://github.com/kerrickstaley/genanki) external library 

If in your note you write text in the following way:

* Text in the foreign language ... = traslation of the text ...

You will get (selecting 1 as order) the following flashcard in your deck:

* question: Text in the foreign language ... 
* answer: traslation of the text ...

You will get the opposite order selecting 2
