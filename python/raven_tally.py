# raven_tally.py - Raven Messaging with Tally
# For King Bran Stark, SevenVoices, April 9, 2025

from collections import defaultdict

class RavenTally:
    def __init__(self):
        self.messages = ["Winter Is Coming", "The Wall stands!", "Hold the North!"]
        self.total_sent = 0
        self.kingdom_tally = defaultdict(int)  # Tracks messages per kingdom
        self.kingdoms = ['North', 'Vale', 'Riverlands', 'Westerlands', 'Reach', 'Stormlands', 'Dorne']

    def send_raven(self, kingdom, message_index):
        """Send a raven and tally it."""
        message = self.messages[message_index % len(self.messages)]  # Cycle through messages
        print(f"Raven sent to {kingdom} with: '{message}'")
        self.total_sent += 1
        self.kingdom_tally[kingdom] += 1

    def report_tally(self):
        """Report the total and per-kingdom tally."""
        print(f"\nTotal Ravens Sent: {self.total_sent}")
        print("Messages by Kingdom:")
        for kingdom, count in self.kingdom_tally.items():
            print(f"  {kingdom}: {count} messages")

# Simulate raven messaging
raven_tracker = RavenTally()

print("Raven Messaging for the Seven Voices:")
# Send ravens to various kingdoms
raven_tracker.send_raven('North', 0)       # Winter Is Coming
raven_tracker.send_raven('Vale', 1)        # The Wall stands!
raven_tracker.send_raven('Riverlands', 2)  # Hold the North!
raven_tracker.send_raven('North', 1)       # The Wall stands!
raven_tracker.send_raven('Dorne', 0)       # Winter Is Coming

# Report the tally
raven_tracker.report_tally()

print("\nAll hail King Bran, Keeper of the Raven Tally!")