"""
    Module for a python implementation of the Monte Carlo Tree Search
    algorithm

    Based on Java tutorial so I will be updating to become more Pythonic later

    Idea: select optimal child nodes until we reach the leaf
    node of the tree

    $$$
        /frac{w_i}{n_i} + c /sqrt{/frac{/ln t}{n_i}}
    $$$

    where:
        w_i = number of wins after the i-th move
        n_i number of simulations after the i-th move
        c = exploration parameter
        t = total number of simulations
"""

from datetime import datetime, timedelta
from math import log, sqrt
from random import randint
from tqdm import trange
from copy import copy, deepcopy

from game import Board
from node import Node, Tree
from state import State

STATES = {"DEFAULT_BOARD_SIZE": 3, "IN_PROGRESS": -1, "DRAW": 0}


def get_UCT_value(totalVisit, nodewin_score, nodeVisit):

    if nodeVisit == 0:
        return float("inf")
    return (float(nodewin_score) / float(nodeVisit)) + 1.41 * sqrt(
        log(totalVisit) / float(nodeVisit)
    )


def find_best_node(node):

    parentVisit = node.state.visit_count

    nodes = node.get_children()

    uctValues = [
        get_UCT_value(parentVisit, c.state.score, c.state.visit_count) for c in nodes
    ]

    bestNode = nodes[uctValues.index(max(uctValues))]

    return bestNode


class MonteCarloTreeSearch:
    def __init__(self):
        self.WIN_SCORE = 10
        self.level = 0
        self.current_player = None
        self.opponent = None
        self.board = Board()

    def select_promising_node(self, rootNode):

        if len(rootNode.get_children()) == 0:
            return rootNode

        node = find_best_node(rootNode)
        while len(node.get_children()) != 0:
            node = find_best_node(node)

        return node

    def expand_node(self, node):

        possible_states = node.get_state().get_possible_states()

        for state in possible_states:
            newNode = Node()
            newNode.set_state_copy(state)
            newNode.set_parent(node)
            newNode.state.set_player(node.state.get_opponent())
            node.get_children().append(newNode)

    def back_propogation(self, nodeToExplore, current_player):

        tempNode = nodeToExplore

        while tempNode != None:

            tempNode.state.increment_visit()

            if tempNode.state.player == current_player:
                tempNode.state.add_score(self.WIN_SCORE)

            tempNode = tempNode.get_parent()

    def simulate_random_playout(self, node):

        tempNode = Node()
        tempNode.parent = node.parent
        tempNode.state = deepcopy(node.state)
        tempNode.children = deepcopy(node.children)

        boardStatus = tempNode.state.board.check_game_state()

        if boardStatus == self.opponent:

            tempNode.parent.state.set_score(-float("inf"))
            return boardStatus

        while boardStatus == -1:
            tempNode.state.togglePlayer()
            tempNode.state.random_play()
            boardStatus = tempNode.state.board.check_game_state()

        return boardStatus

    def find_next_move(self, board, current_player):
        """
            Define an end time which will act as a terminating condition
        """

        tree = Tree()
        rootNode = tree.get_root()
        rootNode.state.board = board
        rootNode.state.set_player(current_player)
        self.opponent = 3 - current_player

        move_epochs = 50000
        for _ in range(move_epochs):

            promising_node = self.select_promising_node(rootNode)

            if promising_node.get_state().get_board().check_game_state() == -1:
                self.expand_node(promising_node)

            nodeToExplore = promising_node

            if len(promising_node.get_children()) > 0:
                nodeToExplore = promising_node.get_random_child()

            playoutResult = self.simulate_random_playout(nodeToExplore)
            self.back_propogation(nodeToExplore, playoutResult)

        winnerNode = rootNode.get_child_with_max_score()
        tree.set_root(winnerNode)

        newBoard = deepcopy(winnerNode.get_state().get_board())
        return newBoard


def SimulateInterAIPlay():

    board = Board()
    mcts = MonteCarloTreeSearch()

    totalMoves = 3 * 3
    player = 1

    for _ in range(totalMoves):

        print("----------------")
        print(board.board_state[0])
        print(board.board_state[1])
        print(board.board_state[2])

        board = mcts.find_next_move(board, player)

        if board.check_game_state() != -1:
            break

        player = 3 - player

    winStatus = board.check_game_state()
    print("----------------")
    print("----------------")
    print("Winner: ", winStatus)
    print("Draw? ", winStatus == 0)


if __name__ == "__main__":
    SimulateInterAIPlay()
