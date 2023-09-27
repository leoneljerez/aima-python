# UNC Charlotte
# ITCS 5153 - Applied AI - Fall 2023
# Lab 2
# Solving problems using search from the AIMA book's code
# Student ID: 800908508

from search import GraphProblem, InstrumentedProblem, romania_map, compare_searchers, breadth_first_graph_search, depth_first_graph_search


problem_arad = GraphProblem('Arad','Lugoj', romania_map)
problem_craiova = GraphProblem('Craiova','Oradea', romania_map)
problem_sibiu = GraphProblem('Sibiu','Bucharest', romania_map)

print('Test 1 - Comparing graph search algorithms using a simplified map of Romania...')
compare_searchers(problems=[problem_arad, problem_craiova, problem_sibiu], 
                  header=['Searcher', 'romania_map(Arad, Lugoj)', 'romania_map(Craiova, Oradea)', 'romania_map(Sibiu, Bucharest)'])


def test_paths(string_title, string_subheading, problem, search):
    print('\n')
    print(string_title)
    print(string_subheading)
    init = InstrumentedProblem(problem)
    result = search(init)
    print('Path followed:', result.path())
    print('Total miles:', result.path_cost)


test_paths('Test 2 - Finding a path from Arad to Lugoj...', 'Using breadth-first graph search:', problem_arad, breadth_first_graph_search)
test_paths('Test 3 - Finding a path from Caroiva to Oradea...', 'Using breadth-first graph search:', problem_craiova, breadth_first_graph_search)
test_paths('Test 4 - Finding a path from Sibiu to Bucharest...', 'Using breadth-first graph search:', problem_sibiu, breadth_first_graph_search)
test_paths('Test 5 - Finding a path from Sibiu to Bucharest...', 'Using depth-first graph search:', problem_sibiu, depth_first_graph_search)

print('\n', 'Done!')