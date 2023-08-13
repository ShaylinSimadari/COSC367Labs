import collections
import itertools
import math
from heapq import heappush, heappop

from search import *
import copy


def strpath(arcs):
    path = "".join([arc.head if arc.head else "#" for arc in arcs])
    return path


def strpathc(arcs):
    cost = sum([arc.cost if arc.cost else 0 for arc in arcs])
    return f"{strpath(arcs)},{cost}"


def strpathh(arcs, f):
    return f"{strpath(arcs)},{f}"


class FSFrontier(Frontier):

    @abstractmethod
    def add(self, path):
        """Adds a new path to the frontier. A path is a sequence (tuple) of
        Arc objects. You should override this method.

        """

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.ct) == 0:
            raise StopIteration
        x = self.pop()
        return x

    @abstractmethod
    def pop(self):
        """Selects, removes, and returns a path on the frontier if there is
        any.Recall that a path is a sequence (tuple) of Arc
        objects. Override this method to achieve a desired search
        strategy.
        """


class DFSFrontier(FSFrontier):
    def __init__(self):
        self.ct = collections.deque()

    def add(self, path):
        self.ct.append(path)
        print(f"+{strpath(path)}")

    def pop(self):
        x = self.ct.pop()
        print(f"-{strpath(x)}")
        return x


class BFSFrontier(FSFrontier):
    def __init__(self):
        self.ct = collections.deque()

    def add(self, path):
        self.ct.append(path)
        print(f"+{strpath(path)}")

    def pop(self):
        x = self.ct.popleft()
        print(f"-{strpath(x)}")
        return x


def cost(path):
    """simple sum of arc costs"""
    return sum(arc.cost for arc in path)


class LCFSFrontier(FSFrontier):
    def __init__(self):
        self.ct = []
        self.i = itertools.count()

    def add(self, path):
        heappush(self.ct, (cost(path), next(self.i), path))
        # print(f"+{strpathc(path)}")

    def pop(self):
        cost, i, path = heappop(self.ct)
        # print(f"-{strpathc(path)}")
        return path


def h(node):
    """put your hueristic function here"""
    estimates={'A': 6, 'B': 3, 'C': 2, 'D': 1, 'G': 0}
    return estimates[node]


def f(path):
    return cost(path) + h(end_node(path))


class AStarFrontier(FSFrontier):
    def __init__(self):
        self.ct = []
        self.i = itertools.count()

    def add(self, path):
        heappush(self.ct, (f(path), next(self.i), path))
        print(f"+{strpathh(path, f(path))}")

    def pop(self):
        cost, i, path = heappop(self.ct)
        print(f"-{strpathh(path, cost)}")
        return path


def end_node(path):
    return path[-1].head


class LCFSFrontierWithPruning(FSFrontier):

    def __init__(self):
        self.ct = []
        self.i = itertools.count()
        self.considered = set()

    def add(self, path):
        if end_node(path) in self.considered:
            print(f"+{strpathc(path)}!")
            return
        cost = sum([arc.cost for arc in path])
        heappush(self.ct, (cost, next(self.i), path))
        print(f"+{strpathc(path)}")

    def pop(self):
        flag = True
        while flag:
            cost, i, path = heappop(self.ct)
            flag = end_node(path) in self.considered
            if flag:
                print(f"-{strpathc(path)}!")

        self.considered.add(end_node(path))
        print(f"-{strpathc(path)}")
        return path


class AStarFrontierWithPruning(FSFrontier):
    def __init__(self):
        self.ct = []
        self.i = itertools.count()
        self.considered = set()

    def add(self, path):
        if end_node(path) in self.considered:
            print(f"+{strpathh(path, f(path))}!")
            return
        heappush(self.ct, (f(path), next(self.i), path))
        print(f"+{strpathh(path, f(path))}")

    def pop(self):
        flag = True
        while flag:
            cost, i, path = heappop(self.ct)
            flag = end_node(path) in self.considered
            if flag:
                print(f"-{strpathh(path, cost)}!")

        self.considered.add(end_node(path))
        print(f"-{strpathh(path, cost)}")
        return path


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


def action_str(tail, head):
    return f"{tail}->{head}"


def euc_dist(pt1, pt2):
    return math.sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)


class LocationGraph(Graph):
    def __init__(self, location, radius, starting_nodes, goal_nodes):
        self.location = location
        self.radius = radius
        self._starting_nodes = starting_nodes
        self.goal_nodes = goal_nodes

    def starting_nodes(self):
        return self._starting_nodes

    def is_goal(self, node):
        return node in self.goal_nodes

    def outgoing_arcs(self, tail):
        arcs = []
        t_pt = self.location[tail]
        for head, h_pt in self.location.items():
            if head == tail:
                continue
            dist = euc_dist(t_pt, h_pt)
            if dist > self.radius:
                continue
            arcs.append(Arc(tail, head, action_str(tail, head), dist))

        arcs.sort(key=lambda arc: arc.head)
        return arcs
