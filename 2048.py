import random
from pprint import pprint

class Game:
    def __init__(self):
        
        self.board_width = 4
        self.board_height = 4
        self.board  = [[0 for _j in range(self.board_width)] for _i in range(self.board_height)]
        self.game_loop()
    
    def print_board(self):
        for i in range(self.board_height):
            for j in range(self.board_width):
                print(self.board[i][j], end=" ")
            print()

    def ask_move(self):
        possible_moves = "wasd"
        print("you can quit with q")
        while True:
            move = input("move [w, a, s, d]> ")
            if move == "q":
                exit()
            if move not in possible_moves:
                print("not a possible move")
                continue
            return move
        
    def get_empty_indexes(self):
        empty_indexes = []
        for i, line in enumerate(self.board):
            for j, val in enumerate(line):
                if not val:
                    empty_indexes.append([i, j])
        return empty_indexes
    
    # adds a random 2 to the board
    def add2(self):
        empty_indexes = self.get_empty_indexes()
        if len(empty_indexes) > 0:
            random_empty = random.choice(empty_indexes)
            i, j = random_empty
            self.board[i][j] = 2
        
    def add_zeros_back(self, target_row_or_col, append):
        while len(target_row_or_col) < self.board_height:
            if append:
                target_row_or_col.append(0)
            else:
                target_row_or_col = [0] + target_row_or_col 
        return target_row_or_col

    def sum_numbers(self, col_or_row):
        # add equal numbers together
        for k in range(len(col_or_row) - 1):
            if col_or_row[k] == col_or_row[k + 1]:
                col_or_row[k + 1] = col_or_row[k] + col_or_row[k + 1]
                col_or_row[k] = 0
    
    def remove_zeroes(self, col_or_row):
        new = []
        for e in col_or_row:
            if e:
                new.append(e)
        return new

    def handle_move(self, move):
        # possible moves are  w a s d for up, left, down, right
        # board looks like this
        # 0 0 0 0
        # 0 2 0 0
        # 0 2 0 0
        # 0 0 0 0

        moving_vertical = False
        moving_up = False
        moving_right = False
        if move == "w":
            moving_vertical = True
            moving_up = True

        # if move == "a":
        #     pass

        if move == "s":
            moving_vertical = True
        #   moving_right_or_up = False
        if move == "d":
            moving_right = True
        
        # algorithm
        # iterate over the board until i find a number
        # then isolate vertical/horizontal axis (row or columns)
        # remove zeros
        # add equal numbers together following moving_right_or_up direction
        # add zeros back (prepend or append)
        new_board = self.board.copy()
        if moving_vertical:
            columns = []
            for i in range(self.board_width):
                column = [] # 
                for j in range(self.board_height):
                    value = self.board[j][i]
                    if value:
                        column.append(value)

                self.sum_numbers(column)
                column = self.remove_zeroes(column) # sum numbers method adds when 2 numbers are added zeroes
                # append or prepend zeros
                column = self.add_zeros_back(column, moving_up)
                columns.append(column)

            # copy the columns into the new board
            for i, column in enumerate(columns):
                for j, value in enumerate(column):
                    new_board[j][i] = value
        else:
            for i in range(self.board_height):
                row = self.board[i]
                row = self.remove_zeroes(row)
                print(f"row i after removing zeroes: {i}; {row}")
                self.sum_numbers(row)
                print(f"row i: {i} after sum; {row}")
                row = self.remove_zeroes(row)
                row = self.add_zeros_back(row, not moving_right)
                self.board[i] = row

    def game_loop(self):
        while True:
            self.add2()
            self.print_board()
            # handle input
            move = self.ask_move()
            self.handle_move(move)

if __name__ == "__main__":
    Game()