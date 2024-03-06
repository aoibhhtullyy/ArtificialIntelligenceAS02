import networkx as nx
import random
import matplotlib.pyplot as plt

g = nx.barabasi_albert_graph(20,3)

colours = {}
for node in g.nodes:
    colours[node] = random.choice(['red', 'green', 'blue', 'yellow'])

plt.figure(figsize=(8,6))
pos = nx.spring_layout(g)
nx.draw(g, pos, with_labels=True, node_color = [colours[node] for node in g.nodes])
plt.title('Small World Network Graph')
plt.show()

def conflicts(g, colours):
    conflict_count = 0
    for edge in g.edges:
        if colours[edge[0]] == colours[edge[1]]:
            conflict_count += 1
    return conflict_count

num_iterations = 100
conflicts_over_time = []

for i in range(num_iterations):
    node = random.choice(list(g.nodes))
    old_colour = colours[node]
    new_colour = random.choice(['red', 'green', 'blue', 'yellow'])
    colours[node] = new_colour
    conflict_count = conflicts(g,colours)
    conflicts_over_time.append(conflict_count)

plt.plot(range(num_iterations), conflicts_over_time)
plt.xlabel('Iteration')
plt.ylabel('Number of Conflicts')
plt.title('Conflicts over time')
plt.show()