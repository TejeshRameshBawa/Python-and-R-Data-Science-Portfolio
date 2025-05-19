import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.patches import Rectangle, Patch

MyGraph = nx.Graph()

# District Line nodes
MyGraph.add_node('S', npos=(-20, 30), ccn='#007d32')
MyGraph.add_node('A-D', npos=(0, 30), ccn='#007d32')
MyGraph.add_node('B-D', npos=(20, 30), ccn='#007d32')
MyGraph.add_node('C', npos=(40, 30), ccn='#007d32')
MyGraph.add_node('D-D', npos=(60, 30), ccn='#007d32')
MyGraph.add_node('E-D', npos=(76, 30), ccn='#007d32')

# Piccadilly Line nodes
MyGraph.add_node('P', npos=(0, 60), ccn='#0019a8')
MyGraph.add_node('A-P', npos=(0, 35), ccn='#0019a8')
MyGraph.add_node('B-P', npos=(20, 35), ccn='#0019a8')
MyGraph.add_node('F-P', npos=(37, 50), ccn='#0019a8')
MyGraph.add_node('G-P', npos=(60, 50), ccn='#0019a8')
MyGraph.add_node('H-P', npos=(76, 67), ccn='#0019a8')

# Jubilee Line nodes
MyGraph.add_node('I-J', npos=(35, 80), ccn='#a1a5a7')
MyGraph.add_node('F-J', npos=(41, 50), ccn='#a1a5a7')
MyGraph.add_node('D-J', npos=(60, 35), ccn='#a1a5a7')
MyGraph.add_node('J-J', npos=(76, 5), ccn='#a1a5a7')
MyGraph.add_node('K', npos=(95, 15), ccn='#a1a5a7')
MyGraph.add_node('Q', npos=(120, 20), ccn='#a1a5a7')

# Bakerloo Line nodes
MyGraph.add_node('R', npos=(20, 90), ccn='#b26300')
MyGraph.add_node('I-B', npos=(35, 85), ccn='#b26300')
MyGraph.add_node('L', npos=(55, 70), ccn='#b26300')
MyGraph.add_node('G-B', npos=(60, 55), ccn='#b26300')
MyGraph.add_node('M-B', npos=(76, 50), ccn='#b26300')
MyGraph.add_node('E-B', npos=(80, 32.5), ccn='#b26300')

# Northern Line nodes
MyGraph.add_node('O', npos=(80, 105), ccn='#000000')
MyGraph.add_node('N', npos=(80, 85), ccn='#000000')
MyGraph.add_node('H-N', npos=(80, 67), ccn='#000000')
MyGraph.add_node('M-N', npos=(80, 50), ccn='#000000')
MyGraph.add_node('E-N', npos=(80, 27.5), ccn='#000000')
MyGraph.add_node('J-N', npos=(80, 5), ccn='#000000')

# District Line edges
MyGraph.add_edge('S', 'A-D', cce='#007d32', distance='1.9 km')
MyGraph.add_edge('A-D', 'B-D', cce='#007d32', distance='1.8 km')
MyGraph.add_edge('B-D', 'C', cce='#007d32', distance='1.9 km')
MyGraph.add_edge('C', 'D-D', cce='#007d32', distance='2.8 km')
MyGraph.add_edge('D-D', 'E-D', cce='#007d32', distance='0.8 km')

# Piccadilly Line edges
MyGraph.add_edge('P', 'A-P', cce='#0019a8', distance='10.4 km')
MyGraph.add_edge('A-P', 'B-P', cce='#0019a8', distance='1.8 km')
MyGraph.add_edge('B-P', 'F-P', cce='#0019a8', distance='2.7 km')
MyGraph.add_edge('F-P', 'G-P', cce='#0019a8', distance='0.6 km')
MyGraph.add_edge('G-P', 'H-P', cce='#0019a8', distance='0.7 km')

# Jubilee Line edges
MyGraph.add_edge('I-J', 'F-J', cce='#a1a5a7', distance='2.4 km')
MyGraph.add_edge('F-J', 'D-J', cce='#a1a5a7', distance='2.1 km')
MyGraph.add_edge('D-J', 'J-J', cce='#a1a5a7', distance='1.1 km')
MyGraph.add_edge('J-J', 'K', cce='#a1a5a7', distance='12 km')
MyGraph.add_edge('K', 'Q', cce='#a1a5a7', distance='5.8 km')

# Bakerloo Line edges
MyGraph.add_edge('R', 'I-B', cce='#b26300', distance='0.5 km')
MyGraph.add_edge('I-B', 'L', cce='#b26300', distance='1.7 km')
MyGraph.add_edge('L', 'G-B', cce='#b26300', distance='0.9 km')
MyGraph.add_edge('G-B', 'M-B', cce='#b26300', distance='0.9 km')
MyGraph.add_edge('M-B', 'E-B', cce='#b26300', distance='1.3 km')

# Northern Line edges
MyGraph.add_edge('O', 'N', cce='#000000', distance='1.8 km')
MyGraph.add_edge('N', 'H-N', cce='#000000', distance='1 km')
MyGraph.add_edge('H-N', 'M-N', cce='#000000', distance='0.5 km')
MyGraph.add_edge('M-N', 'E-N', cce='#000000', distance='1.3 km')
MyGraph.add_edge('E-N', 'J-N', cce='#000000', distance='2.5 km')

# Connect shared stations
MyGraph.add_edge('A-D', 'A-P', cce='none', weight=1)  # Shared connection between District and Piccadilly
MyGraph.add_edge('B-D', 'B-P', cce='none', weight=1)  # Shared connection between District and Piccadilly
MyGraph.add_edge('D-D', 'D-J', cce='none', weight=1)  # Shared connection between District and Jubilee
MyGraph.add_edge('E-D', 'E-B', cce='none', weight=1)  # Shared connection between District and Bakerloo
MyGraph.add_edge('E-D', 'E-N', cce='none', weight=1)  # Shared connection between District and Northern
MyGraph.add_edge('E-B', 'E-N', cce='none', weight=1)  # Shared connection between Bakerloo and Northern
MyGraph.add_edge('F-P', 'F-J', cce='none', weight=1)  # Shared connection between Piccadilly and Jubilee
MyGraph.add_edge('G-P', 'G-B', cce='none', weight=1)  # Shared connection between Piccadilly and Bakerloo
MyGraph.add_edge('H-P', 'H-N', cce='none', weight=1)  # Shared connection between Piccadilly and Northern
MyGraph.add_edge('I-J', 'I-B', cce='none', weight=1)  # Shared connection between Jubilee and Bakerloo
MyGraph.add_edge('J-J', 'J-N', cce='none', weight=1)  # Shared connection between Jubilee and Northern
MyGraph.add_edge('M-B', 'M-N', cce='none', weight=1)  # Shared connection between Bakerloo and Northern

# Create a plot
fig, ax = plt.subplots()

# Extract positions and colours
pos = nx.get_node_attributes(MyGraph, 'npos')
node_list = list(nx.get_node_attributes(MyGraph, 'ccn').values())
edge_list = list(nx.get_edge_attributes(MyGraph, 'cce').values())

# Draw nodes
nx.draw_networkx_nodes(MyGraph, pos, node_color=node_list, node_size=300, ax=ax)

# Draw edges
nx.draw_networkx_edges(MyGraph, pos, edge_color=edge_list, width=3, ax=ax)

# Get distances for edge labels
edge_labels = nx.get_edge_attributes(MyGraph, 'distance')
nx.draw_networkx_edge_labels(MyGraph, pos, edge_labels=edge_labels, font_size=5, ax=ax)

# Write the Title
plt.title("London Tube Visualization", size=25)

# Plot the Legend
plt.legend(handles=[plt.Line2D([0], [0], color='#007d32', lw=4, label='District Line'),
                    plt.Line2D([0], [0], color='#0019a8', lw=4, label='Piccadilly Line'),
                    plt.Line2D([0], [0], color='#a1a5a7', lw=4, label='Jubilee Line'),
                    plt.Line2D([0], [0], color='#b26300', lw=4, label='Bakerloo Line'),
                    plt.Line2D([0], [0], color='#000000', lw=4, label='Northern Line'),
                    Patch(facecolor="none", edgecolor="black", label="Shared Stations"), ],
           loc='upper left')

# Adding Rectangle to show Shared Nodes
Earls_Court = Rectangle((-3.5, 26), 7, 13, color='none', ec="black", lw=1)
ax.add_patch(Earls_Court)

South_Kensington = Rectangle((16.5, 26), 7, 13, color='none', ec="black", lw=1)
ax.add_patch(South_Kensington)

Westminster = Rectangle((56.5, 26), 7, 13, color='none', ec="black", lw=1)
ax.add_patch(Westminster)

Piccadilly_Circus = Rectangle((56.5, 46), 7, 13, color='none', ec="black", lw=1)
ax.add_patch(Piccadilly_Circus)

Baker_Street = Rectangle((31.5, 76), 7, 13, color='none', ec="black", lw=1)
ax.add_patch(Baker_Street)

Green_Park = Rectangle((33.5, 46), 11, 8, color='none', ec="black", lw=1)
ax.add_patch(Green_Park)

Leicester_Square = Rectangle((72.5, 63), 11, 8, color='none', ec="black", lw=1)
ax.add_patch(Leicester_Square)

Charing_Cross = Rectangle((72.5, 46), 11, 8, color='none', ec="black", lw=1)
ax.add_patch(Charing_Cross)

Waterloo = Rectangle((72.5, 1), 11, 8, color='none', ec="black", lw=1)
ax.add_patch(Waterloo)

Embankment = Rectangle((72.5, 23.5), 11, 13, color='none', ec="black", lw=1)
ax.add_patch(Embankment)


# Labelling the nodes
plt.text(-20, 25, s='West\nKensington', ha='center', va='center')
plt.text(-5, 59, s='Park\nRoyal', ha='center', va='center')
plt.text(0, 23, s='Earls\nCourt', ha='center', va='center')
plt.text(20, 23, s='South\nKensington', ha='center', va='center')
plt.text(40, 25, s='Sloane\nSquare', ha='center', va='center')
plt.text(60, 23, s='West\n-minster', ha='center', va='center')
plt.text(84, 30, s='Embankment', va='center')
plt.text(78, -2, s='Waterloo', ha='center', va='center')
plt.text(95, 10, s='North\nGreenwich', ha='center', va='center')
plt.text(39, 43, s='Green\nPark', ha='center', va='center')
plt.text(60, 43, s='Piccadilly\nCircus', ha='center', va='center', size=9)
plt.text(84, 50, s='Charing\nCross', va='center')
plt.text(84, 66, s='Leicester\nSquare', va='center')
plt.text(42, 86, s='Baker\nStreet', ha='center', va='center')
plt.text(58, 75, s='Oxford\nCircus', ha='center', va='center')
plt.text(82, 85, s='Tottenham\nCourt\nRoad', va='center')
plt.text(82, 105, s='Warren\nStreet', va='center')
plt.text(20, 94, s='Marylebone', ha='center', va='center')
plt.text(120, 15, s='Canning\nTown', ha='center', va='center')

plt.axis("off")
plt.show()

is_connected = nx.is_connected(MyGraph)
print("Is the graph connected?", is_connected)
