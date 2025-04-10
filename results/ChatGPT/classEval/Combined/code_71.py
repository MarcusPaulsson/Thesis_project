class PushBoxGame:
    """
    Implements the functionality of a Sokoban game, where the player moves boxes to designated targets to win.
    """

    def __init__(self, game_map):
        """
        Initializes the push box game with the map and various attributes.
        :param game_map: list[str], the map of the push box game.
        """
        self.map = game_map
        self.player_row, self.player_col = self.find_player()
        self.targets = self.find_targets()
        self.boxes = self.find_boxes()
        self.is_game_over = False

    def find_player(self):
        for row in range(len(self.map)):
            for col in range(len(self.map[row])):
                if self.map[row][col] == 'O':
                    return row, col
        raise ValueError("Player position not found in the map.")

    def find_targets(self):
        return [(row, col) for row in range(len(self.map))
                for col in range(len(self.map[row])) if self.map[row][col] == 'G']

    def find_boxes(self):
        return [(row, col) for row in range(len(self.map))
                for col in range(len(self.map[row])) if self.map[row][col] == 'X']

    def check_win(self):
        """
        Check if the game is won. The game is won when all boxes are placed on target positions.
        """
        self.is_game_over = all(box in self.targets for box in self.boxes)
        return self.is_game_over

    def move(self, direction):
        """
        Move the player based on the specified direction and check if the game is won.
        :param direction: str, the direction of the player's movement ('w', 's', 'a', or 'd').
        :return: True if the game is won, False otherwise.
        """
        deltas = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}
        if direction not in deltas:
            return False
        
        delta_row, delta_col = deltas[direction]
        new_player_row, new_player_col = self.player_row + delta_row, self.player_col + delta_col

        # Check if the move is valid (not a wall)
        if self.map[new_player_row][new_player_col] == '#':
            return False

        # Handle box movement
        if self.map[new_player_row][new_player_col] == 'X':
            new_box_row = new_player_row + delta_row
            new_box_col = new_player_col + delta_col
            if self.map[new_box_row][new_box_col] in (' ', 'G'):
                self.boxes.remove((new_player_row, new_player_col))
                self.boxes.append((new_box_row, new_box_col))
            else:
                return False

        # Move the player
        self.player_row, self.player_col = new_player_row, new_player_col
        
        # Check for win condition
        return self.check_win()