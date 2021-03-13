#Rows and Columns
#User Input
#Condition for when the game ends
#X and O markers
#Players
#Labels for Rows and Columns
#Check how many x's and o's in each row/column
#Check if it's a tie.


# create the array for the board and fill it with empty spaces
#Write a makeBoard function that creates a list called "board" and adds 9 " " chars to it.
def make_board():
    board = []
    for i in range(9):
        board.append(" ")
    return board

# print out the current board in the terminal
def print_board(board):
    print("  0   1   2")
    print("0 {} | {} | {}".format(board[0], board[1], board[2]))
    print("  ---------")
    print("0 {} | {} | {}".format(board[3], board[4], board[5]))
    print("  ---------")
    print("0 {} | {} | {}".format(board[6], board[7], board[8]))
    
# get the current players input, check that it is valid, 
# and add the play to the board

#define a method called "get user input"
#2 params: board player:
#ask the player to input a row number and column number, and check to see if those numbers are between 0 and 2

def get_user_input(board, player):
    print("Player {}".format(player))
    row = int(input("Enter row:  "))
    while (row < 0 or row > 2):
        print("Invalid input.  Please try again.")
        row = int(input("Enter row:  "))
    col = int(input("Enter column:  "))
    while (col < 0 or col > 2):
        print("Invalid input.  Please try again.")
        col = int(input("Enter column:  "))

    index = row * 3 + col
    if (board[index] != " "):
        print("That space is already taken.")
        get_user_input(board, player)
    else:
        if (player == 1):
            board[index] = "x"
        else:
            board[index] = "o"
            
