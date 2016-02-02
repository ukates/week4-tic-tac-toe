#Derrick Cates

def printBoard(board):
    print()
    print()
    print('L M R') #this print will go above the board and give a letter distinction to the column for the user. 
    print()
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'] + '  top') # I added top, mid and low to the board so that the user knows how type in their selection. 
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'] + '  mid')
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'] + '  low')
    print()
    print()
    print('Make a selection by typing either top, mid, or low follwed by "-" and the capital letter that matches your column selection:') #this is just a discription of how to make a selection on the board. 
    print()
    # TO DO #################################################################    # Write code in this function that prints the game board.               #
    # The code in this function should only print, the user should NOT      #
    # interact with this function in any way.                               #
    #                                                                       #
    # Hint: you can follow the same process that was done in the textbook.  #
    #########################################################################

def checkWinner(board, player):    
    print('Checking if ' + player + ' is a winner...')

#when the x or the o user make a selection that matches with these different outcomes this function will return True for use in def startgame(), if the statement doesnt return true the game will continue to ask for selections. 
    return((board['top-L'] == player and board['top-M'] == player and board['top-R'] == player) or #These are the different outcomes that can happen during the course of the game. straight across all rows, straight down all columns, and diagonal left or right. 
           (board['mid-L'] == player and board['mid-M'] == player and board['mid-R'] == player) or
           (board['low-L'] == player and board['low-M'] == player and board['low-R'] == player) or
           (board['top-L'] == player and board['mid-L'] == player and board['low-L'] == player) or
           (board['top-M'] == player and board['mid-M'] == player and board['low-M'] == player) or
           (board['top-R'] == player and board['mid-R'] == player and board['low-R'] == player) or
           (board['top-L'] == player and board['mid-M'] == player and board['low-R'] == player) or
           (board['top-R'] == player and board['mid-M'] == player and board['low-L'] == player))
    

    # TO DO #################################################################
    # Write code in this function that checks the tic-tac-toe board          #
    # to determine if the player stored in variable 'player' currently      #
    # has a winning position on the board.                                  #
    # This function should return True if the player specified in           #
    # variable 'player' has won. The function should return False           #
    # if the player in the variable 'player' has not won.                   #
    #########################################################################
    
    
def startGame(startingPlayer, board):
    # TO DO #################################################################
    # Add comments to each line in this function to describe what           #
    # is happening. You do not need to modify any of the Python code        #
    #########################################################################

    turn = startingPlayer
    for i in range(9): # this is a 'for loop' this will loop the game in the amount of times called in the range, in this case 9.  The game will continue to print the board and ask the user for a move until either they have ran out of moves '9 moves' or the checkanswer function returns true ending the game and declaring a winner. 
        printBoard(board) #this calls the print board function, which displays the game board that will include the guesses of either user. 
        print('Turn for ' + turn + '. Move on which space?') # prints text that will display who's turn it is (x or o) and ask which space they would like to choose. 
        move = input() #assigns the users input to the value move. 
        board[move] = turn # takes the users input which is now assigned to move, and places it in the game board to be displayed when it matches the corresponding section.
        if( checkWinner(board, 'X') ): # this gives us an if statment that calls the function checkWinner which determins whether x's choices have matched any of the possible winning outcomes. If checkWinner returns true the loop will break and print that x is the winner. 
            print('X wins!') # if checkWinner returns ture  x wins will print. 
            break #the loop will break and the game will end. 
        elif ( checkWinner(board, 'O') ): #if statement that determines if check winner for x returns false, but checkWinner for O selections returns true. 
            print('O wins!') #if checkWinner function for O selections returns true O Wins will print. 
            break #if O is the winner the loop will break and the game will end. 
    
        if turn == 'X':  # This begins the process of swapping the active player. this is an if statment that asks if the turn is equal to X
            turn = 'O' # if it isnt x's turn then it is O's turn
        else:
            turn = 'X' #if it isnt o's turn then its x's turn. 
        
    printBoard(board) # prints the game board. 
    
