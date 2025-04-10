# market_recursion.py - Simulate market price updates with Recursion Theory
# For King Bran Stark, counseled by Tyrion, Hand of the King, April 10, 2025

import pandas as pd
import random

# Recursive price update function
def update_price(day, max_days, base_price, history=None):
    if history is None:
        history = []
    
    # Base case: Day 0 or max reached
    if day >= max_days:
        return history
    
    # Day 0: Initial price
    if day == 0:
        history.append((day, base_price))
        return update_price(day + 1, max_days, base_price, history)
    
    # Recursive step: Adjust prior price
    prev_price = history[-1][1]
    change = random.uniform(-0.05, 0.05)  # ±5% shift
    new_price = round(prev_price * (1 + change), 2)
    history.append((day, new_price))
    return update_price(day + 1, max_days, base_price, history)

# Simulate market updates
base_price = 20.0  # Initial price (e.g., grain at 20 gold)
max_days = 5       # Simulate 5 days

price_history = update_price(0, max_days, base_price)

# Report
print("Market Price Updates with Recursion:")
for day, price in price_history:
    print(f"Day {day}: {price} gold")

# Export to Excel
df = pd.DataFrame(price_history, columns=["Day", "Price"])
df.to_excel("docs/market_recursion.xlsx", index=False)
print(f"\nPrice history saved to SevenVoices/docs/market_recursion.xlsx, Your Grace!")

# Recursive trend analysis (example: cumulative change)
def cumulative_change(history, day):
    if day <= 0:
        return 0  # Base case: no change at Day 0
    prev_day, prev_price = history[day - 1]
    curr_day, curr_price = history[day]
    return (curr_price - prev_price) + cumulative_change(history, day - 1)

total_change = cumulative_change(price_history, len(price_history) - 1)
print(f"Total Price Change by Day {max_days - 1}: {total_change:.2f} gold")