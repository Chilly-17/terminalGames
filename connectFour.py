from termcolor import colored
import time
from specialPrints import cyan_now_print, cyan_later_print
from specialPrints import error_message, cyan_input
print(time.time())

# creating a dictionary of colors that can be used by players
# they will be removed once they are chosen by the player
# WARNING!!! Global dictionary
available_colors = {
    1: "🔵blue",
    2: "🔴red",
    3: "🟡yellow",
    4: "🟢green",
    5: "🟣magenta"
}


file_a = {}
board = {}

# inputs individual cells into the dictionary
# in the file cells range from 6 to 1
for cell in range(6):
    file_a[6 - cell] = "  "

# file range from 1 to 7
for file in range(7):
    board[file + 1] = file_a.copy()


# prints playing board (first all cells are empty)
def print_board():
    print(22 * "_")
    print("|A |B |C |D |E |F |G |")
    for cell in range(6):
        line = "|"
        for file in range(7):
            line += board[file + 1][6 - cell]
            line += "|"
        print(line)
    print(22 * "¯")


# Player class: Functions for both players
# When creating variables you will need a list from the function bellow
# (introduce_players_to_sys)

class Player:

    def __init__(self, player_details: list):
        # takes the first item of the list (player name (str))
        self.name: str = player_details[0]
        # takes the second item of the list (color (str))
        self.color: str = player_details[1][0]
        # will be used for colored text
        self.color_for_text = player_details[1][1:]
        pass

    def player_turn(self, file: int):
        self.file: int = file
        for row in range(6):
            value_of_file: int = ord(self.file) - 96  # a = 1, b = 2...
            if board[value_of_file][row + 1] == "  ":
                board[value_of_file][row + 1] = self.color
                return True
        else:
            error_message("That file is full")

    def choose_file(self):
        print(colored(f"It's {self.name}'s turn!", f"{self.color_for_text}"))
        user_input = input("Input file from A to G: ")
        stored_input = user_input.lower()
        if stored_input in "abcdefg" and len(stored_input) == 1:
            cyan_now_print(f"You have chosen the file {user_input.upper()}")
            return stored_input
        else:
            error_message("Please only enter valid file name!")
            return None

    def win_check(self):
        # check for vertical
        for file in range(1, 8):  # 1 - 7
            for key in range(1, 4):  # 1 - 3
                if (
                    board[file][key] == self.color
                    and board[file][key + 1] == self.color
                    and board[file][key + 2] == self.color
                    and board[file][key + 3] == self.color
                ):
                    print("Vertical win")
                    return True
        # check for horizontal
        for file in range(1, 5):  # 1 - 4 the other the will be the increments
            for row in range(1, 7):  # 1 - 6 == all the rows
                if (
                    board[file][row] == self.color
                    and board[file + 1][row] == self.color
                    and board[file + 2][row] == self.color
                    and board[file + 3][row] == self.color
                ):
                    print("Horizontal win")
                    return True

    def player_win(self, passed_turns: int):
        x = self.color_for_text
        y = "Congratulations"
        print(12 * "🎆")
        time.sleep(0.4)
        print(colored(f"{self.color} {y} {self.name} {self.color}", x))
        time.sleep(0.4)
        print(colored("You won the game in {passed_turns} turns", x))
        time.sleep(0.4)
        print(12 * "🎆")


# Loops while the return is None, can be used for 5 players max
# (max 5 colors in the dictionary)
# the output of introduce will be handled as a list
# The list will be extracted in __init__ of Player class
def introduce_players_to_sys(player_x: str):
    output = []
    player_name: str = cyan_input(f"What is your name {player_x[:-2]}: ")
    length_of_name: int = len(player_name)
    if length_of_name < 2 or length_of_name > 15:
        error_message("Name must be between 2 and 15 characters long")
        return None
    else:
        output.append(player_name)
        cyan_now_print("Choose your color:")
        global available_colors
        for idx in available_colors:
            just_color: str = available_colors[idx][0]
            print(colored(f"{idx}: {just_color}", available_colors[idx][1:]))
        try:
            input_message = "Input the corresponding number: "
            player_color_index: int = int(input(input_message))
            player_color: str = available_colors[player_color_index]
            just_player_color: str = player_color[0]
            output.append(player_color)
            available_colors.pop(player_color_index)
        # if a player inputs a wrong input the return will be none
        # (entire function will be looped over (just for the player))
        except ValueError:
            error_message("Please only enter numbers!")
            return None
        except KeyError:
            error_message("Please only valid indexes!")
            return None
        print(f"You chose this color: {just_player_color}")
        return [player_name, player_color]


def welcome():
    cyan_later_print("Hello!")
    cyan_later_print("Welcome to connect 4!")
    cyan_later_print("""For rules input 'help',
if you wish to proceed input anything else :D""")
    is_help = cyan_input(">")
    is_help_lower = is_help.lower()
    if is_help_lower == "help":
        cyan_later_print("""Players must connect 4
of the same colored discs in a row to win.""")
        cyan_later_print("Only one piece is played at a time.")
        cyan_later_print("Players can be on the offensive or defensive.")
        cyan_later_print("""The game ends when there is a 4-in-a-row
or a stalemate.""")
        cyan_later_print("""The starter of the previous game
goes second on the next game.""")
    cyan_later_print("Have fun!")
    cyan_later_print(" ")


def pre_game():
    p1name_and_color, p2name_and_color = None, None

    while p1name_and_color is None:
        p1name_and_color = introduce_players_to_sys("player1c4")
    while p2name_and_color is None:
        p2name_and_color = introduce_players_to_sys("player2c4")

    global player1c4, player2c4  # they will be used all over the code
    player1c4 = Player(player_details=p1name_and_color)
    player2c4 = Player(player_details=p2name_and_color)


def p_1_turn():
    successful = False
    while not successful:
        chosen_file_str = None
        while chosen_file_str is None:
            chosen_file_str: str = player1c4.choose_file()
        successful = player1c4.player_turn(chosen_file_str)


def p_2_turn():  # fix
    successful = False
    while not successful:
        chosen_file_str = None
        while chosen_file_str is None:
            chosen_file_str: str = player2c4.choose_file()
        successful = player2c4.player_turn(chosen_file_str)


def connect_4():
    passed_turns = 0
    welcome()
    pre_game()
    while passed_turns < 42:
        p_1_turn()
        passed_turns += 1
        won_by_p1 = player1c4.win_check()
        if won_by_p1 is True:
            print_board()
            print("Player 1 wins")
            return "player 1 win"
        print_board()
        p_2_turn()
        passed_turns += 1
        won_by_p2 = player2c4.win_check()
        if won_by_p2 is True:
            print_board()
            print("Player 2 wins")
            return "player 2 win"
        print_board()
    if passed_turns == 42:
        cyan_now_print(" ")
        cyan_now_print("The game ended in a tie...")


connect_4()
