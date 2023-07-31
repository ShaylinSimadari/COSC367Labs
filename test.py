from search import *
from student_answer import DFSFrontier
from student_answer import BFSFrontier
from student_answer import FunkyNumericGraph
from itertools import dropwhile
from student_answer import SlidingPuzzleGraph


def main():

    # graph = ExplicitGraph(nodes=set('SAG'),
    #                       edge_list=[('S', 'A'), ('S', 'G'), ('A', 'G')],
    #                       starting_nodes=['S'],
    #                       goal_nodes={'G'})
    #
    # solutions = generic_search(graph, DFSFrontier())
    # solution = next(solutions, None)
    # print_actions(solution)
    #
    # graph = ExplicitGraph(nodes=set('SAG'),
    #                       edge_list=[('S', 'G'), ('S', 'A'), ('A', 'G')],
    #                       starting_nodes=['S'],
    #                       goal_nodes={'G'})
    #
    # solutions = generic_search(graph, DFSFrontier())
    # solution = next(solutions, None)
    # print_actions(solution)
    #
    # available_flights = ExplicitGraph(
    #     nodes=['Christchurch', 'Auckland',
    #            'Wellington', 'Gold Coast'],
    #     edge_list=[('Christchurch', 'Gold Coast'),
    #                ('Christchurch', 'Auckland'),
    #                ('Christchurch', 'Wellington'),
    #                ('Wellington', 'Gold Coast'),
    #                ('Wellington', 'Auckland'),
    #                ('Auckland', 'Gold Coast')],
    #     starting_nodes=['Christchurch'],
    #     goal_nodes={'Gold Coast'})
    #
    # my_itinerary = next(generic_search(available_flights, DFSFrontier()), None)
    # print_actions(my_itinerary)

    # graph = ExplicitGraph(nodes=set('SAG'),
    #                       edge_list=[('S', 'A'), ('S', 'G'), ('A', 'G')],
    #                       starting_nodes=['S'],
    #                       goal_nodes={'G'})
    #
    # solutions = generic_search(graph, BFSFrontier())
    # solution = next(solutions, None)
    # print_actions(solution)
    #
    # flights = ExplicitGraph(nodes=['Christchurch', 'Auckland',
    #                                'Wellington', 'Gold Coast'],
    #                         edge_list=[('Christchurch', 'Gold Coast'),
    #                                    ('Christchurch', 'Auckland'),
    #                                    ('Christchurch', 'Wellington'),
    #                                    ('Wellington', 'Gold Coast'),
    #                                    ('Wellington', 'Auckland'),
    #                                    ('Auckland', 'Gold Coast')],
    #                         starting_nodes=['Christchurch'],
    #                         goal_nodes={'Gold Coast'})
    #
    # my_itinerary = next(generic_search(flights, BFSFrontier()), None)
    # print_actions(my_itinerary)

    # graph = FunkyNumericGraph(4)
    # for node in graph.starting_nodes():
    #     print(node)

    # graph = FunkyNumericGraph(3)
    # solutions = generic_search(graph, BFSFrontier())
    # print_actions(next(dropwhile(lambda path: path[-1].head <= 10, solutions)))

    # graph = SlidingPuzzleGraph([[1, 2, 5],
    #                             [3, 4, 8],
    #                             [6, 7, ' ']])
    #
    # solutions = generic_search(graph, BFSFrontier())
    # print_actions(next(solutions))

    # graph = SlidingPuzzleGraph([[3,' '],
    #                              [1, 2]])
    #
    # solutions = generic_search(graph, BFSFrontier())
    # print_actions(next(solutions))

    # graph = SlidingPuzzleGraph([[1, ' ', 2],
    #                             [6, 4, 3],
    #                             [7, 8, 5]])

    # solutions = generic_search(graph, BFSFrontier())
    # print_actions(next(solutions))

    graph = \
        ExplicitGraph(
            nodes={'S', 'A', 'B', 'G'},
            edge_list=[('A', 'B'), ('S', 'A'), ('S', 'G'), ('B', 'G')],
            starting_nodes=['S'],
            goal_nodes={'G'}, )
    solutions = generic_search(graph, BFSFrontier())
    print_actions(next(solutions))

if __name__ == "__main__": main()