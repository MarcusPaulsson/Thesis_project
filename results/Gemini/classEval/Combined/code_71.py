class PushBoxGame:
    """
    This class implements a functionality of a sokoban game, where the player needs to move boxes to designated targets in order to win.
    """

    def __init__(self, map):
        """
        Initialize the push box game with the map and various attributes.
        :param map: list[str], the map of the push box game, represented as a list of strings. 
            Each character on the map represents a different element, including the following:
            - '#' represents a wall that neither the player nor the box can pass through;
            - 'O' represents the initial position of the player;
            - 'G' represents the target position;
            - 'X' represents the initial position of the box.
        """
        self.map = map
        self.player_row = 0
        self.player_col = 0
        self.targets = []
        self.boxes = []
        self.target_count = 0
        self.is_game_over = False
        self._init_game()

    def _init_game(self):
        """
        Initialize the game by setting the positions of the player, targets, and boxes based on the map.
        """
        for row in range(len(self.map)):
            for col in range(len(self.map[row])):
                cell = self.map[row][col]
                if cell == 'O':
                    self.player_row = row
                    self.player_col = col
                elif cell == 'G':
                    self.targets.append((row, col))
                elif cell == 'X':
                    self.boxes.append((row, col))
        self.target_count = len(self.targets)

    def check_win(self):
        """
        Check if the game is won. The game is won when all the boxes are placed on target positions.
        :return: True if all the boxes are placed on target positions, or False otherwise.
        """
        if not self.boxes:
            return False  # No boxes, can't win

        for box in self.boxes:
            if box not in self.targets:
                return False
        self.is_game_over = True
        return True


    def move(self, direction):
        """
        Move the player based on the specified direction and check if the game is won.
        :param direction: str, the direction of the player's movement. 
            It can be 'w', 's', 'a', or 'd' representing up, down, left, or right respectively.

        :return: True if the game is won, False otherwise.
        """
        dr, dc = 0, 0
        if direction == 'w':
            dr, dc = -1, 0
        elif direction == 's':
            dr, dc = 1, 0
        elif direction == 'a':
            dr, dc = 0, -1
        elif direction == 'd':
            dr, dc = 0, 1
        else:
            return self.is_game_over

        new_row = self.player_row + dr
        new_col = self.player_col + dc

        if not (0 <= new_row < len(self.map) and 0 <= new_col < len(self.map[0])):
            return self.is_game_over

        if self.map[new_row][new_col] == '#':
            return self.is_game_over

        box_index = self._find_box_index(new_row, new_col)

        if box_index != -1:
            new_box_row = new_row + dr
            new_box_col = new_col + dc

            if not (0 <= new_box_row < len(self.map) and 0 <= new_box_col < len(self.map[0])):
                return self.is_game_over

            if self.map[new_box_row][new_box_col] == '#':
                return self.is_game_over

            if self._is_occupied_by_another_box(new_box_row, new_box_col):
                return self.is_game_over

            self.boxes[box_index] = (new_box_row, new_box_col)
            self.player_row = new_row
            self.player_col = new_col
            return self.check_win()

        self.player_row = new_row
        self.player_col = new_col
        return self.is_game_over

    def _find_box_index(self, row, col):
        """Helper function to find the index of a box at a given position."""
        for i, box in enumerate(self.boxes):
            if box[0] == row and box[1] == col:
                return i
        return -1

    def _is_occupied_by_another_box(self, row, col):
        """Helper function to check if a position is occupied by another box."""
        for other_box in self.boxes:
            if other_box[0] == row and other_box[1] == col:
                return True
        return False