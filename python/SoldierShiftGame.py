class SoldierShiftGame:
    def __init__(self, soldiers):
        """Initialize game with soldiers as players."""
        self.soldiers = soldiers  # Players
        self.shifts = ["Day Shift", "Night Shift"]  # Strategies
        self.current_soldier_index = 0
        self.current_shift_index = 0  # 0 = Day Shift, 1 = Night Shift
        self.assignments = []  # Track (soldier, shift) assignments
        self.payoffs = {soldier: {"Day Shift": 0, "Night Shift": 0} for soldier in soldiers}  # Track fairness

    def assign_shift(self):
        """Assign next soldier to current shift as a cooperative move."""
        soldier = self.soldiers[self.current_soldier_index]
        shift = self.shifts[self.current_shift_index]
        
        # Record assignment
        self.assignments.append((soldier, shift))
        
        # Update payoff (count of shifts per soldier)
        self.payoffs[soldier][shift] += 1
        
        # Rotate to next soldier and shift
        self.current_soldier_index = (self.current_soldier_index + 1) % len(self.soldiers)
        self.current_shift_index = (self.current_shift_index + 1) % len(self.shifts)
        
        return soldier, shift

    def simulate_game(self, num_shifts):
        """Simulate shift assignments as a cooperative game."""
        print("Players (Soldiers):", self.soldiers)
        print("Strategies (Shifts):", self.shifts)
        print(f"Starting with {self.shifts[self.current_shift_index]}\n")
        
        for i in range(num_shifts):
            soldier, shift = self.assign_shift()
            print(f"Round {i+1}: {soldier} assigned to {shift}")
        
        # Summarize assignments
        print("\nSummary of Assignments:")
        for i, (soldier, shift) in enumerate(self.assignments, 1):
            print(f"Round {i}: {soldier} - {shift}")
        
        # Fairness metrics (payoffs)
        print("\nFairness Metrics (Payoffs):")
        for soldier in self.soldiers:
            day_count = self.payoffs[soldier]["Day Shift"]
            night_count = self.payoffs[soldier]["Night Shift"]
            total = day_count + night_count
            balance = abs(day_count - night_count)
            print(f"{soldier}: Day Shifts = {day_count}, Night Shifts = {night_count}, "
                  f"Total = {total}, Balance Diff = {balance}")

    def check_stability(self):
        """Check if the assignment is stable (fair and cooperative)."""
        print("\nStability Check:")
        max_diff = 0
        for soldier in self.soldiers:
            day_count = self.payoffs[soldier]["Day Shift"]
            night_count = self.payoffs[soldier]["Night Shift"]
            diff = abs(day_count - night_count)
            max_diff = max(max_diff, diff)
        if max_diff <= 1:
            print("Stable: All soldiers have nearly equal Day and Night shifts (max difference ≤ 1).")
        else:
            print(f"Unstable: Some soldiers have uneven shifts (max difference = {max_diff}).")
        return max_diff <= 1

def main():
    # Soldier roster
    soldiers = ["Ser Jaime", "Ser Brienne", "Ser Davos", "Ser Jorah", "Ser Tormund"]
    
    # Initialize game
    game = SoldierShiftGame(soldiers)
    
    # Simulate 8 rounds (4 days, alternating Day and Night)
    print("Simulating soldier shift assignments as a cooperative game:")
    game.simulate_game(num_shifts=8)
    
    # Check stability of assignments
    game.check_stability()

if __name__ == "__main__":
    main()