from collections import deque

class SoldierShiftQueue:
    def __init__(self, soldiers):
        """Initialize queue with soldiers and shift states."""
        self.soldiers = soldiers
        self.queue = deque(soldiers)  # FIFO queue for duty assignments
        self.shifts = ["Day Shift", "Night Shift"]
        self.current_shift_index = 0  # Start with Day Shift (0 = Day, 1 = Night)
        self.assignments = []  # Track history of assignments

    def assign_shift(self):
        """Assign the next soldier to the current shift and rotate queue."""
        if not self.queue:
            return None, None
        
        # Dequeue soldier (assign to shift)
        soldier = self.queue.popleft()
        shift = self.shifts[self.current_shift_index]
        
        # Record assignment
        self.assignments.append((soldier, shift))
        
        # Re-enqueue soldier for future shifts
        self.queue.append(soldier)
        
        # Switch to next shift (Day -> Night or Night -> Day)
        self.current_shift_index = (self.current_shift_index + 1) % len(self.shifts)
        
        return soldier, shift

    def get_queue_state(self):
        """Return current queue contents."""
        return list(self.queue)

    def simulate_shifts(self, num_shifts):
        """Simulate shift assignments for num_shifts."""
        print("Initial Queue:", self.get_queue_state())
        print(f"Starting with {self.shifts[self.current_shift_index]}\n")
        
        for i in range(num_shifts):
            soldier, shift = self.assign_shift()
            if soldier:
                print(f"Shift {i+1}: {soldier} assigned to {shift}")
                print(f"Queue after assignment: {self.get_queue_state()}")
            else:
                print("No soldiers available for assignment.")
                break
        
        print("\nSummary of Assignments:")
        for i, (soldier, shift) in enumerate(self.assignments, 1):
            print(f"Shift {i}: {soldier} - {shift}")

def main():
    # Soldier roster
    soldiers = ["Ser Jaime", "Ser Brienne", "Ser Davos", "Ser Jorah", "Ser Tormund"]
    
    # Initialize queue system
    shift_queue = SoldierShiftQueue(soldiers)
    
    # Simulate 8 shifts (4 days, alternating Day and Night)
    print("Simulating soldier shift assignments:")
    shift_queue.simulate_shifts(num_shifts=8)

    # Queueing Theory Metrics (simplified)
    print("\nQueueing Theory Metrics:")
    print(f"Number of soldiers (queue capacity): {len(soldiers)}")
    print(f"Total shifts assigned: {len(shift_queue.assignments)}")
    print(f"Average service rate: {len(shift_queue.assignments) / 8:.2f} soldiers per shift")
    print(f"Queue discipline: FIFO with circular re-enqueueing")

if __name__ == "__main__":
    main()