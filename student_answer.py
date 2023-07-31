import collections

from search import *
import copy


def strpath(arcs):
    return "".join([arc.head for arc in arcs])


class FSFrontier(Frontier):

    def __init__(self):
        self.dq = collections.deque()

    def add(self, path):
        self.dq.append(path)
        print(f"+{strpath(path)}")

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.dq) == 0:
            raise StopIteration
        x = self.pop()
        print(f"-{strpath(x)}")
        return x

    @abstractmethod
    def pop(self):
        """Selects, removes, and returns a path on the frontier if there is
        any.Recall that a path is a sequence (tuple) of Arc
        objects. Override this method to achieve a desired search
        strategy.
        """


class DFSFrontier(FSFrontier):
    def pop(self):
        return self.dq.pop()


class BFSFrontier(FSFrontier):
    def pop(self):
        return self.dq.popleft()


class FunkyNumericGraph(Graph):

    def __init__(self, starting_number):
        self.starting_number = starting_number

    def outgoing_arcs(self, tail_node):
        return [Arc(tail_node, tail_node - 1, action="1down", cost=1),
                Arc(tail_node, tail_node + 2, action="2up", cost=1)]

    def starting_nodes(self):
        return [self.starting_number]

    def is_goal(self, node):
        return node % 10 == 0


BLANK = ' '


class SlidingPuzzleGraph(Graph):

    def __init__(self, starting_state):
        self.starting_state = starting_state

    def outgoing_arcs(self, state):

        n = len(state)  # the size of the puzzle

        # Find i and j such that state[i][j] == BLANK
        ij = [item for sublist in state for item in sublist].index(BLANK)
        i, j = ij // n, ij % n

        arcs = []
        if i > 0:
            action = "Move {} down".format(state[i - 1][j])  # or blank goes up
            new_state = copy.deepcopy(state)
            new_state[i][j], new_state[i - 1][j] = new_state[i - 1][j], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        if i < n - 1:
            action = "Move {} up".format(state[i + 1][j])  # or blank goes down
            new_state = copy.deepcopy(state)
            new_state[i][j], new_state[i + 1][j] = new_state[i + 1][j], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        if j > 0:
            action = "Move {} right".format(state[i][j - 1])  # or blank goes left
            new_state = copy.deepcopy(state)
            new_state[i][j], new_state[i][j - 1] = new_state[i][j - 1], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        if j < n - 1:
            action = "Move {} left".format(state[i][j + 1])  # or blank goes left
            new_state = copy.deepcopy(state)
            new_state[i][j], new_state[i][j + 1] = new_state[i][j + 1], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        return arcs

    def starting_nodes(self):
        return [self.starting_state]

    def is_goal(self, state):
        flat = [0 if item == BLANK else item for sublist in state for item in sublist]
        return state[0][0] == BLANK and sorted(flat) == flat
