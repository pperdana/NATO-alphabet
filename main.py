import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data[:5], "\n")

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

nato_code = {row.letter: row.code for (index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Enter a word: ").upper()

nato_output = [nato_code[char] for char in user_input]
print(nato_output)
