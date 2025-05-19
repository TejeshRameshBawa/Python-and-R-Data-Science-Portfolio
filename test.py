import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.patches import Rectangle

# Initialize the graph
MyGraph = nx.Graph()

# Add nodes with specific positions and colors for each line
# District Line (green)
MyGraph.add_node('A', npos=(10, 30), ccn='#007d32')
MyGraph.add_node('B', npos=(30, 30), ccn='#007d32')
MyGraph.add_node('C', npos=(40, 30), ccn='#007d32')
MyGraph.add_node('D', npos=(60, 30), ccn='#007d32')
MyGraph.add_node('E', npos=(70, 30), ccn='#007d32')

# Piccadilly Line (blue)
MyGraph.add_node('A', npos=(10, 30), ccn='#0019a8')
MyGraph.add_node('B', npos=(30, 30), ccn='#0019a8')
MyGraph.add_node('F', npos=(50, 50), ccn='#0019a8')
MyGraph.add_node('G', npos=(60, 50), ccn='#0019a8')
MyGraph.add_node('H', npos=(70, 55), ccn='#0019a8')

# Define edges with colors
MyGraph.add_edge('A', 'B', cce='#007d32')
MyGraph.add_edge('B', 'C', cce='#007d32')
MyGraph.add_edge('C', 'D', cce='#007d32')
MyGraph.add_edge('D', 'E', cce='#007d32')
MyGraph.add_edge('A', 'B', cce='#0019a8')
MyGraph.add_edge('B', 'F', cce='#0019a8')

# Get positions, node colors, and edge colors
pos = nx.get_node_attributes(MyGraph, 'npos')
edgecolor = list(nx.get_edge_attributes(MyGraph, 'cce').values())

# Draw edges and labels
fig, ax = plt.subplots()
nx.draw_networkx_edges(MyGraph, pos, edge_color=edgecolor, ax=ax)
nx.draw_networkx_labels(MyGraph, pos, font_size=8, font_color="black", ax=ax)

# Draw shared nodes explicitly with rectangles
ax.add_patch(Rectangle((8, 28), 2, 4, color='#007d32', ec='black', lw=0.5))  # District line color for node 'A'
ax.add_patch(Rectangle((10, 28), 2, 4, color='#0019a8', ec='black', lw=0.5))  # Piccadilly line color for node 'A'

ax.add_patch(Rectangle((28, 28), 2, 4, color='#007d32', ec='black', lw=0.5))  # District line color for node 'B'
ax.add_patch(Rectangle((30, 28), 2, 4, color='#0019a8', ec='black', lw=0.5))  # Piccadilly line color for node 'B'

# Draw non-shared nodes
nx.draw_networkx_nodes(MyGraph, pos, nodelist=['C', 'D', 'E'], node_color=['#007d32'], ax=ax)
nx.draw_networkx_nodes(MyGraph, pos, nodelist=['F', 'G', 'H'], node_color=['#0019a8'], ax=ax)

plt.title("Subway Network with Custom Symbols for Shared Stations")
plt.axis('off')
plt.show()
