import pandas as pd

# Get vocabulary
vocabulary = pd.read_csv("../kanjgetting/cleared_vocabulary.csv", index_col= 0)

# Complete kanjies
vocabulary_kanjies = vocabulary.iloc[:, 0]

banned_nums = []
cleared_vocabulary = []

for i in range(len(vocabulary_kanjies)):
    if i in banned_nums:
        continue     
    word_i = vocabulary_kanjies.iloc[i]

    for j in range(len(vocabulary_kanjies)):
        if j in banned_nums:
            continue     
        word_j = vocabulary_kanjies.iloc[j]
        if word_i == word_j:
            banned_nums.append(j)

    cleared_vocabulary.append(i)
    banned_nums.append(i)

cleared_vocabulary_data = vocabulary.iloc[cleared_vocabulary, :]

cleared_vocabulary_data.to_csv("cleared_vocabulary.csv", columns = ["Kanji", "Meaning", "Radicals", "Sound"])

