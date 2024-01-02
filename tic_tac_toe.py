from random import *

board = [
  [1,2,3],
  [4,5,6],
  [7,8,9]]

def display_board(board):
  
  a,b,c,d,e,f,g,h,i = (board[0][0],board[0][1],board[0][2],
                       board[1][0],board[1][1],board[1][2],
                       board[2][0],board[2][1],board[2][2])

  
  top = "+-------" *3
  side = "|       " * 4
  
  # squares 1,2,3
  print(top,"+",sep="")
  print(side)
  print("|", a ,"|", b ,"|", c ,"|",sep="   ")
  print(side)
  print(top,"+",sep="")
  
  # squares 4,5,6
  print(side)
  print("|", d ,"|", e ,"|", f ,"|",sep="   ")
  print(side)
  print(top,"+",sep="")
  
  # squares 7,8,9
  print(side)
  print("|", g ,"|", h ,"|", i ,"|",sep="   ")
  print(side)
  print(top,"+",sep="")

    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,

  move = 0
  while True:
    try:
      move = int(input("Enter your move: "))

      # checks if move is in row 0
      if move <=3:
        row = 0
        column = board[0].index(move)
        break
      # checks if move is in row 1
      elif move <= 6:
        row = 1
        column = board[1].index(move)
        break
      # checks if move is in row 2
      elif move <=9:
        row = 2
        column = board[2].index(move)
        break
    # prevents error message
    except:
      print("Already Occupied -- Try Again")

  # sets the board with the user's move
  board[row][column] = "\033[1m"+"O"+"\033[0m"
  
    # checks the input, and updates the board according to the user's decision.
  
def make_list_of_free_fields(board):

  nor_board = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
  ]
  
  freespaces = []
  for m in range(3):
    for n in range(3):
      if board[m][n] == nor_board[m][n]:
        tuple = m,n
        freespaces.append(tuple)

  return freespaces
  #print(freespaces)

    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.

def victory_for(board, plays,length):
    # The function analyzes the board's status in order to check if 
  y = "\033[1m"+"X"+"\033[0m"
  z = "\033[1m"+"O"+"\033[0m"

  # user won (across)
  if board[0][0] == z and board[0][1] == z and board[0][2] == z:
    plays = 2
    #print("You Win!1")
  elif board[1][0] == z and board[1][1] == z and board[1][2] == z:
    plays = 2
    #print("You Win!2")
  elif board[2][0] == z and board[2][1] == z and board[2][2] == z:
    plays = 2
    #print("You Win!3")

  # user wins (down)
  elif board[0][0] == z and board[1][0] == z and board[2][0] == z:
    plays = 2
    #print("You Win!4")
  elif board[0][1] == z and board[1][1] == z and board[2][1] == z:
    plays = 2
    #print("You Win!5")
  elif board[0][2] == z and board[1][2] == z and board[2][2] == z:
    plays = 2
    #print("You Win!6")
    
  # user wins (diagonal)
  elif board[0][0] == z and board[1][1] == z and board[2][2] == z:
    plays = 2
    #print('You Win!7')
  elif board[0][2] == z and board[1][1] == z and board[2][0] == z:
    plays = 2
    #print("You Win!8")

    
  # computer wins (across)
  elif board[0][0] == y and board[0][1] == y and board[0][2] == y:
    plays = 3
    #print("You Lost1")
  elif board[1][0] == y and board[1][1] == y and board[1][2] == y:
    plays = 3
    #print("You Lost2")
  elif board[2][0] == y and board[2][1] == y and board[2][2] == y:
    plays = 3
    #print("You Lost3")

  # computer wins (down)
  elif board[0][0] == y and board[1][0] == y and board[2][0] == y:
    plays = 3
    #print("You Lost4")
  elif board[0][1] == y and board[1][1] == y and board[2][1] == y:
    plays = 3
    #print("You Lost5")
  elif board[0][2] == y and board[1][2] == y and board[2][2] == y:
    plays = 3
    #print("You Lost6")

  # computer wins (diagonal)
  elif board[0][0] == y and board[1][1] == y and board[2][2] == y:
    plays = 3
    #print('You Lost7')
  elif board[0][2] == y and board[1][1] == y and board[2][0] == y:
    plays = 3
    #print("You Lost8")
    
  if plays == 0 and length == 0:
    plays = 4
    
    # the player using 'O's or 'X's has won the game
  return plays

def draw_move(board,length):
    # The function draws the computer's move and updates the board.
  while length > 0:
    try:
      # random square selected
      move = randrange(1,10)
      # checks if computer move is in row 0
      if move <=3:
        row = 0
        column = board[0].index(move)
        break
      # checks if computer move is in row 1
      elif move <= 6:
        row = 1
        column = board[1].index(move)
        break
      # checks if computer move is in row 2
      elif move <=9:
        row = 2
        column = board[2].index(move)
        break
    # prevents error message
    except:
      None

  # updates board with computer's move
  while True:
    try:
      board[row][column] = "\033[1m"+"X"+"\033[0m"
      break
    except:
      break


plays = 0
length = 1
while plays == 0:
  length = len(make_list_of_free_fields(board))
  display_board(board)
  enter_move(board)
  plays = victory_for(board,plays,length)
  display_board(board)
  length = len(make_list_of_free_fields(board))
  draw_move(board,length)
  plays = victory_for(board,plays,length)

display_board(board)
if plays == 2:
  print("You Won!")
elif plays == 3:
  print("You Lost")
elif plays == 4:
  print("Tie")
