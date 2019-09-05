class BfsTraverser:

    def __init__(self):
        self.visited = []
        self.end_search = False

    def BFS(self, graph, start_node, goal_node):
        queue = [start_node]

        # set of visited nodes
        self.visited.append(start_node)

        while queue and not self.end_search:
            # Dequeue a vertex
            cur_node = queue.pop(0)
            print("\nDrive to", cur_node, " Estate", end="\n")

            # Get all adjacent vertices of `cur_node`. If a adjacent
            # has not been visited, then mark it visited and enqueue it
            print(graph[cur_node])
            for i in graph[cur_node]:  #Loop through list of adjacent nodes
                print('i', i)
                print('weight', graph[cur_node][i]['weight'])
                if i not in self.visited:
                    print("Goal node:", goal_node, " Current Node:", i)
                    if i is goal_node:
                        self.end_search = True
                    else:
                        queue.append(i)

                    self.visited.append(i)
                    print('Hapa', self.end_search)
        # return visited
