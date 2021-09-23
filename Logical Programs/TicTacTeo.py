'''
* @Author: Mohammad Fatha.
* @Date: 2021-09-17 20:05  
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-09-17 20:30
* @Title: Tic Tac Teo Game 
'''
import random

class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        """
            Description:
                    This Function is use generate the 3x3 tic tac teo board
                    using 2D array concept
        """ 
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def get_random_first_player(self):
        """
            Description:
                    This function is use to select the person
        """ 
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        """
            Description:
                This function is use to fix the spot of the players
                on the specific positions to play game
        """ 
        self.board[row][col] = player

    def is_player_win(self, player):
        win = None

        n = len(self.board)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def is_board_filled(self):
        """
            Description:
                This function is used to check wheather the board is filled
                or is there any space in it
        """ 
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        """
            Description:
                This is function is use to select play either X or O
        """ 
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        """
            Description:
                This function is used to print tha 3x3 tic tac teo game board

        """ 
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        """
            Description:
                This function is use to start the tic tac teo game
                from this function the other funnctions are called 
        """ 
        self.create_board()

        player = 'X' if self.get_random_first_player() == 1 else 'O'
        while True:
            print(f"Player {player} turn")

            self.show_board()

            # taking user input
            row, col = list(
                map(int, input("Enter row and column numbers to fix spot: ").split()))
            print()

            # fixing the spot
            self.fix_spot(row - 1, col - 1, player)

            # checking whether current player is won or not
            if self.is_player_win(player):
                print(f"Player {player} wins the game!")
                break

            # checking whether the game is draw or not
            if self.is_board_filled():
                print("Match Draw!")
                break

            # swapping the turn
            player = self.swap_player_turn(player)

        # showing the final view of board
        print()
        self.show_board()



# starting the game
if __name__ == '__main__':
    tic_tac_toe = TicTacToe()
    tic_tac_toe.start()
