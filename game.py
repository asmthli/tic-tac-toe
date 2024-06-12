import user_interface
from player import Player
from grid import Grid
import random


class Game:
    def __init__(self):
        self.players = None
        self.grid = None
        self.current_player = None
        self.setup()

    def setup(self):
        user_interface.show_welcome()
        user_interface.show_instructions()
        player1_marker, player2_marker = user_interface.get_player_markers()
        self.players = [Player(number=1, marker=player1_marker), Player(number=2, marker=player2_marker)]
        size = user_interface.get_grid_size()
        self.grid = Grid(size)
        self.current_player = random.choice(self.players)

    def reset(self):
        self.grid = Grid(self.grid.size)

    def start(self):
        user_interface.show_begin()
        user_interface.show_grid(self.grid)

        game_over = False
        while not game_over:
            x, y = user_interface.ask_player_place_marker(self.current_player)
            self.grid.place_marker(self.current_player, x, y)
            self.grid.markers_placed += 1
            user_interface.show_grid(self.grid)

            if self.grid.check_if_won(x, y):
                self.current_player.score += 1
                user_interface.show_game_over(self.players[0], self.players[1])
                game_over = True
            elif self.grid.is_full():
                user_interface.show_game_over(self.players[0], self.players[1])
                game_over = True
            else:
                self.current_player = self.players[0] if self.current_player == self.players[1] else self.players[1]

        if user_interface.ask_play_again():
            self.reset()
            self.start()


if __name__ == "__main__":
    game = Game()
    game.start()
