from player import Player


class Grid:
    def __init__(self, height, width):
        self.height = height
        # TODO change to size. Game only really makes sense on an nxn grid.
        self.width = width
        self.total_cells = height * width
        self.array = []
        for _ in range(height):
            self.array.append(['_']*width)

    def place_marker(self, player_, across, down):
        self.array[down][across] = player_.marker

    def get_marker(self, across, down):
        return self.array[down][across]

    def check_diagonal_win(self, column_choice: int, row_choice: int) -> bool:
        placed_marker = self.array[column_choice][row_choice]
        if column_choice != row_choice:
            return False
        else:
            for i in range(self.width):
                if not self.array[i][i] == placed_marker:
                    break
                elif i == self.width-1:
                    return True

            for i in range(self.width):
                if not self.array[i][-i] == placed_marker:
                    break
                elif i == self.width-1:
                    return True
            return False

    def check_if_won(self, player: Player, column_choice: int, row_choice: int) -> bool:
        return self.check_diagonal_win(column_choice, row_choice)
