import random as rd

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
    [i + 1 for i in range(passwordLength)] for _ in range(attempts)
]

def color(item, column):
    if item == password[column]:
        return 2
    if item in password:
        return 1
    return 0

def print_board(board):
    for i in range(attempts):
        for j in range(passwordLength):
            if board[i][j]:
                printer.PrintColors(color(board[i][j], j), f" {board[i][j]}")
            else:
                printer.PrintColors(4, f"  ")
            printer.PrintColors(4, f"|")
        printer.PrintColors(4, "\n", "__+" * (passwordLength - 1))
        printer.PrintColors(4, "__|\n")

def inputValidation(playerInput: str):
    return playerInput.isnumeric() and playerInput in range(1, 10)


print_board(board)
print(password)
