import heapq
from constants.Node import Node

class UCS:

    def __init__(self):
        self.visited = []
        self.end_reached = False

    def ucs(self, graph, start_node, end_node):
        node = (0, start_node)
        frontier = [node]   #Nodes to explore
        explored = set()   #Set of explored nodes

        while True:
            if not frontier:
                return 'Not found'  #Work on this

            node = frontier.pop(0)
            print('We drive to:', node[Node.NAME])

            explored.add(node[Node.NAME])

            if node[Node.NAME] == end_node:
                self.visited = explored
                return 'Complete'   #Work on this

            for child in graph[node[Node.NAME]].items():
                child_weight = int(child[1]['weight']) + node[Node.WEIGHT]
                child_in_frontier = self.isValuePresentInTupleList(frontier, Node.NAME, child)
                if child[0] not in explored and not child_in_frontier:
                    print('We peer at child node:', child[0], ' Weight:', child_weight)
                    heapq.heappush(frontier, (child_weight, child[0]))
                elif child_in_frontier and child_in_frontier[Node.WEIGHT] > child_weight:
                    child_in_frontier[Node.WEIGHT] = child_weight #CRITICAL. Needs to be corrected.


    def isValuePresentInTupleList(self, tuple_list, tuple_index, value):
        for i in tuple_list:
            if i[tuple_index] == value:
                return i

        return False


