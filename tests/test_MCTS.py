import pytest

from src.game import Board
from src.MCTS import MonteCarloTreeSearch


PLAYER1 = 1
PLAYER2 = 2


class TestBoard:
    """
            Tests for the board class

            Ex:
                -------------
                | 1 | 1 | 2 |
                -------------
                | 2 | 1 | 1 |
                -------------
                | 1 | 2 | 2 |
                -------------


        """

    def test_move(self):

        board = Board()
        board.move(PLAYER1, 2, 1)
        assert board.board_state[2][1] == PLAYER1

    def test_get_empty_positions(self):

        board = Board()

        board.move(PLAYER1, 2, 1)
        board.move(PLAYER2, 1, 0)

        emptyPositions = board.get_empty_positions()

        assert [1, 0] not in emptyPositions
        assert [2, 1] not in emptyPositions

    def test_checkStatus_tie(self):

        board = Board()

        board.move(PLAYER1, 0, 0)
        board.move(PLAYER1, 0, 1)
        board.move(PLAYER2, 0, 2)
        board.move(PLAYER2, 1, 0)
        board.move(PLAYER1, 1, 1)
        board.move(PLAYER1, 1, 2)
        board.move(PLAYER1, 2, 0)
        board.move(PLAYER2, 2, 1)
        board.move(PLAYER2, 2, 2)

        emptyPositions = board.get_empty_positions()

        assert len(emptyPositions) == 0
        assert board.checkStatus() == 0

    def test_checkStatus_in_progress(self):

        board = Board()

        board.move(PLAYER1, 0, 0)
        board.move(PLAYER1, 0, 1)
        board.move(PLAYER2, 0, 2)
        board.move(PLAYER2, 1, 0)
        board.move(PLAYER1, 1, 1)
        board.move(PLAYER1, 1, 2)
        board.move(PLAYER1, 2, 0)
        board.move(PLAYER2, 2, 1)

        emptyPositions = board.get_empty_positions()

        assert len(emptyPositions) == 1
        assert board.checkStatus() == -1

    def test_checkStatus_player_two_win(self):

        board = Board()

        board.move(PLAYER1, 0, 0)
        board.move(PLAYER1, 0, 1)
        board.move(PLAYER2, 0, 2)
        board.move(PLAYER2, 1, 0)
        board.move(PLAYER1, 1, 1)
        board.move(PLAYER2, 1, 2)
        board.move(PLAYER2, 2, 0)
        board.move(PLAYER2, 2, 1)

        emptyPositions = board.get_empty_positions()

        assert len(emptyPositions) == 0
        assert board.checkStatus() == 2

    def test_checkStatus_player_one_win(self):

        board = Board()

        board.move(PLAYER1, 0, 0)
        board.move(PLAYER1, 0, 1)
        board.move(PLAYER2, 0, 2)
        board.move(PLAYER2, 1, 0)
        board.move(PLAYER1, 1, 1)
        board.move(PLAYER1, 1, 2)
        board.move(PLAYER2, 2, 0)
        board.move(PLAYER1, 2, 1)

        emptyPositions = board.get_empty_positions()

        assert len(emptyPositions) == 0
        assert board.checkStatus() == 1
