class PushBoxGame:
    """
    This class implements the functionality of a Sokoban game, where the player needs to move boxes to designated targets to win.
    """

    WALL = '#'
    PLAYER = 'O'
    TARGET = 'G'
    BOX = 'X'
    
    def __init__(self, game_map):
        """
        Initialize the push box game with the map and various attributes.
        :param game_map: list[str], the map of the push box game, represented as a list of strings. 
        """
        self.map = game_map
        self.player_row, self.player_col = self.find_player()
        self.targets = self.find_targets()
        self.boxes = self.find_boxes()
        self.is_game_over = False

    def find_player(self):
        """Finds the player's initial position."""
        for row, line in enumerate(self.map):
            if self.PLAYER in line:
                return row, line.index(self.PLAYER)
        raise ValueError("Player not found on the map.")

    def find_targets(self):
        """Finds all target positions."""
        return [(row, col) for row in range(len(self.map)) 
                for col in range(len(self.map[row])) 
                if self.map[row][col] == self.TARGET]

    def find_boxes(self):
        """Finds all box positions."""
        return [(row, col) for row in range(len(self.map)) 
                for col in range(len(self.map[row])) 
                if self.map[row][col] == self.BOX]

    def check_win(self):
        """
        Check if the game is won. The game is won when all the boxes are placed on target positions.
        """
        return all(box in self.targets for box in self.boxes)

    def move(self, direction):
        """
        Move the player based on the specified direction and check if the game is won.
        :param direction: str, the direction of the player's movement.
        :return: True if the game is won, False otherwise.
        """
        delta = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}
        if direction not in delta:
            return False

        new_row, new_col = self.player_row + delta[direction][0], self.player_col + delta[direction][1]

        if self.is_valid_move(new_row, new_col):
            self.player_row, self.player_col = new_row, new_col
            if (new_row, new_col) in self.boxes:
                box_new_row = new_row + delta[direction][0]
                box_new_col = new_col + delta[direction][1]
                if self.is_valid_move(box_new_row, box_new_col):
                    self.move_box(new_row, new_col, box_new_row, box_new_col)

            self.is_game_over = self.check_win()
            return self.is_game_over
        return False

    def move_box(self, box_row, box_col, new_box_row, new_box_col):
        """Moves the box to a new position."""
        self.boxes.remove((box_row, box_col))
        self.boxes.append((new_box_row, new_box_col))

    def is_valid_move(self, row, col):
        """Checks if the move is valid (not out of bounds and not hitting walls)."""
        return (0 <= row < len(self.map) and 
                0 <= col < len(self.map[row]) and 
                self.map[row][col] != self.WALL)