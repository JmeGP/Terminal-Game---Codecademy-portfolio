#tic-tac-toe.py
##############################
##   ttt TIC - TAC - TOE    ##
##############################
import itertools
import re


#STATIC global variables
ROWS, COLS = (3,3)
BLANK_MOVES = [[ " " for j in range(COLS)] for j in range(ROWS)]
SYMBOLS =('O', 'X')
BOARD_FORMAT ="""
               1     2      3

          1    {}  |  {}  |  {}  
             -----|-----|-----
          2    {}  |  {}  |  {} 
             -----|-----|-----
          3    {}  |  {}  |  {} \n """ 

INPUT_REGEX = "^[123],[123]$"
#DYNAMIC global variables
x_o = BLANK_MOVES.copy()
turn = 0

def get_move(message):
    draw_board()
    location = input(message)
    return location


def play_move(player):
    msg = 'Where do you want to place your {}?\n'.format(player)
    format_error_msg = 'PLAYER {}, Please type a the location of your {} as \'row,col\'.\n\trow and col are numbers between 1 and 3 separated by a comma\n'.format(player,player)
    location_error_msg = 'PLAYER {}, The location you selected is not empty, please enter an empty location to place your {}\n'.format(player, player)
    global x_o


    attempt = 0
    valid_location = False
    input_format = None

  

    #Get and check user input for valid format and valid location
    while (input_format == None or not valid_location):
      if attempt == 0:
         error_msg = msg
      elif input_format == None:
         error_msg = format_error_msg
      elif not valid_location:
         error_msg = location_error_msg
    
      location_str = get_move(error_msg) 
      attempt += 1
      input_format = re.fullmatch(INPUT_REGEX, location_str)
      if (input_format != None):
        row,col = location_str.split(',')
        row, col = (int(row), int(col))
    
        if x_o[row-1][col-1] == " ":
          valid_location = True    


    #Add played move to board
    x_o[row-1][col-1] = player
    print("You played {} at row {} column {}".format(player, row, col))
    draw_board()

    return row, col

def draw_board():
    board = BOARD_FORMAT.format(*(list(itertools.chain.from_iterable(x_o))))
    print(board)

#check grid rows, columns and diagonals for winner
def check_winner():
   winner = (False, None)

   def check_rows():
      for row in range(ROWS):
         if x_o[row][0] == x_o[row][1] and x_o[row][0] == x_o[row][2] and x_o[row][0] in SYMBOLS:
            nonlocal winner
            winner = (True, x_o[row][0])
            break
      return

   def check_cols():
      for col in range(COLS):
        if x_o[0][col] == x_o[1][col] and x_o[0][col] == x_o[2][col] and x_o[0][col] in SYMBOLS:
          nonlocal winner
          winner = (True, x_o[0][col])
          break
      return
   def check_diags():
      if x_o[0][0] == x_o[1][1] and x_o[0][0] == x_o[2][2] and x_o[0][0] in SYMBOLS:
          nonlocal winner
          winner = (True, x_o[0][0])
          return
      if x_o[0][2] == x_o[1][1] and x_o[0][2] == x_o[2][0] and x_o[0][2] in SYMBOLS:
          winner = (True, x_o[0][2])
          return
      return
  
   check_rows()
   if not winner[0]:
      check_cols()
      if not winner[0]:
         check_diags()

   return winner



def play_game():
    welcome = "Welcome to your terminal tic-tac-toe game"
    print(welcome)
    draw_board()
    turn = 0
    game_over = False

  
    while (not game_over):
      turn +=1
      player = SYMBOLS[turn % 2]
      print("Player {}'s turn".format(player))

      #Player whose turn it is plays a move        
      row, col = play_move(player)

      #check grid for winner
      winner = check_winner()

      #if there is a winner, exit the loop/end the game
      if (winner[0] == True):
         print("*****GAME OVER******")
         print("*****PLAYER {} WINS!!".format(winner[1]))
         game_over = True
      
      #if no winner by the 9th turn, end game
      elif turn == ROWS * COLS:
         print("*****GAME OVER******")
         print("****NO WINNER!!*****")
         game_over = True


           
def main():
    play_game()

if __name__ == "__main__":
    main()
