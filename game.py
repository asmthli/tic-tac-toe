import user_interface
from player import Player
from grid import Grid
import random

user_interface.show_welcome()
user_interface.show_instructions()

player1_marker, player2_marker = user_interface.get_player_markers()
players = [Player(number=1, marker=player1_marker), Player(number=2, marker=player2_marker)]

size = user_interface.get_grid_size()
grid = Grid(size)

user_interface.show_begin()

markers_placed = 0
game_over = False
current_player = random.choice(players)
while not game_over:
    x, y = user_interface.ask_player_place_marker(current_player)
    grid.place_marker(current_player, x, y)
    markers_placed += 1
    user_interface.show_grid(grid)

    if markers_placed == grid.total_cells:
        user_interface.show_game_over(players[0], players[1])
        game_over = not user_interface.ask_play_again()
    else:
        winner = grid.check_if_won(x, y)
        if winner:
            print("Winner!")
            current_player.score += 1

    current_player = players[0] if current_player == players[1] else players[1]
