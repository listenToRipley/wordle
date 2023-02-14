import pathlib
import sys 
from string import ascii_letters

in_path = pathlib.Path(sys.argv[1]) #where the words are coming from
out_path = pathlib.Path(sys.argv[2]) #where they are going.

words = sorted(
    {
        word.lower() #create an array of all lowercase words within a given path
        for word in in_path.read_text(encoding="utf-8").split()
        if len(word) == 5 and all(letter in ascii_letters for letter in word)
    },
    key=lambda word: (len(word), word),
)

out_path.write_text("\n".join(words)) #add new word to old list.