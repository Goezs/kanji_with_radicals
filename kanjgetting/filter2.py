import pandas as pd

# Get vocabulary
vocabulary = pd.read_csv("../kanjgetting/cleared_vocabulary.csv")

# identify kanjies with long meaning in "()"
kanjies_meanings = vocabulary.iloc[:, 1]

not_changed_vocabulary_idx = []

cleared_meanings_vocabulary = []

def get_parentesis_str(meaning, idx_parentesis):
    """
    If inside "()" theres more than 21 letters cut it out

    Args:
        meaning (str): Complete meaning of the symbols
        idx_parentesis (str): Index where the parentesis start in the meaning 

    returns:
        parentesis_s(str or int): The str with the content in the parentesis, if is more than
            21 letters, returns an int with the lenght of the str 
    """
    parentesis_s = ""
    for s_j in meaning[idx_parentesis:]:
        if s_j == ")":
            parentesis_s += ")"
            break
        parentesis_s += s_j
    
    if len(parentesis_s) > 20:
        return len(parentesis_s)
    return parentesis_s

## len(kanjies_meanings) == len(kanjies_radicals)
for i in range(len(kanjies_meanings)):
    
    meaning_i = kanjies_meanings.iloc[i]
    cleared_meaning = 0
   
    new_meaning_i = ""

    ## for s_i in range(len(meaning_i)):
    s_i = 0
    while s_i < len(meaning_i):
        if meaning_i[s_i] == "(":
            ## Goes inside the parentesis to see if its too large
            parentesis_s = get_parentesis_str(meaning_i, s_i)
            if  type(parentesis_s) == int:
                cleared_meaning = 1
                s_i += parentesis_s
            else:
                new_meaning_i += parentesis_s
                s_i += len(parentesis_s)
            continue
        new_meaning_i += meaning_i[s_i]
        s_i += 1

    ## Add data to the vocabulary
    if cleared_meaning == 1:
        data_to_add = [vocabulary.iloc[i,0], new_meaning_i, vocabulary.iloc[i,2], vocabulary.iloc[i,3]]
        cleared_meanings_vocabulary.append(data_to_add)
    else:
        not_changed_vocabulary_idx.append(i)
 
# Generates an empty cleared_vocabulary1.csv
###  c_vocabulary1 = pd.DataFrame(columns= ["Kanji", "Meaning", "Radicals", "Sound"])

###  c_vocabulary1.to_csv("cleared_vocabulary1.csv", columns= ["Kanji", "Meaning", "Radicals", "Sound"], index = False)
# Cleared meanings dataset
cleared_meanings_vocabulary_df = pd.DataFrame(cleared_meanings_vocabulary, columns = ["Kanji", "Meaning", "Radicals", "Sound"])


# Vocabulary dataset (Not changed rows)
vocabulary_data_not_changed = vocabulary.iloc[not_changed_vocabulary_idx, :]

# Concatenate the datasets
cleared_vocabulary1 = pd.concat([vocabulary_data_not_changed, cleared_meanings_vocabulary_df])

### print(cleared_vocabulary1.iloc[0:25])
# Upload the data
cleared_vocabulary1.to_csv("cleared_vocabulary1.csv", columns = ["Kanji", "Meaning", "Radicals", "Sound"], index = False)

