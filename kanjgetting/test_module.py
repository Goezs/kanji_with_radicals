from selenium import webdriver
from selenium.webdriver.common.by import By

import pandas as pd

# Get the kanjies to search in jisho
kanjies_and_data = pd.read_csv("../kanjgetting/kanjies_and_data.csv")

kanjies_and_meanings = kanjies_and_data.iloc[:, [0,1]]

# Open the driver and page
options = webdriver.EdgeOptions()
options = options.add_argument("--no-sandbox--")

driver = webdriver.Edge(options = options)


driver.get("https://jisho.org/")


# driver.implicitly_wait(25.5)

def search_kanji(kanji):
    global driver
    # Searching tool
    text_box = driver.find_element(by = By.NAME, value= "keyword")
    submit_button = driver.find_element(by=By.CLASS_NAME, value = "submit")

    ## Submit with searching tool
    text_box.send_keys("*%s*" % (kanji))
    submit_button.click()

def get_information(concept):
    """
    Verifies if a concept related to a search, can be vocabulary or not.
    If it is vocabulary save's the information

    args:
        concept : block of information with a concept related to a search

    returns:
        info_row : None if it's not suitable, or an array with
                    kanji text, meaning text and reading text
    """
    global kanjies_and_meanings
    # Left column

    tag_column = concept.find_element(by = By.CLASS_NAME, value = "concept_light-wrapper")

    ## Wanikani tag data

    tag_column_child = tag_column.find_elements(by = By.CLASS_NAME, value = "concept_light-status")

    if len(tag_column_child) < 1:
        return None

    tags = tag_column_child[0].find_elements(by = By.CLASS_NAME, value = "concept_light-tag")

    if len(tags) < 1:
        return None

    wani_tag = tags[-1].find_elements(by = By.TAG_NAME, value= "a")

    if len(wani_tag) < 1:
        return None
   
    ## reading info

    reading_column = tag_column.find_element(by = By.CLASS_NAME, value= "concept_light-readings")

    reading_column_child = reading_column.find_element(by = By.CLASS_NAME, value= "concept_light-representation")

    ### kanji form

    reading_text= reading_column_child.find_element(by = By.CLASS_NAME, value = "text")

    kanji_text = reading_text.text
    if len(kanji_text) == 1:
        return None

    ### spelling of the kanji

    furigana = reading_column_child.find_element(by = By.CLASS_NAME, value = "furigana")
    furigana_texts = furigana.find_elements(by = By.CLASS_NAME, value = "kanji")
    
    spelling_text = ""
    for i in range(len(furigana_texts)):
       spelling_text += furigana_texts[i].text
 
    #  Right column 

    ## meaning data

    meaning_column = concept.find_element(by = By.CLASS_NAME, value = "concept_light-meanings")

    meanings_wrapper = meaning_column.find_element(by = By.CLASS_NAME, value = "meanings-wrapper")

    meanings = meanings_wrapper.find_elements(by = By.CLASS_NAME, value = "meaning-wrapper")

    first_meaning = meanings[0].find_element(by = By.CLASS_NAME, value = "meaning-definition")

    first_meaning_child = first_meaning.find_element(by = By.CLASS_NAME, value ="meaning-meaning")
    
    meaning_texts = first_meaning_child.text 
    ### Get the first meaning text
    meaning_text = meaning_texts.split(";")[0]

    # Search for the radicals of the kanji_text in the original dataset

    radicals = ""
    ## Going trough every kanji
    for kanji in kanji_text:
        ### Search kanji
        kanji_row = kanjies_and_meanings[kanjies_and_meanings["Kanji"] == kanji]
        ### Get the meaning
        if kanji_row.empty:
            continue
        word = kanji_row.iloc[0, 1]
        ### Words that have more than 1 meaning, only get the first one
        if len(word.split(",")) > 1: 
            word = word.split(",")[0]
        radicals += "%s + " % word

    ### Quit the last ", " in radicals
    radicals = radicals[:-3] 

    info_row = [kanji_text, meaning_text, radicals, spelling_text]

    return info_row

# Vocabulary that is being redacted from kanjies
start_from_certain_kanji = False

## Verifies if the code stop and start from the last kanji printed
## If it so, the variable 'start_from_certain_kanji' has to be true
## and the 'last_kanji' variable is the last kanji printed

if start_from_certain_kanji == True:
    last_kanji = ""
    start_idx = 0
    start_idx = kanjies_and_data.index[kanjies_and_data['Kanji'] == last_kanji].tolist()[0]

    kanjies_symbols = kanjies_and_meanings.iloc[start_idx:, 0]
else:
    kanjies_symbols = kanjies_and_meanings.iloc[:, 0]


 
for kanji in kanjies_symbols:
    print(kanji)

    # Vocabulary associated with a single kanji

    ## Vocabulary learned until now
    vocabulary_data = pd.read_csv("../kanjgetting/vocabulary.csv")

    # array with the specific kanji vocabulary information
    specific_vocabulary = []

    # Search kanji
    search_kanji(kanji)
    vocabulary_in_page = True

    while vocabulary_in_page == True:
        vocabulary_in_page = False
        concept_column = driver.find_element(by = By.CLASS_NAME, value= "concepts")

        concepts = concept_column.find_elements(by = By.CLASS_NAME, value= "concept_light")

        ### Loop for every concept in a single page
        for concept in concepts:
            # Save information in the new csv 
            
            info_row = get_information(concept)
            if info_row != None:
                specific_vocabulary.append(info_row)
                vocabulary_in_page = True

        ### Click to go to another page
        new_page = driver.find_elements(by = By.CLASS_NAME, value = "more")
        #### Verify if there is another page
        if len(new_page) < 1:
            break
        
        if vocabulary_in_page == True:
            new_page[0].click()

    # saving information

    ## New vocabulary

    ### Saving the vocabulary of a single kanji
    kanji_vocabulary = pd.DataFrame(specific_vocabulary, columns = ["Kanji", "Meaning", "Radicals", "Sound"])


    ### adding the vocabulary to the greater dataset
    if vocabulary_data.empty == True:
        new_vocabulary_data = kanji_vocabulary
    else:
        new_vocabulary_data = pd.concat([vocabulary_data, kanji_vocabulary])

    ### Vocabulary added
 
    new_vocabulary_data.to_csv("vocabulary.csv", columns = ["Kanji", "Meaning", "Radicals", "Sound"], index = False)


driver.quit()