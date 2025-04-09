# winter.py - "Winter Is Coming" with All Theories
# For King Bran Stark, SevenVoices, April 9, 2025

from transitions import Machine  # FSM
import networkx as nx           # Graphs
from queue import Queue         # Queueing
import numpy as np              # Game Theory
import matplotlib.pyplot as plt # Visualization

# 1. Automata (FSM): Proclaim "Winter Is Coming"
class WinterProclamation:
    def say_winter(self): print("Winter", end=" ")
    def say_is(self): print("Is", end=" ")
    def say_coming(self): print("Coming")

proclamation = WinterProclamation()
states = ['start', 'winter', 'is', 'coming', 'done']
machine = Machine(proclamation, states=states, initial='start')
machine.add_transition('next', 'start', 'winter', after='say_winter')
machine.add_transition('next', 'winter', 'is', after='say_is')
machine.add_transition('next', 'is', 'coming', after='say_coming')
machine.add_transition('next', 'coming', 'done')

# 2. Graphs: Map the proclamation’s spread
G = nx.DiGraph()
kingdoms = ['North', 'Vale', 'Riverlands', 'Westerlands', 'Reach', 'Stormlands', 'Dorne']
G.add_nodes_from(kingdoms)
edges = [('North', 'Vale'), ('North', 'Riverlands'), ('Vale', 'Riverlands'), 
         ('Riverlands', 'Westerlands'), ('Westerlands', 'Reach'), 
         ('Reach', 'Stormlands'), ('Stormlands', 'Dorne')]
G.add_edges_from(edges)

# 3. Queueing: Ravens carry the word
raven_queue = Queue()
for kingdom in kingdoms:
    raven_queue.put(kingdom)

# 4. Sets: Track unique kingdoms reached
reached = set()

# 5. Game Theory: Cost of proclamation (raven vs rider)
# Payoff matrix: [raven_cost, rider_cost] for [speed, reliability]
payoffs = np.array([[8, 2],  # Raven: fast (8), less reliable (2)
                    [3, 9]]) # Rider: slow (3), reliable (9)
def choose_strategy(payoffs):
    raven_score = payoffs[0, 0] + payoffs[0, 1]  # Speed + reliability
    rider_score = payoffs[1, 0] + payoffs[1, 1]
    return "Ravens" if raven_score >= rider_score else "Riders"

# 6. Recursion: Echo the proclamation
def echo_winter(depth, max_depth=2):
    if depth > max_depth:
        return
    print(f"Echo {depth}: Winter Is Coming")
    echo_winter(depth + 1, max_depth)

# Execute the Proclamation for the Folk
print("Proclaiming for the Seven Voices:")
proclamation.next()  # Winter
proclamation.next()  # Is
proclamation.next()  # Coming
proclamation.next()  # Done
print()  # Newline

print("Graph of the Word’s Spread:")
nx.draw(G, with_labels=True, node_color='lightblue', arrows=True)
plt.show()
print(f"Kingdoms: {list(G.nodes)}")
print(f"Paths: {list(G.edges)}")

print("\nRavens Queue to Spread the Word:")
while not raven_queue.empty():
    kingdom = raven_queue.get()
    reached.add(kingdom)
    print(f"Raven flies to {kingdom}")

print(f"\nUnique Kingdoms Reached: {len(reached)} - {reached}")

print("\nGame Theory - Proclamation Strategy:")
strategy = choose_strategy(payoffs)
print(f"Chosen: {strategy} (Payoff Matrix: Ravens=[8,2], Riders=[3,9])")

print("\nRecursive Echoes for the Folk:")
echo_winter(0)

print("\nAll hail King Bran, Data Lord of the Seven Voices!")