# market_game.py - Simulate market price updates with Game Theory
# For King Bran Stark, counseled by Tyrion, Hand of the King, April 10, 2025

import random
import pandas as pd

# Define the game
class MarketGame:
    def __init__(self):
        # Strategies: High (H) or Low (L) price
        self.strategies = ["H", "L"]
        # Payoff matrix: (Merchant A profit, Merchant B profit)
        self.payoffs = {
            ("H", "H"): (10, 10),  # Both high: moderate profit
            ("H", "L"): (5, 15),  # A high, B low: B undercuts, wins
            ("L", "H"): (15, 5),  # A low, B high: A undercuts, wins
            ("L", "L"): (8, 8)    # Both low: low profit, high volume
        }
        # Price mapping
        self.price_map = {"H": 20.0, "L": 10.0}

    def play_round(self):
        # Random initial strategies
        a_strategy = random.choice(self.strategies)
        b_strategy = random.choice(self.strategies)
        return a_strategy, b_strategy, self.payoffs[(a_strategy, b_strategy)]

    def find_nash(self):
        # Check for Nash equilibrium (simplified: pure strategy)
        nash = []
        for a in self.strategies:
            for b in self.strategies:
                a_pay, b_pay = self.payoffs[(a, b)]
                # A won’t switch if a_pay >= other options given B’s choice
                # B won’t switch if b_pay >= other options given A’s choice
                a_better = all(a_pay >= self.payoffs[(x, b)][0] for x in self.strategies)
                b_better = all(b_pay >= self.payoffs[(a, y)][1] for y in self.strategies)
                if a_better and b_better:
                    nash.append((a, b))
        return nash

# Simulate market updates
game = MarketGame()
history = []
for day in range(5):  # 5 days
    a_strat, b_strat, (a_pay, b_pay) = game.play_round()
    a_price = game.price_map[a_strat]
    b_price = game.price_map[b_strat]
    history.append({
        "Day": day + 1,
        "A Strategy": a_strat,
        "A Price": a_price,
        "A Payoff": a_pay,
        "B Strategy": b_strat,
        "B Price": b_price,
        "B Payoff": b_pay
    })

# Report
print("Market Price Game Simulation (5 Days):")
for round in history:
    print(f"Day {round['Day']}: A sets {round['A Price']} (Payoff: {round['A Payoff']}), "
          f"B sets {round['B Price']} (Payoff: {round['B Payoff']})")

nash = game.find_nash()
print("\nNash Equilibria (Stable Strategies):")
for a, b in nash:
    print(f"A: {game.price_map[a]}, B: {game.price_map[b]}")

# Export to Excel
df = pd.DataFrame(history)
df.to_excel("docs/market_game.xlsx", index=False)
print("\nSimulation saved to SevenVoices/docs/market_game.xlsx, Your Grace!")