import random


class Move:

    pattern = None
    prev_pattern = None
    game_active = True
    patterns_are_equal = True
    score = 0

    def __init__(self):

        self.pattern = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.prev_pattern = [[
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]]
        self.generate_tile_on_move()
        self.generate_tile_on_move()

    def action_right(self):
        self.forward_movement()
        self.generate_tile_on_move()

    def action_left(self):
        self.backward_movement()
        self.generate_tile_on_move()

    def action_up(self):
        self.rotate_pattern()
        self.forward_movement()
        self.rotate_pattern()
        self.rotate_pattern()
        self.rotate_pattern()
        self.generate_tile_on_move()

    def action_down(self):
        self.rotate_pattern()
        self.backward_movement()
        self.rotate_pattern()
        self.rotate_pattern()
        self.rotate_pattern()
        self.generate_tile_on_move()

    def __str__(self):
        return f"""{self.pattern[0]}
{self.pattern[1]}
{self.pattern[2]}
"""

    # {self.prev_pattern}
    def generate_tile_on_move(self, max_tile_value: int = 2):
        """
        Replaces a random zero with a provided number.
        Works with a square 2D arrays.
        :param max_tile_value:
        :return:
        """

        zeros_numbers = []
        step_counter = 0
        for row in self.pattern:
            for tile in row:
                step_counter += 1
                if tile == 0:
                    zeros_numbers.append(step_counter)

        if not zeros_numbers:
            self.game_active = False

        target_tile = random.choice(zeros_numbers)

        # print(f'random tile: {target_tile}')

        y = (target_tile - 1) // len(self.pattern)

        while target_tile > len(self.pattern):
            target_tile -= len(self.pattern)
        x = target_tile - 1

        self.pattern[y][x] = max_tile_value


    def rotate_pattern(self):
        """
        Rotating 2D-pattern clockwise
        Solved @ https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python
        :param pattern:
        :return:
        """
        rotated_pattern = list(zip(*self.pattern[::-1]))
        result = []
        for n in rotated_pattern:
            result.append(list(n))
        self.pattern = result

    def forward_movement(self):
        """
        Adapts common_move to work with a list of lists frontwards.
        :param pattern:
        :return:
        """
        for row in self.pattern:
            if row[2] == 0:
                row[2] = row[1]
                row[1] = row[0]
                row[0] = 0
            if row[1] == 0:
                row[1] = row[0]
                row[0] = 0
            if row[2] == row[1]:
                row[2] = row[2] + row[1]
                row[1] = row[0]
                row[0] = 0
                self.score += row[2] * 2
            if row[0] == row[1]:
                row[1] = row[1] + row[0]
                row[0] = 0
                self.score += row[1] * 2
            if row[2] == 0:
                row[2] = row[1]
                row[1] = row[0]

    def backward_movement(self):
        """
        Adapts common_move to work with a list of lists backwards.
        :param pattern:
        :return:
        """
        for row in self.pattern:
            row.reverse()
            if row[2] == 0:
                row[2] = row[1]
                row[1] = row[0]
                row[0] = 0
            if row[1] == 0:
                row[1] = row[0]
                row[0] = 0
            if row[2] == row[1]:
                row[2] = row[2] + row[1]
                row[1] = row[0]
                row[0] = 0
                self.score += row[2] * 2
            if row[0] == row[1]:
                row[1] = row[1] + row[0]
                row[0] = 0
                self.score += row[1] * 2
            if row[2] == 0:
                row[2] = row[1]
                row[1] = row[0]
            row.reverse()
