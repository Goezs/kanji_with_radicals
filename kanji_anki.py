import matplotlib.pyplot as plt
import matplotlib
import matplotlib.font_manager as fm
import random
import numpy.random as rnd
from numpy import array, linspace


plt.style.use("dark_background")
font_files = fm.findSystemFonts()

for font_file in font_files:
  fm.fontManager.addfont(font_file)

font_name = "Noto Sans JP"
matplotlib.rcParams['font.family'] = font_name

def initiate_game():
  """Gets the params to create a KanjiBox and return it to the user"""
  lvl = get_lvl()
  n_rad = get_rad()
  random_state = get_random_state()
  skip = get_skip(random_state)

  kanji_box = KanjiBox(lvl, filter = n_rad, random_state = random_state,
                       skip_kanjies = skip)
  kanji_box.get_kanji

  return kanji_box

def get_lvl():
  """Asks the user a method to question and show the solutions of the kanjies"""
  question_0 = "0: All in one"
  question_1 = "1: What is the kanji and meaning?"
  question_2 = "2: What is the use description?"
  question_3 = "3: Give the sound of the kanji"

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
  """Asks the user the number of radicals that will have the kanjies"""
  answer = input("You want to filter kanjies based on radicals? y/n: ")
  if answer == "y":
    print("\nRadicals explanations: \n")
    print("Filter on number 1: Radicals (Some are also kanjies).")
    print("Filter on number 2: Kanjies made with radicals.")
    print("Filter on number 3: Kanjies made with kanjies of filter 2.")
    print("Filter on number 4: Kanjies made with kanjies of filter 3.\n")
    ########## FILTER 5
    print("Filter on number 5: Vocabulary made based on all kanjies.\n")

    n_rad = int(input("\nradicals to have: "))
    available_nums = range(0, 6) ########## If nothing selected is 5
    while n_rad not in available_nums:
       n_rad = int(input("Introduce an available number of radicals: "))
    return n_rad
  else:
    return 0 ########## If nothing selected is 5

def get_random_state():
  """Asks the user what will be the timeline of sucecions of kanjies"""
  answer = input("Do you want to set a specific random state? y/n: ")
  if answer == "y":
    random_state = int(input("\nRandom state (0 is not valid): "))
    return random_state
  else:
    return 0

def get_skip(random_state):
  """Asks the user how many kanjies will be skiped"""
  if random_state != 0:
   answer = input("Skip kanjies? y/n: ")
   if answer == "y":
     return 1
  return 0

class Kanji(object):
  """
  Creates objects for a kanji that has:
  Args:
    kanji (str): Symbol of the kanji to show
    Meaning (str): Words in english with the semantic of the kanji
    radicals (str): Words in english with the radicals of the kanji (mnemonics)
    sound (str): In their mayority hiragana with the most used sound
        of the kanji
    ########################################### MODIFICATION
    lvl(int) : Gives a question based on the level selected
    points(int) : Help parameter to create the loading square

  """
  def __init__(self, kanji, meaning, radicals, sound, lvl, points = []):
    self.kanji = kanji
    self.meaning = meaning
    self.radicals = radicals
    self.sound = sound
    self.lvl = lvl
    self.points = points

  @property
  def question(self):
    """
    Given a number returns the correspondent answer
    """
    question_0 = ""
    question_1 = "What is the kanji and sound?"
    question_2 = "What are the radicals and the meaning?"
    question_3 = "Give the sound"

    possible_questions = [question_1, question_2, question_3, question_0]

    return possible_questions[self.lvl]

  ##################################### kanji triangular background
  def show_kanji(self, loading_square):
    """
    Shows the clue of the kanji
    """
    #Plot modifications
    plt.figure(figsize = (10, 4))
    plt.axis("off")
    # The parameters you know
    self.parameter_to_show()

    # Loading square if wanted
    if loading_square == True:
      self.points = self.loading_square

    # The question
    plt.text(0.3 * 3, 0.05 * 3, "%s" % self.question, size = 15)
    plt.show()

  def parameter_to_show(self, center_x: int = 0.25, center_y: int = 0.5,
                     size_title: float = 10, size_parameter : float = 15):
    """
    Texts in the plt the information you know based on the level
    """
    # Limit on y axis
    plt.ylim(top = 0.85, bottom = 0)
    plt.xlim(right = 1, left = 0)

    # Arrangement space neccesary for more than 1 character showing
    lenght_kanji = len(self.kanji) - 1
    arrangement_space = lenght_kanji * 0.09

    if abs(self.lvl) == 1:
      # First clue

      ###########################

      plt.text(center_x + 0.12 - arrangement_space, center_y - 0.20, "%s" % self.kanji,
               size = size_parameter + 100)

    elif self.lvl == 0:
      # First clue
      plt.text(center_x + 0.04, center_y, "%s" % self.meaning,
               size = size_parameter + 25)

    else:
      # First clue
      plt.text(center_x - 0.05, center_y + 0.15, "kanji",
               size = size_title + 15)

      ###########################

      plt.text(center_x - arrangement_space, center_y - 0.10, "%s" % self.kanji,
               size = size_parameter + 20)
      # Second clue
      plt.text(center_x + 0.25, center_y + 0.15, "meaning",
               size = size_title + 15)
      plt.text(center_x + 0.30, center_y - 0.10, "%s" % self.meaning,
               size = size_parameter + 20)

  @property
  def show_answer(self):
    """Plots the answer to the question in a plot"""
    print("kanji chars: ", self.kanji)
    # Plot modifications
    plt.figure(figsize = (10, 4))
    plt.axis("off")

    # Plot text
    self.answer_to_show()

    plt.show()

  def answer_to_show(self, center_x: int = 0.5, center_y: int = 0.5,
                     size_title: float = 20, size_answer : float = 15):
    """
    Decides what answer to show based on the lvl selected
    """

    # Arrangament for more than 1 character and for lines
    lenght_kanji = len(self.kanji) - 1
    arrangement_space = lenght_kanji * 0.06


    breath_space = 0.10 + arrangement_space
    const_y = 0.87

    # Upper left line
    x0  = linspace(0, center_x - breath_space)
    y0 = [const_y for i in range(len(x0))]

    # Upper right line
    x1  = linspace(center_x + breath_space, 1)
    y1 = [const_y for i in range(len(x1))]

    plt.ylim(top = 1)

    # Plot lines with white color
    plt.plot(x0, y0, c = "w")
    plt.plot(x1, y1, c = "w")

    # Print the kanji
    plt.text(center_x - 0.05 - arrangement_space, center_y + 0.25, self.kanji,
             size = size_title + 40)

    if self.lvl == -1:
      # Answer 1
      plt.text(center_x - 0.4, center_y + 0.15, "Meaning", size = size_title)
      plt.text(center_x - 0.4, center_y, self.meaning, size = size_answer)
      # Answer 2
      plt.text(center_x + 0.25, center_y + 0.15, "Sound", size = size_title)
      plt.text(center_x + 0.25, center_y, self.sound, size = size_answer)
      # Answer 3
      plt.text(center_x - 0.05, center_y - 0.30, "Radical(s)",
               size = size_title)
      plt.text(center_x - 0.05, center_y - 0.45, self.radicals,
               size = size_answer)

    elif self.lvl == 1:
      # Answer 1
      plt.text(center_x - 0.4, center_y, "Radicals", size = size_title + 5)
      plt.text(center_x - 0.4, center_y - 0.15, self.radicals,
               size = size_answer)
      # Answer 2
      plt.text(center_x + 0.2, center_y, "Meaning", size = size_title + 5)
      plt.text(center_x + 0.2, center_y - 0.15, self.meaning,
               size = size_answer)

    else:
      # Answer 1
      plt.text(center_x - 0.05, center_y - 0.2, self.sound,
               size = size_answer + 30)

  @property
  def loading_square(self):
      """
      Plots lines that will form a square the more they are drawn.

      returns:
        points [array of tuple of ints]: points but one more than last time.
      """
      points = self.points

      plt.style.use("dark_background")

      if points == []:
        for i in range(2):
          axis_choice = rnd.randint(2)
          side_choice = rnd.randint(2)
          if axis_choice == 0:
            x = side_choice
            y = rnd.rand()
          else:
            y = side_choice
            x = rnd.rand()
          points.append([x, y])
      else:
        axis_choice = rnd.randint(2)
        side_choice = rnd.randint(2)
        if axis_choice == 0:
          x = side_choice
          y = rnd.rand()
        else:
          y = side_choice
          x = rnd.rand()
        points.append([x, y])

      plot_points = array(points)
      # Plot coordinates
      plt.plot(array(plot_points)[:,0] / 10 + 0.9,
              array(plot_points)[:,1] / 5, c = "w")

      return points


class KanjiBox(object):
  """
  Creates a boc with the kanjies that the user wants to have.
  Args:
    lvl (int): How will be ilustrated the rounds and solutions [0, 3]
    ##################################### Kanjies rad 5 [1, 5]
    filter (int): Filters the kanjies based on the radicals [1, 5]
    random_state (int): The timeline of a sucecions of kanjies [-inf, inf]
    skip kanjies (int): How many kanjies will be skiped
            (cannot be higher than the kanjies total kanjies in a filter )
  """
  def __init__(self, lvl, filter = 0, kanji = [], actual_k = "",
               random_state = 0, skip_kanjies = 0, onlyskip = 0):
    self.lvl = lvl
    self.kanji = kanji
    self.filter = filter
    self.actual_k = actual_k
    self.random_state = random_state
    self.skip_kanjies = skip_kanjies

    if random_state != 0:
      random.seed(self.random_state)

  @property
  def bag_of_kanji(self):
    """
    Creates a array of kanjies based on a .csv file
    """
    import urllib
    import csv

    # each one with his own webpage and the vocabulary needed (rad 5, and 1-4)
    if self.filter == 5:
      url = "https://raw.githubusercontent.com/Goezs/kanji_with_radicals/main/kanjgetting/cleared_vocabulary.csv"
    else:
      url = "https://raw.githubusercontent.com/Goezs/kanji_with_radicals/refs/heads/main/Kanji.csv"

    webpage = urllib.request.urlopen(url)

    data = csv.reader(webpage.read().decode('utf-8'),)

    raw_kanji = []
    row = []
    word = ""

    for line in data:
      if len(line) < 1:
        row.append(word)
        if self.filter == 5:
          if len(row) != 1:
            raw_kanji.append(row[1:])
        else:
          raw_kanji.append(row)
        row = []
        word = ""
        continue
      elif len(line) > 1:
        row.append(word)
        word = ""
        continue
      word = word + line[0]

    webpage.close()

    return raw_kanji[1:]

  def kanjilizer(self, kanji):
    """
    Converts an array of 5 elements to a Kanji
    """
    kanji, meaning, radicals, sound = kanji

    kanji = Kanji(kanji, meaning, radicals, sound,
                        self.lvl)
    return kanji

  @property
  def random_p(self):
    """
    Gets a random kanji from a list of kanji based on a funnel(position)
        and a caegory of that position
    """

    try:
      p_idx = random.choice(range(len(self.kanji)))
    except IndexError:
      if self.random_state == 0:
        message = "You end the filter %s, ニズ !" % self.filter
      else:
        message = "You end the filter %s in the %s timeline" % (self.filter,
                        self.random_state)

      raise ValueError(message)

    p = self.kanji.pop(p_idx)

    return p


  @property
  def get_kanji(self):
    """
    Fills the kanji list with Kanji objects based on a bag of kanji
    """
    kanji_box = self.bag_of_kanji
    all_kanjies = []
    for k in kanji_box:
      all_kanjies.append(self.kanjilizer(k))
    # Filter kanjies
    self.kanji = self.filter_kanji(all_kanjies)
    self.skips

  def filter_kanji(self, kanjies):
    """
    Filters the kanji based on the number of radicals that they have
    ######## 0 is not default but 5
    The 0 will be interpretated has all the kanjies
    """

    # Make different argumentations for each bag of kanjies
    if self.filter == 5:
      return kanjies

    good_kanjies = []
    for i in kanjies:
      radicals = i.radicals
      radicals = radicals.replace(" ", "")

      if ("#" in radicals) and (self.filter == 4):
        i.radicals = i.radicals[:-2]
        good_kanjies.append(i)
        continue

      if ("*" in radicals) and (self.filter == 3):
        i.radicals = i.radicals[:-1]
        good_kanjies.append(i)
        continue

      list_of_rad = radicals.split(sep = "+")
      n_rads = len(list_of_rad)
      if (n_rads == 1) and (self.filter == 1):
        good_kanjies.append(i)
        continue

      elif (n_rads > 1) and ("*" not in list_of_rad[-1]) and self.filter == 2:
        good_kanjies.append(i)


    return good_kanjies

  def make_round(self, left_kanjies = False, loading_square = False):
    """Sets a new kanji to be tested and gives the left kanjies if is true"""
    kanji = self.random_p
    # Optional parameters

    print("Número de kanjies que faltan: ",
          len(self.kanji)) if left_kanjies == True else None

    # Kanji showing
    kanji.show_kanji(loading_square)
    self.actual_k = kanji

  @property
  def solution(self):
    """Shows the solution of the kanji if the user has started a round"""
    if self.actual_k == "":
      return "Start a round to show a solution"
    self.actual_k.show_answer

  @property
  def skips(self):
    """Make a skip of kanjies until the number that is given"""
    if self.skip_kanjies == True:
      skips = int(input("\nKanjies to skip: "))
      available_nums = range(0, len(self.kanji) - 2)

      while skips not in available_nums:
        skips = int(input("\nThat's not a number possible of days to skip: "))
      only_skips = input("\nDo you want to only have the skipped kanjies but randomized? y/n: ")
      if only_skips == "y":
        new_kanjies = []
        for i in range(skips):
          new_kanjies.append(self.random_p)
        self.kanji = new_kanjies
        self.random_state = 0
      else:
        for i in range(skips):
          self.random_p
