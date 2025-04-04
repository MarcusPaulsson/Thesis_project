class PushBoxGame:
    """
    This class implements a functionality of a sokoban game, where the player needs to move boxes to designated targets in order to win.
    """

    def __init__(self, game_map):
        """
        Initialize the push box game with the map and various attributes.
        :param game_map: list[str], the map of the push box game, represented as a list of strings. 
            Each character on the map represents a different element:
            - '#' represents a wall;
            - 'O' represents the player;
            - 'G' represents the target position;
            - 'X' represents the box.
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
        return None  # Should not happen if the map is valid

    def find_targets(self):
        targets = []
        for row in range(len(self.map)):
            for col in range(len(self.map[row])):
                if self.map[row][col] == 'G':
                    targets.append((row, col))
        return targets

    def find_boxes(self):
        boxes = []
        for row in range(len(self.map)):
            for col in range(len(self.map[row])):
                if self.map[row][col] == 'X':
                    boxes.append((row, col))
        return boxes

    def check_win(self):
        """
        Check if the game is won. The game is won when all boxes are on target positions.
        """
        return all(box in self.targets for box in self.boxes)

    def move(self, direction):
        """
        Move the player based on the specified direction and check if the game is won.
        :param direction: str, the direction of the player's movement. 
            It can be 'w', 's', 'a', or 'd' representing up, down, left, or right respectively.
        :return: True if the game is won, False otherwise.
        """
        move_map = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}
        if direction in move_map:
            delta_row, delta_col = move_map[direction]
            new_player_row = self.player_row + delta_row
            new_player_col = self.player_col + delta_col

            if self.is_valid_move(new_player_row, new_player_col):
                self.player_row = new_player_row
                self.player_col = new_player_col
                self.update_boxes()
                self.is_game_over = self.check_win()
                return self.is_game_over
        return False

    def is_valid_move(self, new_row, new_col):
        if self.map[new_row][new_col] == '#':
            return False  # Wall
        if (new_row, new_col) in self.boxes:
            # Check if we can push the box
            box_new_row = new_row + (new_row - self.player_row)
            box_new_col = new_col + (new_col - self.player_col)
            return (0 <= box_new_row < len(self.map) and
                    0 <= box_new_col < len(self.map[0]) and
                    self.map[box_new_row][box_new_col] != '#' and
                    (box_new_row, box_new_col) not in self.boxes)
        return True

    def update_boxes(self):
        # Update the position of boxes if they are pushed
        for box_index in range(len(self.boxes)):
            box_row, box_col = self.boxes[box_index]
            if (box_row, box_col) == (self.player_row + (self.player_row - box_row), 
                                      self.player_col + (self.player_col - box_col)):
                self.boxes[box_index] = (box_row + (box_row - self.player_row), 
                                         box_col + (box_col - self.player_col))

    def print_map(self):
        display_map = [list(row) for row in self.map]
        display_map[self.player_row][self.player_col] = 'O'
        for box_row, box_col in self.boxes:
            display_map[box_row][box_col] = 'X'
        for target_row, target_col in self.targets:
            display_map[target_row][target_col] = 'G'

        for row in display_map:
            print(''.join(row))