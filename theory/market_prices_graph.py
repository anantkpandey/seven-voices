# market_prices_graph.py - Market Prices with Graph Theory
# For King Bran Stark, counseled by Tyrion, Hand of the King, April 10, 2025

import networkx as nx
import matplotlib.pyplot as plt
import random
import time

class MarketGraph:
    def __init__(self):
        # Create directed graph
        self.G = nx.DiGraph()
        # Initial goods and prices
        self.goods = {
            "grain": 10.0,
            "steel": 25.0,
            "wine": 15.0,
            "bread": 5.0
        }
        # Add nodes (goods) with prices
        for good, price in self.goods.items():
            self.G.add_node(good, price=price)
        # Add edges (trade links) with weights (influence)
        self.G.add_edge("grain", "bread", weight=0.5)  # Grain affects bread
        self.G.add_edge("steel", "bread", weight=0.2)  # Steel tools for baking
        self.G.add_edge("wine", "bread", weight=0.1)  # Wine with bread

    def update_prices(self):
        """Update prices with random shifts and propagate via edges."""
        for node in self.G.nodes:
            # Random price shift: ±10%
            change = self.goods[node] * random.uniform(-0.1, 0.1)
            self.goods[node] = round(self.goods[node] + change, 2)
            self.G.nodes[node]["price"] = self.goods[node]
        
        # Propagate changes along edges
        for u, v, data in self.G.edges(data=True):
            influence = data["weight"]
            base_price = self.goods[u]
            self.goods[v] += round(base_price * influence * random.uniform(0.05, 0.15), 2)
            self.goods[v] = round(self.goods[v], 2)
            self.G.nodes[v]["price"] = self.goods[v]

    def traverse_and_report(self):
        """Traverse graph and report prices."""
        print("\nMarket Prices Report:")
        for node in nx.dfs_preorder_nodes(self.G, source="grain"):  # Depth-first from grain
            price = self.G.nodes[node]["price"]
            print(f"{node.capitalize()}: {price} gold")
        print("Trade Links:")
        for u, v, data in self.G.edges(data=True):
            print(f"{u} -> {v} (weight: {data['weight']})")

    def plot_graph(self):
        """Visualize the graph with prices."""
        pos = nx.spring_layout(self.G)
        prices = [self.G.nodes[n]["price"] for n in self.G.nodes]
        nx.draw(self.G, pos, with_labels=True, node_color="lightblue", 
                node_size=800, font_size=10, font_weight="bold")
        nx.draw_networkx_labels(self.G, pos, labels={n: f"{n}\n{self.G.nodes[n]['price']}" for n in self.G.nodes})
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels={(u, v): f"{d['weight']}" for u, v, d in self.G.edges(data=True)})
        plt.title("King Bran’s Market Network")
        plt.show()

    def run(self):
        print("Initial Market:", self.goods)
        for _ in range(3):  # 3 updates
            print("\nUpdating prices...")
            self.update_prices()
            self.traverse_and_report()
            time.sleep(1)  # Simulate delay
        print("\nPlotting market graph...")
        self.plot_graph()

# Run the market graph
if __name__ == "__main__":
    market = MarketGraph()
    market.run()