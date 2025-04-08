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
        for row_index, row in enumerate(self.map):
            for col_index, cell in enumerate(row):
                if cell == 'O':
                    self.player_row = row_index
                    self.player_col = col_index
                elif cell == 'G':
                    self.targets.append((row_index, col_index))
                elif cell == 'X':
                    self.boxes.append((row_index, col_index))
        self.target_count = len(self.targets)

    def check_win(self):
        """
        Check if the game is won. The game is won when all the boxes are placed on target positions.
        :return: True if all the boxes are placed on target positions, or False otherwise.
        """
        return all(box in self.targets for box in self.boxes)

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
            return self.check_win()  # Invalid direction, no change

        new_player_row = self.player_row + delta_row
        new_player_col = self.player_col + delta_col

        if not (0 <= new_player_row < len(self.map) and 0 <= new_player_col < len(self.map[0])):
            return self.check_win() # Out of bounds

        if self.map[new_player_row][new_player_col] == '#':
            return self.check_win()  # Wall collision

        box_index = self._find_box_index(new_player_row, new_player_col)

        if box_index != -1:
            new_box_row = self.boxes[box_index][0] + delta_row
            new_box_col = self.boxes[box_index][1] + delta_col

            if not (0 <= new_box_row < len(self.map) and 0 <= new_box_col < len(self.map[0])):
                return self.check_win() # Box out of bounds

            if self.map[new_box_row][new_box_col] == '#':
                return self.check_win()  # Box hitting a wall

            if any(box == (new_box_row, new_box_col) for i, box in enumerate(self.boxes) if i != box_index):
                return self.check_win()  # Box colliding with another box

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
        Returns -1 if no box is found.
        """
        for i, box in enumerate(self.boxes):
            if box[0] == row and box[1] == col:
                return i
        return -1