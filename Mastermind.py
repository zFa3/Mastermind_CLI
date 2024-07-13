#!usr/bin/env python3
# zFa3 - Mastermind 

# In this game, you have to try and crack a
# randomly generated passcode. Enter a 5 digit
# number (you can change this) and the colors will
# tell you whether you got the correct number in the
# right place (green), the correct number in the
# wrong place (yellow), or the incorrect number (red)

# you have 10 attemps(you can also change this)  


import random as rd
import sys

class Colors:
    def __init__(self) -> None:
        self.RED = '\033[91m'
        self.YELLOW = '\033[93m'
        self.GREEN = '\033[92m'
        self.PURPLE = '\033[94m'
        self.BLUE = '\033[96m'

        self.All_colors = [self.RED, self.YELLOW, self.GREEN, self.PURPLE, self.BLUE]

    def PrintColors(self, colorIndex: int, *args):
        print(f"{self.All_colors[colorIndex]}", *args, sep="", end="")

printer = Colors()

attempts = 10
passwordLength = 5
password = [rd.randint(1, 9) for _ in range(passwordLength)]
# the password uses digits 1 through 9
board = [
    [0 for i in range(passwordLength)] for _ in range(attempts)
]

def color(item, column):
    if item == password[column]:
        return 2
    if item in password:
        return 1
    return 0

def print_board(board):
    print("\033c", end = "")
    for i in range(attempts):
        for j in range(passwordLength):
            if board[i][j]:
                printer.PrintColors(color(board[i][j], j), f" {board[i][j]}")
            else:
                printer.PrintColors(4, f"  ")
            printer.PrintColors(4, f"|")
        if i == 0:
            print(" <-- Your most recent guess", end = "")
        printer.PrintColors(4, "\n", "__+" * (passwordLength - 1))
        printer.PrintColors(4, "__|\n")

def inputValidation(playerInput: str):
    try:
        return int(playerInput) in range(1, 10)
    except: return False

for i in range(attempts):
    answer = []
    for j in range(passwordLength):
        try:
            arg = input().split()
            if all([inputValidation(item) for item in arg]) and len(arg) == 5:
                answer = list(map(int, arg)); break
        except: pass
        print("Invalid input")
    board.pop(0)
    board.append(answer)
    print_board(board[::-1])
    if answer == password:
        print("YOU WON!")
        sys.exit()

print("GAME OVER!")
