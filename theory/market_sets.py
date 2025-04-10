# market_sets.py - Simulate market price updates with Set theory
# For King Bran Stark, counseled by Tyrion, Hand of the King, April 10, 2025

import random
import pandas as pd

# Simulate initial and updated prices (gold pieces)
initial_prices = {10.0, 15.0, 20.0, 25.0}  # Yesterday’s prices (Set A)
new_updates = {15.0, 20.0, 22.5, 27.5}    # Today’s updates (Set B)

# Set operations
all_prices = initial_prices.union(new_updates)              # A ∪ B
stable_prices = initial_prices.intersection(new_updates)    # A ∩ B
dropped_prices = initial_prices.difference(new_updates)     # A - B
added_prices = new_updates.difference(initial_prices)       # B - A
changed_prices = initial_prices.symmetric_difference(new_updates)  # A △ B

# Report
print("Market Price Analysis with Set Theory:")
print(f"Initial Prices (Yesterday): {initial_prices}")
print(f"New Updates (Today): {new_updates}")
print(f"All Prices (Union): {all_prices}")
print(f"Stable Prices (Intersection): {stable_prices}")
print(f"Dropped Prices (Initial - New): {dropped_prices}")
print(f"Added Prices (New - Initial): {added_prices}")
print(f"Changed Prices (Symmetric Diff): {changed_prices}")

# Simulate multiple updates (e.g., 5 days)
price_history = [initial_prices]
goods = ["grain", "steel", "wine"]
current_prices = initial_prices.copy()

for day in range(1, 6):
    # Randomly adjust prices
    new_prices = set()
    for price in current_prices:
        shift = random.uniform(-2.5, 2.5)  # ±2.5 gold shift
        new_prices.add(round(price + shift, 1))
    price_history.append(new_prices)
    current_prices = new_prices

# Build DataFrame for export
df = pd.DataFrame({
    f"Day {i}": list(prices) + [None] * (max(len(p) for p in price_history) - len(prices))
    for i, prices in enumerate(price_history)
})
df.to_excel("docs/market_sets.xlsx", index=False)

print(f"\n5-Day Price History saved to SevenVoices/docs/market_sets.xlsx, Your Grace!")