# raven_tally.py - Raven Messaging with Tally and Edges
# For King Bran Stark, SevenVoices, April 9, 2025

from transitions import Machine

class RavenMessenger:
    def __init__(self, message="Winter Is Coming"):
        self.message = message
    
    def on_waiting(self):
        print(f"Raven waits with: '{self.message}'")
    
    def on_sent(self):
        print("Raven dispatched!")
    
    def on_flying(self):
        print(f"Raven flies with: '{self.message}'")
    
    def on_delivered(self):
        print(f"Raven delivers: '{self.message}'")

class RavenTally:
    def __init__(self):
        self.messages = ["Winter Is Coming", "The Wall stands!", "Hold the North!"]
        self.total_sent = 0
        self.destinations = []  # List of all destinations
        self.kingdoms = ['North', 'Vale', 'Riverlands', 'Westerlands', 'Reach', 'Stormlands', 'Dorne']
    
    def send_raven(self, kingdom, message_index):
        """Send a raven with FSM and tally its destination."""
        message = self.messages[message_index % len(self.messages)]
        raven = RavenMessenger(message)
        
        # FSM for this raven
        states = ['waiting', 'sent', 'flying', 'delivered']
        machine = Machine(raven, states=states, initial='waiting')
        machine.add_transition('dispatch', 'waiting', 'sent', after='on_sent')
        machine.add_transition('launch', 'sent', 'flying', after='on_flying')
        machine.add_transition('land', 'flying', 'delivered', after='on_delivered')
        
        # Fly the raven
        raven.dispatch()
        raven.launch()
        raven.land()
        
        self.total_sent += 1
        self.destinations.append(kingdom)
    
    def list_edges(self):
        """List edges as sequential pairs from destinations."""
        edges = []
        for i in range(len(self.destinations) - 1):
            edges.append((self.destinations[i], self.destinations[i + 1]))
        return edges
    
    def report_tally(self):
        """Report tally and edges."""
        unique_destinations = set(self.destinations)
        edges = self.list_edges()
        print(f"\nTotal Ravens Sent: {self.total_sent}")
        print(f"All Destinations: {self.destinations}")
        print(f"Unique Kingdoms Reached: {len(unique_destinations)} - {unique_destinations}")
        print(f"Edges (Sequential): {edges}")

# Simulate raven messaging
raven_tracker = RavenTally()

print("Raven Messaging for the Seven Voices:")
raven_tracker.send_raven('North', 0)       # Winter Is Coming
raven_tracker.send_raven('Vale', 1)        # The Wall stands!
raven_tracker.send_raven('Riverlands', 2)  # Hold the North!
raven_tracker.send_raven('North', 1)       # The Wall stands!
raven_tracker.send_raven('Dorne', 0)       # Winter Is Coming

# Report with edges
raven_tracker.report_tally()

print("\nAll hail King Bran, Lord of Ravens and Edges!")