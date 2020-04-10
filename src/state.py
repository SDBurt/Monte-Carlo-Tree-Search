from copy import deepcopy
from random import randint

from game import Board


class State:
    def __init__(self):

        self.board = Board()
        self.player = 1
        self.visit_count = 0
        self.score = 0

    def get_board(self):
        return self.board

    def get_player(self):
        return self.player

    def get_visit_count(self):
        return self.visit_count

    def get_score(self):
        return self.score

    def get_opponent(self):
        return 3 - self.player

    def set_Board(self, board):
        self.board = board

    def copy_Board(self, board):
        self.board = board

    def set_player(self, player):
        self.player = player

    def set_visit_count(self, visit_count):
        self.visit_count = visit_count

    def set_score(self, score):
        self.score = score

    def increment_visit(self):
        self.visit_count += 1

    def add_score(self, score):
        self.score += score

    def get_possible_states(self):
        """
            constructs a list of all possible states from current state
        """

        possible_states = []

        empty_positions = self.board.get_empty_positions()

        for position in empty_positions:
            tempState = State()
            tempState.board = deepcopy(self.board)
            tempState.player = self.player
            tempState.visit_count = self.visit_count
            tempState.score = self.score
            tempState.board.move(self.player, position[0], position[1])
            possible_states.append(tempState)

        return possible_states

    def random_play(self):
        """
            get_ a list of all possible positions on the board and play a random move
        """
        empty_positions = self.board.get_empty_positions()

        ranPos = randint(0, len(empty_positions) - 1)

        self.board.move(
            self.player, empty_positions[ranPos][0], empty_positions[ranPos][1]
        )

    def togglePlayer(self):
        self.player = 3 - self.player
