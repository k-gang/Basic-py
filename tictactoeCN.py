board = [
  ["-", "-", "-"],
  ["-", "-", "-"],
  ["-", "-", "-"]
]

user = True # when true it refers to x, otherwise o
turns = 0

def my_board(board): #function
  for row in board: #look at each row
    for slot in row: #look at each slot
      print(slot+" ", end="")
    print()

def quit(user_choice):
  if user_choice.lower() == "k": 
    print("thanks for playing mate")
    return True
  else: return False


def check_input(user_choice):
  
  if not isnum(user_choice): return False
  user_choice = int(user_choice)
  
  if not bounds(user_choice): return False

  return True

def isnum(user_choice):
  if not user_choice.isnumeric(): 
    print("pls enter only a number")
    return False
  else: return True

def bounds(user_choice):
  if user_choice > 9 or user_choice < 1: 
    print("this number is out of the range")
    return False
  else: return True

def istaken(coords, board):
  row = coords[0]
  col = coords[1]
  if board[row][col] != "-":
    print("EHH your opponent has taken this position")
    return True
  else: return False

def coordinates(user_choice):
  row = int(user_choice / 3) # 0 or 2 divided by3 will give 0th row, 
                             # anything between 3 and 5 will give 1
  col = user_choice
  if col > 2: col = int(col % 3)
  return (row,col)

def add_to_board(coords, board, active_user):
  row = coords[0]
  col = coords[1]
  board[row][col] = active_user

def current_user(user):
  if user: return "x"
  else: return "o"

def iswin(user, board):
  if check_row(user, board): return True
  if check_col(user, board): return True
  if check_diag(user, board): return True
  return False

def check_row(user, board):
  for row in board:
    complete_row = True
    for slot in row:
      if slot != user:
        complete_row = False
        break
    if complete_row: return True
  return False 

def check_col(user, board):
  for col in range(3):
    complete_col = True
    for row in range(3):
      if board[row][col] != user:
        complete_col = False
        break
    if complete_col: return True
  return False

def check_diag(user, board):
  #top left to bottom right
  if board[0][0] == user and board[1][1] == user and board[2][2] == user: return True
  elif board[0][2] == user and board[1][1] == user and board[2][0] == user: return True
  else: return False

while turns < 9:
  active_user = current_user(user)
  my_board(board)
  user_choice = input("enter a position from 1-9 or enter \"k\" to quit:")
  if quit(user_choice): break
  if not check_input(user_choice):
    print("try again.")
    continue
  user_choice = int(user_choice) - 1
  coords = coordinates(user_choice)
  if istaken(coords, board):
    print("try again.")
    continue
  add_to_board(coords, board, active_user)
  if iswin(active_user, board): 
    print(f"{active_user.upper()} won!")
    break
  
  turns += 1
  if turns == 9: print("it's a tie!")
  user = not user