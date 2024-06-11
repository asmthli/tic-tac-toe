from grid import Grid
from player import Player


def show_welcome() -> None:
    print("Welcome to Tic-Tac-Toe.")


def show_instructions() -> None:
    print("You will both take turns placing a chosen marker in a grid. You win when you make a complete line with your"
          " markers.\n")


def show_game_over(player1: Player, player2: Player) -> None:
    print(f"GAME OVER! Score: P1: {player1.score} P2: {player2.score}")


def get_grid_size() -> tuple[int, int]:
    rows = int(input("How many rows would you like your grid to have?: "))
    columns = int(input("How many columns would you like your grid to have?: "))
    return rows, columns


def get_player_marker(player_num: int) -> None:
    marker = input(f"Player {player_num} - What would you like your mark to be? (x/o): ")


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
    print("---" * grid.width)

    for j in range(grid.height):
        row = ""
        for i in range(grid.width):
            mark = grid.get_marker(i, j)
            row += make_grid_cell(mark)
        print(row)
        print("---" * grid.width)


show_grid(Grid(3, 3))
