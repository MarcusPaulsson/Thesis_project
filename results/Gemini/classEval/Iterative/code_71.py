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
        self.height = len(map)
        self.width = len(map[0]) if map else 0  # Handle empty map case
        self.init_game()

    def init_game(self):
        """
        Initialize the game by setting the positions of the player, targets, and boxes based on the map.
        """
        for row in range(self.height):
            for col in range(self.width):
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
        And update the value of self.is_game_over.
        :return: True if all the boxes are placed on target positions, or False otherwise.
        """
        if not self.boxes or not self.targets:
            self.is_game_over = False
            return self.is_game_over

        boxes_on_targets = 0
        for box in self.boxes:
            if box in self.targets:
                boxes_on_targets += 1
        self.is_game_over = boxes_on_targets == self.target_count
        return self.is_game_over

    def move(self, direction):
        """
        Move the player based on the specified direction and check if the game is won.
        :param direction: str, the direction of the player's movement. 
            It can be 'w', 's', 'a', or 'd' representing up, down, left, or right respectively.

        :return: True if the game is won, False otherwise.
        """
        new_row = self.player_row
        new_col = self.player_col

        if direction == 'w':
            new_row -= 1
        elif direction == 's':
            new_row += 1
        elif direction == 'a':
            new_col -= 1
        elif direction == 'd':
            new_col += 1
        else:
            return False  # Invalid direction

        if not (0 <= new_row < self.height and 0 <= new_col < self.width):
            return False  # Out of bounds

        if self.map[new_row][new_col] == '#':
            return False  # Hit a wall

        box_index = -1
        for i, box in enumerate(self.boxes):
            if box[0] == new_row and box[1] == new_col:
                box_index = i
                break

        if box_index != -1:
            box_row, box_col = self.boxes[box_index]
            new_box_row = box_row + (new_row - self.player_row)
            new_box_col = box_col + (new_col - self.player_col)

            if not (0 <= new_box_row < self.height and 0 <= new_box_col < self.width):
                return False  # Box out of bounds

            if self.map[new_box_row][new_box_col] == '#':
                return False  # Box hits a wall

            is_occupied = False
            for other_box in self.boxes:
                if other_box != (box_row, box_col) and other_box[0] == new_box_row and other_box[1] == new_box_col:
                    is_occupied = True
                    break

            if is_occupied:
                return False  # Box hits another box

            self.boxes[box_index] = (new_box_row, new_box_col)

        self.player_row = new_row
        self.player_col = new_col

        return self.check_win()

    def print_map(self):
        """
        Print the current state of the map.
        """
        temp_map = [list(row) for row in self.map]

        # Place player
        temp_map[self.player_row][self.player_col] = 'O'

        # Place boxes
        for row, col in self.boxes:
            temp_map[row][col] = 'X'

        # Place targets if not covered by a box
        for row, col in self.targets:
            if temp_map[row][col] not in ['X', 'O']:
                temp_map[row][col] = 'G'

        for row in temp_map:
            print(''.join(row))