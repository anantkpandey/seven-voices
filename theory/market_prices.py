# market_prices.py - Simple Acceptor for Market Price Updates
# For King Bran Stark, crafted by Tyrion, Hand of the King, April 10, 2025

import random
import time

# Simple Acceptor class - a basic state machine
class MarketAcceptor:
    def __init__(self):
        self.state = "waiting"  # States: waiting, updating, reporting
        self.prices = {
            "grain": 10.0,  # Floats for prices
            "steel": 25.0,
            "wine": 15.0
        }
        self.history = []  # Track updates

    def transition(self, new_state):
        print(f"State: {self.state} -> {new_state}")
        self.state = new_state

    def update_prices(self):
        self.transition("updating")
        for good in self.prices:
            # Simulate price change: ±10% random shift
            change = self.prices[good] * random.uniform(-0.1, 0.1)
            self.prices[good] += change
            self.prices[good] = round(self.prices[good], 2)  # 2 decimals
            self.history.append(f"{good}: {self.prices[good]}")
        self.transition("reporting")

    def report(self):
        if self.state != "reporting":
            print("Not ready to report yet!")
            return
        print("\nMarket Prices Report:")
        for good, price in self.prices.items():
            print(f"{good.capitalize()}: {price} gold")
        self.transition("waiting")

    def run(self):
        print("Market Acceptor begins...")
        while True:
            if self.state == "waiting":
                print("\nWaiting for market shift...")
                time.sleep(2)  # Simulate delay
                self.update_prices()
            elif self.state == "reporting":
                self.report()
            else:
                print("Updating prices...")
                time.sleep(1)  # Brief pause

# Run the market acceptor
if __name__ == "__main__":
    market = MarketAcceptor()
    print("Initial Prices:", market.prices)
    try:
        market.run()  # Runs until Ctrl+C
    except KeyboardInterrupt:
        print("\nMarket closed by royal decree!")
        print("Price History:", market.history)