class SoldierShiftRecursion:
    def __init__(self, soldiers):
        """Initialize recursion with soldiers and shifts."""
        self.soldiers = soldiers
        self.shifts = ["Day Shift", "Night Shift"]
        self.assignments = []  # Track (soldier, shift) assignments

    def assign_shifts_recursive(self, remaining_shifts, soldier_index=0, shift_index=0):
        """Recursively assign soldiers to shifts."""
        # Base case: no more shifts to assign
        if remaining_shifts <= 0:
            return
        
        # Assign current soldier to current shift
        soldier = self.soldiers[soldier_index]
        shift = self.shifts[shift_index]
        self.assignments.append((soldier, shift))
        
        # Print assignment (in recursive call for ordered output)
        print(f"Shift {len(self.assignments)}: {soldier} assigned to {shift}")
        
        # Prepare for next recursive call
        next_soldier_index = (soldier_index + 1) % len(self.soldiers)
        next_shift_index = (shift_index + 1) % len(self.shifts)
        
        # Recursive call with one fewer shift
        self.assign_shifts_recursive(
            remaining_shifts - 1,
            next_soldier_index,
            next_shift_index
        )

    def simulate_shifts(self, num_shifts):
        """Start recursive shift assignments."""
        print("Soldiers:", self.soldiers)
        print("Shifts:", self.shifts)
        print(f"Starting recursive assignment for {num_shifts} shifts\n")
        
        # Clear any prior assignments
        self.assignments = []
        
        # Begin recursion
        self.assign_shifts_recursive(num_shifts)
        
        # Summarize assignments
        print("\nSummary of Assignments:")
        for i, (soldier, shift) in enumerate(self.assignments, 1):
            print(f"Shift {i}: {soldier} - {shift}")

def main():
    # Soldier roster
    soldiers = ["Ser Jaime", "Ser Brienne", "Ser Davos", "Ser Jorah", "Ser Tormund"]
    
    # Initialize recursion system
    recursion = SoldierShiftRecursion(soldiers)
    
    # Simulate 8 shifts (4 days, alternating Day and Night)
    print("Simulating soldier shift assignments recursively:")
    recursion.simulate_shifts(num_shifts=8)

if __name__ == "__main__":
    main()