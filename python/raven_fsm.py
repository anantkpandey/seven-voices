# raven_fsm.py - Raven Messaging with FSM
# For King Bran Stark, SevenVoices, April 9, 2025

from transitions import Machine

class RavenMessenger:
    def __init__(self, message="Winter Is Coming"):
        self.message = message
    
    def on_waiting(self):
        print(f"Raven waits with message: '{self.message}'")
    
    def on_sent(self):
        print("Raven dispatched from the rookery!")
    
    def on_flying(self):
        print(f"Raven flies, bearing '{self.message}'!")
    
    def on_delivered(self):
        print(f"Raven lands—'{self.message}' delivered, Your Grace!")


# Create the raven with a message
raven = RavenMessenger()

# Define FSM states and transitions
states = ['waiting', 'sent', 'flying', 'delivered']
machine = Machine(raven, states=states, initial='waiting')
machine.add_transition('dispatch', 'waiting', 'sent', after='on_sent')
machine.add_transition('launch', 'sent', 'flying', after='on_flying')
machine.add_transition('land', 'flying', 'delivered', after='on_delivered')

# Send the raven on its journey
print("Raven Messaging for the Seven Voices:")
raven.on_waiting()  # Show initial state
raven.dispatch()    # To sent
raven.launch()      # To flying
raven.land()        # To delivered

print("\nAll hail King Bran, Master of Ravens!")