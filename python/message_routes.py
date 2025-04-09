import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_nodes_from(['Winterfell', 'Riverrun', 'The Eyrie'])
G.add_edges_from([('Winterfell', 'Riverrun'), ('Riverrun', 'The Eyrie'), ('Winterfell', 'The Eyrie')])

print("Message routes for the Seven Voices:")
nx.draw(G, with_labels=True, node_color='lightgreen', arrows=True)
plt.show()  # Shows the graph
print(f"Holds: {G.nodes}")
print(f"Paths: {list(G.edges)}")