import random
from transitions import Machine

class RavenTally:
    def __init__(self):
        self.destinations = []
        self.total_sent = 0
        self.delivered = 0
        self.queue = []
        self.kingdoms = ['North', 'Vale', 'Riverlands', 'Dorne']

    def send_raven(self, kingdom):
        raven = RavenMessenger()
        machine = Machine(raven, states=['waiting', 'flying', 'delivered', 'lost'], initial='waiting')
        machine.add_transition('fly', 'waiting', 'flying')
        machine.add_transition('land', 'flying', 'delivered', conditions=lambda: random.random() > 0.2)
        machine.add_transition('crash', 'flying', 'lost', conditions=lambda: random.random() <= 0.2)
        raven.fly()
        if random.random() > 0.2:
            raven.land(); self.delivered += 1
        else:
            raven.crash()
        self.destinations.append(kingdom)
        self.total_sent += 1

    def process_queue(self):
        if self.queue:
            kingdom = self.queue.pop(0)
            self.send_raven(kingdom)
            self.process_queue()