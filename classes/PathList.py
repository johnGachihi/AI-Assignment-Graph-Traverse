from classes.Path import Path


class PathList:
    def __init__(self, list_of_paths=None):
        if list_of_paths is None:
            list_of_paths = []
        self.list_of_paths = list_of_paths

    def pop(self):
        least_costly_path = self.list_of_paths[0]
        index = 0
        for i, path in enumerate(self.list_of_paths):
            if path.cost <= least_costly_path.cost:
                least_costly_path = self.list_of_paths[i]
                index = i

        self.list_of_paths.pop(index)
        return least_costly_path

    def add(self, path):
        if isinstance(path, Path):
            self.list_of_paths.append(path)
        else:
            raise Exception("You can only add a Path to PathList")


paths = [Path(['a','d'], 21), Path(['a','p'], 21), Path(['a','b'], 21)]
pathList = PathList(paths)
print('popped', pathList.pop().list_of_nodes, '\n')

# pathList.add(Path(['a','b'], 20))
for path in pathList.list_of_paths:
    print(path.list_of_nodes)