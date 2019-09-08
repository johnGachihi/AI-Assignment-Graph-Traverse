import heapq
from constants.Node import Node

class UCS:

    def __init__(self):
        self.visited = []
        self.end_reached = False
        self.paths = []

    def ucs(self, graph, start_node, end_node):
        node = (0, start_node)
        frontier = [node]   #Nodes to explore
        explored = set()   #Set of explored nodes

        paths = [(0, [start_node])]

        while True:
            if not frontier:
                return 'Not found'  # Work on this

            node = frontier.pop(0)
            # current_path = paths.pop(0)
            explored.add(node[Node.NAME])
            print('We drive to:', node[Node.NAME], ' explored', explored, ' frontier', frontier)

            if node[Node.NAME] == end_node:
                self.visited = explored
                return 'Complete'   # Work on this

            for child in graph[node[Node.NAME]].items():
                # print('blebleble', child[1]['weight'], child[0])
                child_weight = float(child[1]['weight']) + node[Node.WEIGHT]
                child_in_frontier = self.isValuePresentInTupleList(frontier, Node.NAME, child[0])
                # nodes_of_cur_path = current_path[1]
                # print('nodes_of_cur_path', nodes_of_cur_path)
                # print('child_in_frontier', child[0], child_in_frontier)
                if child[0] not in explored and child_in_frontier == -1:
                    print('We peer at child node:', child[0], ' Weight:', child_weight)
                    heapq.heappush(frontier, (child_weight, child[0]))
                    # heapq.heappush(paths, (child_weight, current_path[1].append(child[0])))
                elif child_in_frontier != -1 and frontier[child_in_frontier][Node.WEIGHT] > child_weight:
                    # print('Child in frontier', frontier[child_in_frontier][Node.WEIGHT], child_weight)
                    # frontier[child_in_frontier][Node.WEIGHT] = child_weight
                    frontier[child_in_frontier] = (child_weight, frontier[child_in_frontier][Node.NAME])

    @staticmethod
    def isValuePresentInTupleList(tuple_list, tuple_index, value):
        for i, val in enumerate(tuple_list):
            if val[tuple_index] == value:
                return i

        return -1



a_list_of_tuples = [(1, 'a'), (2, 'b'), (3, 'c')]
b = UCS.isValuePresentInTupleList(a_list_of_tuples, 1, 'd')
print(b)
if b == -1:
    print('Condition is true')
else:
    print('Condition is false')
