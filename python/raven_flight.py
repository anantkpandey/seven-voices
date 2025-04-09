from transitions import Machine

class Raven:
    def on_flying(self): print("Raven takes wing for the Wall!")
    def on_landed(self): print("Message delivered, Your Grace!")

raven = Raven()
states = ['waiting', 'flying', 'landed']
machine = Machine(raven, states=states, initial='waiting')
machine.add_transition('send', 'waiting', 'flying', after='on_flying')
machine.add_transition('arrive', 'flying', 'landed', after='on_landed')

print("Raven’s journey begins:")
raven.send()   # To flying
raven.arrive() # To landed