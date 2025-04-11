# Note: Requires networkx and matplotlib. Install via:
# pip install networkx matplotlib

import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

class SoldierShiftGraph:
    def __init__(self, soldiers):
        """Initialize graph with soldiers and shifts."""
        self.soldiers = soldiers
        self.shifts = ["Day", "Night"]
        self.graph = defaultdict(list)
        self.nx_graph = nx.DiGraph()  # NetworkX directed graph for visualization
        self.build_graph()

    def build_graph(self):
        """Construct directed graph of (soldier, shift) states."""
        for i, soldier in enumerate(self.soldiers):
            next_soldier = self.soldiers[(i + 1) % len(self.soldiers)]  # Circular rotation
            for shift in self.shifts:
                current_state = (soldier, shift)
                next_shift = "Night" if shift == "Day" else "Day"
                next_state = (next_soldier, next_shift)
                # Add to adjacency list
                self.graph[current_state].append(next_state)
                # Add to NetworkX graph
                self.nx_graph.add_node(current_state, shift=shift)
                self.nx_graph.add_node(next_state, shift=next_shift)
                self.nx_graph.add_edge(current_state, next_state)

    def cycle_shifts(self, start_state, num_transitions):
        """Cycle through shift assignments starting from start_state."""
        current_state = start_state
        history = [current_state]
        print(f"Starting: Soldier: {current_state[0]}, Shift: {current_state[1]}")

        for i in range(num_transitions):
            if self.graph[current_state]:
                current_state = self.graph[current_state][0]  # Follow first (only) edge
                history.append(current_state)
                print(f"Transition {i+1}: Soldier: {current_state[0]}, Shift: {current_state[1]}")
            else:
                print("No further transitions possible.")
                break

        return history

    def visualize_graph(self):
        """Visualize the shift assignment graph using Matplotlib and NetworkX."""
        # Set node colors based on shift
        node_colors = []
        for node in self.nx_graph.nodes:
            shift = self.nx_graph.nodes[node]["shift"]
            node_colors.append("lightblue" if shift == "Day" else "lightcoral")

        # Set node labels as "soldier:shift"
        labels = {node: f"{node[0]}:{node[1]}" for node in self.nx_graph.nodes}

        # Use circular layout to emphasize cycle
        pos = nx.spring_layout(self.nx_graph, k=0.5, iterations=50)

        plt.figure(figsize=(12, 8))
        nx.draw(
            self.nx_graph,
            pos,
            with_labels=True,
            labels=labels,
            node_color=node_colors,
            node_size=2000,
            font_size=10,
            font_weight="bold",
            edge_color="gray",
            arrows=True,
            arrowstyle="->",
            arrowsize=20
        )
        plt.title("Soldier Shift Assignment Graph", fontsize=14, pad=20)
        plt.show()

def main():
    # Soldier roster
    soldiers = ["Ser Jaime", "Ser Brienne", "Ser Davos", "Ser Jorah", "Ser Tormund"]
    graph = SoldierShiftGraph(soldiers)

    # Start with first soldier on Day Shift
    start_state = (soldiers[0], "Day")
    
    print("Cycling through soldier shift assignments:")
    # Simulate 8 transitions (4 days, day and night shifts)
    graph.cycle_shifts(start_state, num_transitions=8)

    print("\nGenerating graph visualization...")
    graph.visualize_graph()

if __name__ == "__main__":
    main()