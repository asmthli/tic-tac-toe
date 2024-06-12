from player import Player


class Grid:
    def __init__(self, height, width):
        self.height = height
        # TODO change to size. Game only really makes sense on an nxn grid.
        self.width = width
        self.total_cells = height * width
        self.array = []
        for _ in range(height):
            self.array.append(['_'] * width)

    def place_marker(self, player_, x, y):
        self.array[y][x] = player_.marker

    def get_marker(self, x, y):
        return self.array[y][x]

    def check_diagonal_win(self, x: int, y: int) -> bool:
        placed_marker = self.array[y][x]
        if x != y:
            return False
        else:
            for i in range(self.width):
                if not self.array[i][i] == placed_marker:
                    break
                elif i == self.width - 1:
                    return True

            for i in range(self.width):
                if not self.array[self.height - 1 - i][i] == placed_marker:
                    break
                elif i == self.width - 1:
                    return True
            return False

    def check_vertical_win(self, x: int, y: int) -> bool:
        placed_marker = self.array[y][x]
        for i in range(self.height):
            if self.array[i][x] != placed_marker:
                return False
        return True

    def check_horizontal_win(self, x: int, y: int) -> bool:
        placed_marker = self.array[y][x]
        for i in range(self.width):
            if self.array[y][i] != placed_marker:
                return False
        return True

    def check_if_won(self, x: int, y: int) -> bool:
        if self.check_diagonal_win(x, y):
            return True
        elif self.check_horizontal_win(x, y):
            return True
        elif self.check_vertical_win(x, y):
            return True
        else:
            return False
