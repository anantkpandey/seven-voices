class SoldierDutyFSM:
    def __init__(self, soldiers):
        """Initialize FSM with soldier roster and states."""
        self.soldiers = soldiers
        self.current_soldier_index = 0
        self.states = ["Day Shift", "Night Shift"]
        self.current_state = self.states[0]  # Start with Day Shift
        self.transitions = {
            "Day Shift": "Night Shift",
            "Night Shift": "Day Shift"
        }

    def get_current_soldier(self):
        """Return the soldier currently on duty."""
        return self.soldiers[self.current_soldier_index]

    def transition(self):
        """Move to the next state and rotate soldier."""
        # Change state
        self.current_state = self.transitions[self.current_state]
        # Rotate to next soldier
        self.current_soldier_index = (self.current_soldier_index + 1) % len(self.soldiers)
        return self.current_state, self.get_current_soldier()

    def get_state(self):
        """Return current state and soldier."""
        return self.current_state, self.get_current_soldier()

def main():
    # Soldier roster
    soldiers = ["Ser Jaime", "Ser Brienne", "Ser Davos", "Ser Jorah", "Ser Tormund"]
    fsm = SoldierDutyFSM(soldiers)

    print("Initial Duty Assignment:")
    state, soldier = fsm.get_state()
    print(f"State: {state}, Soldier on Duty: {soldier}\n")

    # Simulate 8 transitions (4 days, covering day and night shifts)
    print("Cycling through 4 days (8 shifts):")
    for i in range(8):
        state, soldier = fsm.transition()
        print(f"Transition {i+1}: State: {state}, Soldier on Duty: {soldier}")

if __name__ == "__main__":
    main()