#
# warning
# !!!!! turn main into a func and update connectFour.py !!!!!!!
#

from connectFour import connect_4
from generalUseFunc import intify, div

available_games_numbers: list = (1, )

available_games_names: dict = {
    1: "Connect 4",
    2: "Game unavailable for now",
    3: "Game unavailable for now"
}

div()

print("What game do you want to play?")

div()

for game_key in available_games_names:
    print(f"    {game_key}: {available_games_names[game_key]}")

div()

game_choice_int = None
while game_choice_int is None:
    game_choice_str: str = input("Input the number: ")
    game_choice_int: int = intify(game_choice_str)
    div()
    if (
        game_choice_int not in available_games_numbers
        and game_choice_int is not None
    ):
        print("The game you chose doesn't exist or is currently unavailable.")
        game_choice_int = None
        div()


print(f"You have chosen the game {available_games_names[game_choice_int]}")

div()

if game_choice_int == 1:
    connect_4()
if game_choice_int != 1:
    print("How did you even manage to get this message, post a screenshot")
