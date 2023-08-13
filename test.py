from search import *
from student_answer import DFSFrontier, LCFSFrontierWithPruning, LCFSFrontier, AStarFrontier, AStarFrontierWithPruning, \
    LocationGraph
from student_answer import BFSFrontier
from student_answer import FunkyNumericGraph
from itertools import dropwhile
from student_answer import SlidingPuzzleGraph


def main():
    graph = LocationGraph(
        location={'A': (25, 7),
                  'B': (1, 7),
                  'C': (13, 2),
                  'D': (37, 2)},
        radius=15,
        starting_nodes=['B'],
        goal_nodes={'D'}
    )

    solution = next(generic_search(graph, LCFSFrontier()))
    print_actions(solution)

if __name__ == "__main__": main()