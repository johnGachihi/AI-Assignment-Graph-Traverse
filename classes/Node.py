import heapq


class Node:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        

class NodesPriorityQueue:
    def __init__(self):
        self.queue = []
        
    def add(self, node):
        if isinstance(node, Node):
            heapq.heappush(self.queue, 1)
        else:
            raise Exception('Parameter requires a Node object')

    def print(self):
        print(self.queue)

q = NodesPriorityQueue()
q.add(Node('ble', 20))
q.add(Node('cle', 20))
q.add(Node('dle', 20))
q.print()