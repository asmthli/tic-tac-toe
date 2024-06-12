class Grid:
    def __init__(self, size: int) -> None:
        self.size = size
        self.total_cells = size * size
        self.array = []
        for _ in range(size):
            self.array.append(['_'] * size)
        self.markers_placed = 0

    def place_marker(self, player_, x, y) -> None:
        self.array[y][x] = player_.marker

    def check_diagonal_win(self, x: int, y: int) -> bool:
        placed_marker = self.array[y][x]
        if x != y:
            return False
        else:
            for i in range(self.size):
                if not self.array[i][i] == placed_marker:
                    break
                elif i == self.size - 1:
                    return True

            for i in range(self.size):
                if not self.array[self.size - 1 - i][i] == placed_marker:
                    break
                elif i == self.size - 1:
                    return True
            return False

    def check_vertical_win(self, x: int, y: int) -> bool:
        placed_marker = self.array[y][x]
        for i in range(self.size):
            if self.array[i][x] != placed_marker:
                return False
        return True

    def check_horizontal_win(self, x: int, y: int) -> bool:
        placed_marker = self.array[y][x]
        for i in range(self.size):
            if self.array[y][i] != placed_marker:
                return False
        return True

    def is_full(self) -> bool:
        if self.markers_placed == self.total_cells:
            return True
        else:
            return False

    def check_if_won(self, x: int, y: int) -> bool:
        if self.check_diagonal_win(x, y):
            return True
        elif self.check_horizontal_win(x, y):
            return True
        elif self.check_vertical_win(x, y):
            return True
        else:
            return False

    def check_cell_occupied(self, x: int, y: int) -> bool:
        if self.array[y][x] == "_":
            return False
        else:
            return True
