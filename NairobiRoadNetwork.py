import networkx as nx
import matplotlib.pyplot as plt
from classes.bfs import BfsTraverser
from classes.ucs import UCS

nodes = ["Karen", "J6", "Gitaru", "J1", "J4", "J7"]

G = nx.Graph()
G.add_nodes_from(nodes)
G.nodes()  # confirm nodes

# Add Edges and their weights
G.add_edge("Karen", "J1", weight="2")
G.add_edge("Karen", "J6", weight="4")
G.add_edge("J1", "J4", weight="2")
G.add_edge("J6", "Gitaru", weight="10")
G.add_edge("J6", "J7", weight="6")
G.add_edge("J6", "J4", weight="6")
G.add_edge("Gitaru", "J7", weight="6")

# position the nodes to resemble Nairobis map
G.node["Karen"]['pos'] = (0, 0)
G.node["J6"]['pos'] = (0, 2)
G.node["J1"]['pos'] = (2, -2)
G.node["J4"]['pos'] = (4, -2)
G.node["J7"]['pos'] = (0, 4)
G.node["Gitaru"]['pos'] = (-1, 3)

# store all positions in a variable
node_pos = nx.get_node_attributes(G, 'pos')

route_bfs = BfsTraverser()
routes = route_bfs.BFS(G, "Karen", "Gitaru")
print(route_bfs.visited)
route_list = route_bfs.visited

# color the nodes in the route_bfs
node_col = ['darkturquoise' if not node in route_list else 'red' for node in G.nodes()]
peru_colored_edges = list(zip(route_list, route_list[1:]))
# print('route_list', route_list)
# print('route_list[1:]', route_list[1:])
# print('edges ->', peru_colored_edges)

# color the edges as well
# edge_col = ['darkturquoise' if not edge in peru_colored_edges else 'peru' for edge in G.edges()]
# arc_weight = nx.get_edge_attributes(G, 'weight')
# nx.draw_networkx(G, node_pos, node_color=node_col, node_size=450)
# nx.draw_networkx_edges(G, node_pos, width=2, edge_color=edge_col)
# nx.draw_networkx_edge_labels(G, node_pos, edge_color=edge_col, edge_labels=arc_weight)
# plt.axis('off')
# plt.show()

ucs = UCS()
print(ucs.ucs(G, 'Karen', 'Gitaru'))
print(ucs.visited)

node_colors = ['darkturquoise' if n not in ucs.visited else 'peru' for n in G.nodes()]
arc_weight = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx(G, node_pos, node_color=node_colors, node_size=450)
plt.axis('off')
plt.show()