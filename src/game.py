class Board:
    def __init__(self, board_size=3):
        self.total_moves = 0
        self.board_size = board_size
        self.board_state = [[0] * board_size for i in range(board_size)]

    def is_legal_move(self, y, x):
        valid = (y < self.board_size and y >= 0) and (x < self.board_size and x >= 0)

        return valid

    def move(self, player: int, y: int, x: int):
        """
            Update the board state with new new move
            Error check that the x and y coords are valid
                and that the player is correct
        """
        if not self.is_legal_move(y, x):
            raise ValueError(
                "Move: Invalid coordinate (%d, %d), Outside board size." % (x, y)
            )
        if self.board_state[y][x] != 0:
            raise ValueError(
                "Move: Invalid coordinate (%d, %d), Position already taken." % (x, y)
            )

        self.total_moves += 1
        self.board_state[y][x] = player

    def check_game_state(self):

        winning_positions = [
            [[0, 0], [0, 1], [0, 2]],
            [[1, 0], [1, 1], [1, 2]],
            [[2, 0], [2, 1], [2, 2]],
            [[0, 0], [1, 0], [2, 0]],
            [[0, 1], [1, 1], [2, 1]],
            [[0, 2], [1, 2], [2, 2]],
            [[0, 0], [1, 1], [2, 2]],
            [[2, 0], [1, 1], [0, 2]],
        ]
        zero_found = False

        for arrangement in winning_positions:
            first_symbol = self.board_state[arrangement[0][0]][arrangement[0][1]]
            if first_symbol != 0:
                winner = True
                for y, x in arrangement:
                    if self.board_state[y][x] != first_symbol:
                        winner = False
                        if self.board_state[y][x] == 0:
                            zero_found = True
                        break

                if winner:
                    return first_symbol  # winner found, return player
            else:
                winner = False
                zero_found = True

        if zero_found:
            return -1  # game is not done

        # No zeros found, all positions filled, no winner, tie game
        return 0

    def get_empty_positions(self):
        length = len(self.board_state)

        emptyPositions = []

        for j in range(length):
            for i in range(length):
                if self.board_state[j][i] == 0:
                    emptyPositions.append([j, i])

        return emptyPositions
