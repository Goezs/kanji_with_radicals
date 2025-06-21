Welcome !!

One form to put to work the python code is.

1. Open google colab

2. Open a new notebook

3. (Optional) Create a text code cell

   There copy the code "# Your number of kanjies you have learn are: 0"

   # The idea is that in the right part, How much kanjies or symbols have been learned is descripted
   # It is manually... Sooooo..... just sum to the last number the quantity learned today !

5. Create the second text code cell. Yes, there is a second (and possibly a third one)

  There copy the code "## Launch effects"

6. Create a normal code cell

   There copy the code :

  (A little late, but in any code don't copy the quatiation marks '"')

  
  "
  
   !git clone https://github.com/Goezs/kanji_with_radicals
  !cp "/content/kanji_with_radicals/JP_FONTS_test/static/NotoSansJP-Regular.ttf" "/usr/share/fonts/truetype/humor-sans"
  from kanji_with_radicals import kanji_anki
  
  "
  
8.  Create another normal code cell
   
  There copy the code :

  "
  particles_box = kanji_anki.initiate_game()
  "

9.  Create THE THIRD text code cell.

    There copy the code "## The matter"

10.  Create another normal code cell
   
  There copy the code :

  "
  particles_box.make_round(left_symbols = True)
  "

11.  Create another normal code cell
   
  There copy the code :

  "
  particles_box.solution
  "

Explication on how to run all:


0. (If you are on colab) Connect to the colab runner of python code, is on the right above part

1. Run the first line

2. The second has almost all the explanations things so....



















3. Run the THIRD line for SHOWING THE SYMBOL.

  There are some parameters, you can use here (Inside the "()", copy these lines):

  "left_symbols = True, " : Says how much symbols are left to finish

  "loading_square = True, " : In the right bottom part shows a constructing square by each run of this line


4. Run the LAST line to see SOLUTION.


   
