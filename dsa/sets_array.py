# raven_tally.py - Raven Messaging with Tally (List and Set)
# For King Bran Stark, SevenVoices, April 9, 2025

class RavenTally:
    def __init__(self):
        self.messages = ["Winter Is Coming", "The Wall stands!", "Hold the North!"]
        self.total_sent = 0
        self.destinations = []  # List to store all destinations
        self.kingdoms = ['North', 'Vale', 'Riverlands', 'Westerlands', 'Reach', 'Stormlands', 'Dorne']

    def send_raven(self, kingdom, message_index):
        """Send a raven and log its destination."""
        message = self.messages[message_index % len(self.messages)]  # Cycle through messages
        print(f"Raven sent to {kingdom} with: '{message}'")
        self.total_sent += 1
        self.destinations.append(kingdom)  # Add to list

    def report_tally(self):
        """Report total sent, all destinations, and unique kingdoms."""
        unique_destinations = set(self.destinations)  # Convert to set for unique counts
        print(f"\nTotal Ravens Sent: {self.total_sent}")
        print(f"All Destinations (in order): {self.destinations}")
        print(f"Unique Kingdoms Reached: {len(unique_destinations)} - {unique_destinations}")

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