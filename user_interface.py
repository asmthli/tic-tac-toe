from grid import Grid
from player import Player


def show_welcome() -> None:
    print("Welcome to Tic-Tac-Toe.")


def show_instructions() -> None:
    print("You will both take turns placing a chosen marker in a grid. You win when you make a complete line with your"
          " markers.\n")


def show_begin() -> None:
    print("The game will now begin!")


def show_game_over(player1: Player, player2: Player) -> None:
    print(f"GAME OVER! Score: P1: {player1.score} P2: {player2.score}")


def get_grid_size() -> int:
    size = int(input("What size grid would you like to play on?: "))
    return size


def get_player_markers() -> tuple[str, str]:
    # TODO Check length of marker - don't let user input a massive string.
    player1_marker = input(f"Player 1 - What would you like your mark to be? (x/o): ")
    player_2_marker = 'x' if player1_marker == 'o' else 'o'
    print(f"Great, player 1 has marker {player1_marker}. Player 2, your marker must then be {player_2_marker}.")
    return player1_marker, player_2_marker


def ask_player_place_marker(player: Player) -> tuple[int, int]:
    marker_position = input(f"Player {player.number}, where would you like to place a marker? (x, y): ")
    x = int(marker_position.split(',')[0].strip())
    y = int(marker_position.split(',')[1].strip())
    return x, y


def ask_play_again() -> bool:
    answer = input("Would you like to play again? (y/n): ")
    if answer == "y":
        return True
    elif answer == "n":
        return False
    else:
        print("Please input a valid answer 'y' or 'n'.")
        return ask_play_again()


def make_grid_cell(fill: str = "") -> str:
    return f"|{fill}|"


def show_grid(grid: Grid) -> None:
    print("---" * grid.size)

    for j in range(grid.size):
        row = ""
        for i in range(grid.size):
            mark = grid.get_marker(i, j)
            row += make_grid_cell(mark)
        print(row)
        print("---" * grid.size)
