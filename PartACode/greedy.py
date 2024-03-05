import networkx as nx
import random
import matplotlib.pyplot as plt

def greedy(graph):
    colours = {}
    for node in graph.nodes:
        neighbour_colours = {colours[neighbour] for neighbour in graph.neighbors(node) if neighbour in colours}
        available_colours = set(range(len(neighbour_colours)+1))
        colours[node] = min(available_colours - neighbour_colours)
    return colours

def count_conflicts(graph, colours):
    conflict_count = 0
    for edge in graph.edges:
        if colours[edge[0]] == colours[edge[1]]:
            conflict_count += 1
    return conflict_count

g = nx.random_geometric_graph(20,0.3)

colours = greedy(g)

initial_conflicts = count_conflicts(g,colours)

plt.figure(figsize=(8,6))
pos = nx.spring_layout(g)
nx.draw(g, pos, with_labels=True, node_color=[colours[node] for node in g.nodes])
plt.title('Greedy Colouring Algorithm')
plt.show()

num_iterations = 100
conflicts_over_time = [initial_conflicts]
for i in range(num_iterations):
    node = random.choice(list(g.nodes))
    old_colour = colours[node]
    neighbour_colours = {colours[neighbour] for neighbour in g.neighbors(node) if neighbour in colours}
    available_colours = set(range(len(neighbour_colours)+1))
    new_colour = min(available_colours - neighbour_colours)
    colours[node] = new_colour
    conflict_count = count_conflicts(g, colours)
    conflicts_over_time.append(conflict_count)

plt.plot(range(num_iterations + 1), conflicts_over_time)
plt.xlabel('Iteration')
plt.ylabel('Number of Conflicts')
plt.title('Conflicts over Time (Greedy Colouring)')
plt.show()
