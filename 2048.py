from enum import Enum
from pprint import pprint
import random 


class Position:
    x: int
    y: int
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

class BoardSquare:
    def __init__(self) -> None:
        self.is_empty = True
        self.value = 0

    """
    Returns: True if the square is empty and False if not
    """
    def is_empty(self) -> bool:
        return self.is_empty
    
class Board:
    def __init__(self, w: int=4, h: int=4):
        self.w = w
        self.h = h
        self.board = [[BoardSquare() for _y in range(w)] for _x in range(h)]
    
    """
    Returns: a list containing the indexes to empty squares
    """
    def get_empty_squares(self) -> list[int]:
        empty_indexes = []
        for i, layer in enumerate(self.board):
            for j, square in enumerate(layer):
                if square.is_empty():
                    empty_indexes.append([i, j])

        return empty_indexes
    
    """
    Description: sets the square at param:pos to param:value
    Args: pos for position (index x, y) and value
    """
    def set_square(self, pos: Position, value: int) -> None:
        self.board[pos.y][pos.x].value = value

    """
    Returns the value at param:pos
    """
    def get(self, pos: Position):
        return self.board[pos.y][pos.x].value

class Game:
    def __init__(self):
        self.board = Board()
        self.print_welcome()
        self.game_loop()

    """
    Description: prints welcome message
    """
    def print_welcome(self):
        print("Welcome to 2048.py")
        print("write l for left, r for right, u for up and d for down")
        print("Have fun!")
        print()
        print()

    """
    Description: adds a "2" to the board at a random empty position
    """
    def add_random2(self):
        empty_squares = self.board.get_empty_squares()
        pos = random.choice(empty_squares)
        self.board.set_square(pos, 2)

    """
    Description: prints the board to the console
    """
    def print_board(self):
        for y in range(self.board.h):
            for x in range(self.board.w):
                value = self.board.get(Position(x, y))
                print(value, end=" "*(5 - len(str(value))))
            print()
            print()
            print()

    """
    Description: handles player input
    Returns: valid player input (r/l/u/d)
    """
    def handle_input(self):
        while True:
            in_ = input("(l/r/u/d)>")
            moves = ["l", "r", "u", "d"]
            for move in moves:
                if move == in_:
                    return in_
            print("please input only valid moves")

    """
    Description: moves the squares based on the player input (up, down, left, right) and adds
    same value squares together
    """
    def move_squares(self, direction: str):

        delta_pos = []
        if direction == "l":
            delta_pos = [0, 1]
        elif direction == "r":
            delta_pos =  [0, -1]
        elif direction == "u":
            delta_pos = [-1, 0]
        elif direction == "d":
            delta_pos = [1, 0]
        
        


    """
    Description: game loop that handles input and output and contains
    the game logic
    """
    def game_loop(self):
        while True:
            self.print_board()
            player_input = self.handle_input()
            self.move_squares()
        
        
if __name__ == "__main__":
    game = Game()
    
