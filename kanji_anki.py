import matplotlib.pyplot as plt
import matplotlib
import matplotlib.font_manager as fm
import random

plt.style.use("dark_background")
font_files = fm.findSystemFonts()

for font_file in font_files:
  fm.fontManager.addfont(font_file)

font_name = "Noto Sans JP"
matplotlib.rcParams['font.family'] = font_name

def initiate_game():
  lvl = get_lvl()
  n_rad = get_rad()
  random_state = get_random_state()
  skip = get_skip(random_state)

  kanji_box = KanjiBox(lvl, filter = n_rad, random_state = random_state,
                       skip_kanjies = skip)
  kanji_box.get_kanji()

  return kanji_box

def get_lvl():
  question_0 = "0: All in one"
  question_1 = "1: What is the kanji and meaning?"
  question_2 = "2: What is the use description?"
  question_3 = "3: Give an example in japanase and the translation in english"

  possible_questions = [question_0, question_1, question_2, question_3]

  print("The difficulties of the game are: ")
  for q in possible_questions:
    print(q)
  lvl = int(input("What difficulty you want? "))
  possibly_levels = range(0, 4)
  while lvl not in possibly_levels:
    lvl = int(input("That's not a difficulty elect one available: "))

  # Convert the [1, 3] into [0, 2]
  lvl = lvl - 1 #######
  return lvl

def get_rad():
  answer = input("You want to filter kanji based on her number of radicals? y/n: ")
  if answer == "y":
    print("Radicals go between 1 to 3, 0 if you want any number of radicals")
    n_rad = int(input("\nradicals to have: "))
    available_nums = range(0, 4)
    while n_rad not in available_nums:
       n_rad = int(input("Introduce an avaible number of radicals: "))
    return n_rad
  else:
    return 0

def get_random_state():
  answer = input("Do you want to set a specific random state? y/n: ")
  if answer == "y":
    random_state = int(input("\nRandom state (0 is not valid): "))
    return random_state
  else:
    return 0

def get_skip(random_state):
  if random_state != 0:
   answer = input("Skip kanjies? y/n: ")
   if answer == "y":
     return 1
  return 0

class Kanji(object):
  def __init__(self, kanji, meaning, radicals, sound, lvl):
    self.kanji = kanji
    self.meaning = meaning
    self.radicals = radicals
    self.sound = sound
    self.lvl = lvl

  def question(self):
    """
    Given a number returns the correspondent andswer
    """
    question_0 = ""
    question_1 = "What is the kanji and sound?"
    question_2 = "What are the radicals and the meaning?"
    question_3 = "Give the sound"

    possible_questions = [question_1, question_2, question_3, question_0,]

    return possible_questions[self.lvl]

  def show_kanji(self):
    """
    Shows the clue of the kanji
    """
    #Plot modifications
    plt.figure(figsize = (10, 4))
    plt.axis("off")
    # The parameters you know
    self.parameter_to_show()

    # The question
    plt.text(0.3, 0.05, "%s" % self.question(), size = 12)
    plt.show()

  def parameter_to_show(self, center_x: int = 0.25, center_y: int = 0.5,
                     size_title: float = 10, size_parameter : float = 15):
    """
    Texts in the plt the information you know based on the level
    """
    #plt.text(center_x + 0.25, center_y + 0.45, "CLUES", size = size_title + 10)
    if self.lvl == -1:
      # First clue
      plt.text(center_x, center_y, "%s" % self.kanji,
               size = size_parameter + 100)

    elif self.lvl == 0:
      # First clue
      plt.text(center_x, center_y + 0.35, "Meaning:", size = size_title)
      plt.text(center_x, center_y + 0.15, "%s" % self.meaning,
               size = size_parameter)

    elif self.lvl == 1:
      # First clue
      plt.text(center_x, center_y, "%s" % self.kanji,
               size = size_parameter + 90)
    else:
      # First clue
      plt.text(center_x - 0.25, center_y + 0.15, "kanji:",
               size = size_title + 15)
      plt.text(center_x - 0.20, center_y - 0.10, "%s" % self.kanji,
               size = size_parameter + 20)
      # Second clue
      plt.text(center_x + 0.25, center_y + 0.15, "meaning:",
               size = size_title + 15)
      plt.text(center_x + 0.30, center_y - 0.10, "%s" % self.meaning,
               size = size_parameter + 20)


  def show_answer(self):
    """Plots the answer to the question in a plot"""
    print("kanji chars: ", self.kanji)
    # Plot modifications
    plt.figure(figsize = (10, 4))
    plt.axis("off")

    # Plot text
    self.answer_to_show()

    plt.show()

  def answer_to_show(self, center_x: int = 0.1, center_y: int = 0.5,
                     size_title: float = 10, size_answer : float = 15):
    """
    Decides what answer to show based on the lvl selected
    """
    plt.text(center_x + 0.15, center_y + 0.45, "The solution was ...",
             size = size_title + 10)

    if self.lvl == -1:
      # Answer 1

      plt.text(center_x + 0.24, center_y + 0.10, self.meaning, size = size_answer)
      # Answer 2
      plt.text(center_x + 0.15, center_y, self.radicals, size = size_answer)
      # Answer 3
      plt.text(center_x + 0.15, center_y - 0.20, "Sound: ", size = size_title)
      plt.text(center_x + 0.15, center_y - 0.30, self.sound, size = size_answer)

    elif self.lvl == 0:
      # Answer 1
      plt.text(center_x + 0.15, center_y, self.kanji, size = size_answer + 95)
      # Answer 2
      plt.text(center_x + 0.15, center_y - 0.20, "Sound: ", size = size_title)
      plt.text(center_x + 0.15, center_y - 0.30, self.sound, size = size_answer)
    elif self.lvl == 1:
      # Answer 1
      plt.text(center_x, center_y, self.radicals, size = size_answer)
      # Answer 2
      plt.text(center_x + 0.24, center_y, self.meaning, size = size_answer)
    else:
      # Answer 1
      plt.text(center_x + 0.15, center_y - 0.20, "Sound: ", size = size_title)
      plt.text(center_x + 0.15, center_y - 0.30, self.sound, size = size_answer)

class KanjiBox(object):
  def __init__(self, lvl, filter = 0, kanji = [], actual_k = "",
               random_state = 0, skip_kanjies = 0):
    self.lvl = lvl
    self.kanji = kanji
    self.filter = filter
    self.actual_k = actual_k
    self.random_state = random_state
    self.skip_kanjies = skip_kanjies

  def bag_of_kanji(self):
    """
    Creates a array of the kanji
    """
    import urllib
    import csv

    webpage = urllib.request.urlopen("https://raw.githubusercontent.com/Goezs/kanji_with_radicals/main/Kanji.csv")

    data = csv.reader(webpage.read().decode('utf-8'))

    raw_kanji = []
    row = []
    word = ""

    for line in data:
      for i in range(51):
        continue
      if len(line) < 1:
        row.append(word)
        raw_kanji.append(row)
        row = []
        word = ""
        continue
      elif len(line) > 1:
        row.append(word)
        word = ""
        continue
      word = word + line[0]

    for line in data:
      for i in range(51):
        continue
      if len(line) == 2:
        row.append(word)
        word = ""
        continue
      if line == []:
        raw_kanji.append(row)
        row = []
        continue
      word = word + line[0]

    return raw_kanji[1:]

  def kanjilizer(self, kanji):
    """
    Converts an array of 5 elements to a Kanji
    """
    kanji, meaning, radicals, sound = kanji

    kanji = Kanji(kanji, meaning, radicals, sound,
                        self.lvl)
    return kanji

  def random_p(self):
    """
    Gets a random kanji from a list of kanji based on a funnel(position)
        and a caegory of that position
    """
    if self.random_state == 0:
      p_idx = random.choice(range(len(self.kanji)))
      p = self.kanji.pop(p_idx)
    else:
      random.seed(self.random_state)
      p_idx = random.choice(range(len(self.kanji)))
      p = self.kanji.pop(p_idx)

    return p

  def get_kanji(self):
    """
    Fills the kanji list with Kanji objects based on a bag of kanji
    """
    kanji_box = self.bag_of_kanji()
    all_kanjies = []
    for k in kanji_box:
      all_kanjies.append(self.kanjilizer(k))
    # Filter kanjies
    self.kanji = self.filter_kanji(all_kanjies)
    self.skips()

  def filter_kanji(self, kanjies):
    if self.filter == 0:
      return kanjies
    good_kanjies = []
    for i in kanjies:
      radicals = i.radicals
      radicals = radicals.replace(" ", "")
      list_of_rad = radicals.split(sep = "+")
      if len(list_of_rad) == self.filter:
        good_kanjies.append(i)
    return good_kanjies

  def make_round(self, left_kanjies = False):
    kanji = self.random_p()
    print("Número de kanjies que faltan: ", len(self.kanji)) if left_kanjies == True else None
    kanji.show_kanji()
    self.actual_k = kanji

  def solution(self):
    if self.actual_k == "":
      return "Start a round to show a solution"
    self.actual_k.show_answer()
  
  def skips(self):
    if self.skip_kanjies == True:
      skips = int(input("\nKanjies to skip: "))
      available_nums = range(0, len(self.kanji) - 2)
      while skips not in available_nums:
        skips = int(input("\nThat's not a number possible of days to skip: "))
      for i in range(skips):
        self.random_p()
