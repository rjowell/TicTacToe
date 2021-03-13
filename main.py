#define a method called "get user input"
#2 params: board player:
#ask the player to input a row number and column number, and check to see if those numbers are between 0 and 2

board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']


def getUserInput(board,player):
  print("Player "+player)
  row = int(input("Enter Row "))
  while row < 0 or row > 2:
    print("Please enter a valid row")
    row = int(input("Enter Row "))
  column = int(input("Enter Column "))
  while column < 0 or column > 2:
    print("Please enter a valid column")
    column = int(input("Enter Column "))

  index = row * 3 + column
  if board[index] != ' ':
    print("That space is already taken")
    getUserInput(board,player)

  #What Do You Need To build Car
  #Glass
  #Wheels
  #Lights
  #Seats
  #A person
  #Windows
  #Car
  
  #Index = row * 3 + column
    #if board[index is not " "
    #print that space is already taken
    #call get user input again
    #else
    #if player is 1:
    #board[index] = "x"
    #else
    #board[index] = "o"

