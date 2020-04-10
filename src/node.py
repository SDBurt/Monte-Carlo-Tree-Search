from random import randint

from state import State
from copy import deepcopy


class Node:
    def __init__(self):

        self.state = State()
        self.parent = None
        self.children = []

    def get_state_copy(self):
        return deepcopy(self.state)

    def get_state(self):
        return self.state

    def get_parent(self):
        return self.parent

    def get_children(self):
        return self.children

    def set_state(self, new_state):
        self.state = new_state

    def set_state_copy(self, new_state):
        self.state = deepcopy(new_state)

    def set_parent(self, new_parent):
        self.parent = new_parent

    def set_children(self, new_child):
        self.children = new_child

    def has_children(self):
        return len(self.children) > 0

    def has_parent(self):
        return self.parent is not None

    def get_random_child(self):
        """
            Select a random node from child nodes
        """
        length = len(self.children)
        return self.children[randint(0, length - 1)]

    def get_child_with_max_score(self):
        """
            Iterate over child nodes and select the node with the highest
            score.
        """

        if len(self.children) == 0:
            raise ValueError("Node: No child nodes to get max score.")

        ideal_node = self.children[0]
        max_score = -float("inf")
        for child_node in self.children:
            child_score = child_node.state.score
            if child_score > max_score:
                max_score = child_score
                ideal_node = child_node

        return ideal_node


class Tree:
    def __init__(self):
        self.root = Node()

    def set_root(self, newRoot):
        self.root = newRoot

    def get_root(self):
        return self.root
