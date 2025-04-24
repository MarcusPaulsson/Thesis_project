class PushBoxGame:
    """
    This class implements the functionality of a Sokoban game, where the player needs to move boxes to designated targets to win.
    """

    def __init__(self, game_map):
        """
        Initialize the push box game with the map and various attributes.
        :param game_map: list[str], the map of the push box game, represented as a list of strings. 
            Each character on the map represents a different element:
            - '#' represents a wall;
            - 'O' represents the player's initial position;
            - 'G' represents a target position;
            - 'X' represents a box.
        """
        self.map = game_map
        self.player_row, self.player_col = self.find_player()
        self.targets = self.find_targets()
        self.boxes = self.find_boxes()
        self.is_game_over = False

    def find_player(self):
        """Find the player's initial position on the map."""
        for row in range(len(self.map)):
            for col in range(len(self.map[row])):
                if self.map[row][col] == 'O':
                    return row, col
        raise ValueError("Player not found on the map.")

    def find_targets(self):
        """Find all target positions on the map."""
        return [(row, col) for row in range(len(self.map)) for col in range(len(self.map[row])) if self.map[row][col] == 'G']

    def find_boxes(self):
        """Find all box positions on the map."""
        return [(row, col) for row in range(len(self.map)) for col in range(len(self.map[row])) if self.map[row][col] == 'X']

    def check_win(self):
        """Check if the game is won. The game is won when all boxes are placed on target positions."""
        return all(box in self.targets for box in self.boxes)

    def move(self, direction):
        """
        Move the player based on the specified direction and check if the game is won.
        :param direction: str, the direction of the player's movement ('w', 's', 'a', 'd').
        :return: True if the game is won, False otherwise.
        """
        delta = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}

        if direction not in delta:
            return False

        new_row = self.player_row + delta[direction][0]
        new_col = self.player_col + delta[direction][1]

        if self.is_move_valid(new_row, new_col):
            self.player_row, self.player_col = new_row, new_col
            self.check_box_move(new_row, new_col)
            self.is_game_over = self.check_win()
            return self.is_game_over
        return False

    def is_move_valid(self, new_row, new_col):
        """Check if the move is valid (not hitting a wall or moving out of bounds)."""
        return (0 <= new_row < len(self.map) and
                0 <= new_col < len(self.map[new_row]) and
                self.map[new_row][new_col] != '#')

    def check_box_move(self, new_row, new_col):
        """Check if the player is pushing a box and move the box if possible."""
        if (new_row, new_col) in self.boxes:
            box_new_row = new_row + (new_row - self.player_row)
            box_new_col = new_col + (new_col - self.player_col)

            if self.is_move_valid(box_new_row, box_new_col) and (box_new_row, box_new_col) not in self.boxes:
                self.boxes.remove((new_row, new_col))
                self.boxes.append((box_new_row, box_new_col))