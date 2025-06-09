import pandas as pd

# Generate full dataset of kanjies
kanjies_and_data = pd.read_csv("https://raw.githubusercontent.com/Goezs/kanji_with_radicals/main/Kanji.csv")

kanjies_and_data.to_csv("kanjies_and_data.csv", columns= ["Kanji", "Meaning", "Radicals", "Sound"], index = False)

# Generate empty vocabulary dataset
vocabulary = pd.DataFrame(columns= ["Kanji", "Meaning", "Radicals", "Sound"])

vocabulary.to_csv("vocabulary.csv", columns= ["Kanji", "Meaning", "Radicals", "Sound"], index = False)