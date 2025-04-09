# raven_tally.py - Raven Messaging with Manual List and Recursion
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
        self.destinations = []  # All destinations
        self.kingdoms = ['North', 'Vale', 'Riverlands', 'Westerlands', 'Reach', 'Stormlands', 'Dorne']
        self.raven_queue = []  # Manual queue as list
    
    def enqueue_raven(self, kingdom, message_index):
        """Manually add a raven to the queue."""
        self.raven_queue.append((kingdom, message_index))
        print(f"Queued raven for {kingdom} with message index {message_index}")
    
    def send_raven(self, kingdom, message_index):
        """Send a raven with FSM."""
        message = self.messages[message_index % len(self.messages)]
        raven = RavenMessenger(message)
        
        # FSM for this raven
        states = ['waiting', 'sent', 'flying', 'delivered']
        machine = Machine(raven, states=states, initial='waiting')
        machine.add_transition('dispatch', 'waiting', 'sent', after='on_sent')
        machine.add_transition('launch', 'sent', 'flying', after='on_flying')
        machine.add_transition('land', 'flying', 'delivered', after='on_delivered')
        
        raven.dispatch()
        raven.launch()
        raven.land()
        
        self.total_sent += 1
        self.destinations.append(kingdom)
    
    def process_ravens(self, queue):
        """Recursively process the raven queue."""
        if not queue:  # Base case: empty queue
            print("\nAll ravens processed, Your Grace!")
            return
        # Pop first raven (kingdom, message_index)
        kingdom, message_index = queue.pop(0)
        self.send_raven(kingdom, message_index)
        self.process_ravens(queue)  # Recursive call
    
    def list_edges(self):
        """List edges as sequential pairs."""
        edges = [(self.destinations[i], self.destinations[i + 1]) 
                 for i in range(len(self.destinations) - 1)]
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
# Manually queue ravens
raven_tracker.enqueue_raven('North', 0)       # Winter Is Coming
raven_tracker.enqueue_raven('Vale', 1)        # The Wall stands!
raven_tracker.enqueue_raven('Riverlands', 2)  # Hold the North!
raven_tracker.enqueue_raven('North', 1)       # The Wall stands!
raven_tracker.enqueue_raven('Dorne', 0)       # Winter Is Coming

# Process the queue recursively
raven_tracker.process_ravens(raven_tracker.raven_queue)

# Report with edges
raven_tracker.report_tally()

print("\nAll hail King Bran, Lord of Recursive Ravens!")