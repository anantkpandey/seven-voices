def debug_print(message):
    """Helper function to print debug messages."""
    print(f"[DEBUG] {message}")

class SoldierShiftSet:
    def __init__(self, soldiers):
        """Initialize sets for soldiers and shifts."""
        debug_print("Initializing SoldierShiftSet")
        if not soldiers:
            raise ValueError("Soldier list cannot be empty")
        self.soldiers = set(soldiers)  # Set S: soldiers
        self.shifts = {"Day Shift", "Night Shift"}  # Set T: shifts
        self.soldier_list = list(soldiers)  # Ordered list for rotation
        self.current_soldier_index = 0
        self.current_shift = "Day Shift"
        self.assignments = set()  # Track assignments as (soldier, shift) pairs
        self.all_pairs = {(s, t) for s in self.soldiers for t in self.shifts}  # S × T
        debug_print(f"Soldiers: {self.soldiers}, Shifts: {self.shifts}")

    def next_assignment(self):
        """Assign next soldier to current shift using set operations."""
        debug_print(f"Assigning shift, current index: {self.current_soldier_index}")
        soldier = self.soldier_list[self.current_soldier_index]
        shift = self.current_shift
        
        # Create assignment as a singleton set
        assignment = {(soldier, shift)}
        debug_print(f"Assigning {soldier} to {shift}")
        
        # Add to assignments (union)
        self.assignments = self.assignments | assignment
        
        # Update state
        self.current_soldier_index = (self.current_soldier_index + 1) % len(self.soldier_list)
        self.current_shift = "Night Shift" if shift == "Day Shift" else "Day Shift"
        
        return soldier, shift

    def simulate_shifts(self, num_shifts):
        """Simulate shift assignments for num_shifts."""
        debug_print("Starting simulation")
        print("Soldiers (Set S):", self.soldiers)
        print("Shifts (Set T):", self.shifts)
        print("Possible Assignments (S × T):", self.all_pairs)
        print(f"\nStarting with {self.current_shift}\n")
        
        for i in range(num_shifts):
            soldier, shift = self.next_assignment()
            print(f"Shift {i+1}: {soldier} assigned to {shift}")
            
            # Show remaining unassigned pairs (difference)
            remaining = self.all_pairs - self.assignments
            print(f"Remaining possible assignments: {len(remaining)} pairs")
        
        print("\nSummary of Assignments:")
        for i, (soldier, shift) in enumerate(sorted(self.assignments, key=lambda x: x[0]), 1):
            print(f"Shift {i}: {soldier} - {shift}")
        
        # Reset assignments after full cycle
        if len(self.assignments) >= len(self.all_pairs):
            debug_print("Full cycle completed, resetting assignments")
            print("\nFull cycle completed. Resetting assignments.")
            self.assignments = set()

def main():
    debug_print("Entering main function")
    try:
        # Soldier roster
        soldiers = ["Ser Jaime", "Ser Brienne", "Ser Davos", "Ser Jorah", "Ser Tormund"]
        debug_print(f"Soldier roster: {soldiers}")
        
        # Initialize set-based system
        shift_set = SoldierShiftSet(soldiers)
        
        # Simulate 8 shifts (4 days, alternating Day and Night)
        print("\nSimulating soldier shift assignments:")
        shift_set.simulate_shifts(num_shifts=8)
    except Exception as e:
        debug_print(f"Error occurred: {str(e)}")
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    debug_print("Script starting")
    main()