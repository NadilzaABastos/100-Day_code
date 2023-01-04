import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet = {row.letter: row.code for (index,row) in data.iterrows()}
name = input(str("Type a word :")).upper()
new_list = [alphabet[letter] for letter in name]
print(new_list)

