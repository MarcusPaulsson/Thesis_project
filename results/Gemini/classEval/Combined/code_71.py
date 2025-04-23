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
        self.init_game()

    def init_game(self):
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
        for box in self.boxes:
            if box not in self.targets:
                self.is_game_over = False
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
        delta_row, delta_col = 0, 0
        if direction == 'w':
            delta_row = -1
        elif direction == 's':
            delta_row = 1
        elif direction == 'a':
            delta_col = -1
        elif direction == 'd':
            delta_col = 1
        else:
            return self.check_win()

        new_player_row = self.player_row + delta_row
        new_player_col = self.player_col + delta_col

        if self.map[new_player_row][new_player_col] == '#':
            return self.check_win()

        box_index = self._find_box_index(new_player_row, new_player_col)

        if box_index != -1:
            new_box_row = self.boxes[box_index][0] + delta_row
            new_box_col = self.boxes[box_index][1] + delta_col

            if self.map[new_box_row][new_box_col] == '#':
                return self.check_win()

            if self._is_obstacle(new_box_row, new_box_col):
                return self.check_win()

            self.boxes[box_index] = (new_box_row, new_box_col)
            self.player_row = new_player_row
            self.player_col = new_player_col
        else:
            self.player_row = new_player_row
            self.player_col = new_player_col

        return self.check_win()

    def _find_box_index(self, row, col):
        """
        Helper function to find the index of a box at a given position.
        :param row: The row of the box.
        :param col: The column of the box.
        :return: The index of the box in the boxes list, or -1 if no box is found.
        """
        for i, box in enumerate(self.boxes):
            if box[0] == row and box[1] == col:
                return i
        return -1

    def _is_obstacle(self, row, col):
        """
        Helper function to check if a given position is an obstacle (another box).
        :param row: The row to check.
        :param col: The column to check.
        :return: True if the position is an obstacle, False otherwise.
        """
        for other_box in self.boxes:
            if other_box[0] == row and other_box[1] == col:
                return True
        return False

    def print_map(self):
        """
        Print the current map of the game.
        """
        for row in self.map:
            print(' '.join(row))