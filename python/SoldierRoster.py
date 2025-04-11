import time
from collections import deque

# List of soldiers (initial roster)
soldiers = ["Ser Jaime", "Ser Brienne", "Ser Davos", "Ser Jorah", "Ser Tormund"]

def rotate_soldiers(arr, rotations=1):
    """Rotate the soldier list left by specified rotations."""
    if not arr:
        return arr
    # Normalize rotations to avoid redundant cycles
    rotations = rotations % len(arr)
    return arr[rotations:] + arr[:rotations]

def access_soldier(arr, index):
    """Access a soldier by index."""
    return arr[index]

def insert_soldier(arr, soldier, position=None):
    """Insert a soldier into the list at position (default: end)."""
    arr_copy = arr.copy()  # Avoid modifying original
    if position is None:
        arr_copy.append(soldier)  # Insert at end
    else:
        arr_copy.insert(position, soldier)  # Insert at position
    return arr_copy

def delete_soldier(arr, soldier_name):
    """Delete a soldier by name."""
    arr_copy = arr.copy()  # Avoid modifying original
    if soldier_name in arr_copy:
        arr_copy.remove(soldier_name)
    return arr_copy

# Demonstrate and time operations
def main():
    print("Initial Soldier Roster:", soldiers)

    # 1. Access Operation
    start_time = time.time()
    soldier = access_soldier(soldiers, 2)  # Access "Ser Davos"
    end_time = time.time()
    print(f"\nAccessing soldier at index 2: {soldier}")
    print(f"Access time: {(end_time - start_time):.8f} seconds")

    # 2. Insert Operation
    start_time = time.time()
    new_roster = insert_soldier(soldiers, "Ser Bronn", position=1)
    end_time = time.time()
    print(f"\nAfter inserting 'Ser Bronn' at position 1: {new_roster}")
    print(f"Insert time: {(end_time - start_time):.8f} seconds")

    # 3. Delete Operation
    start_time = time.time()
    new_roster = delete_soldier(soldiers, "Ser Jorah")
    end_time = time.time()
    print(f"\nAfter deleting 'Ser Jorah': {new_roster}")
    print(f"Delete time: {(end_time - start_time):.8f} seconds")

    # 4. Rotate Operation
    start_time = time.time()
    rotated = rotate_soldiers(soldiers, 2)  # Rotate left by 2
    end_time = time.time()
    print(f"\nAfter rotating roster left by 2: {rotated}")
    print(f"Rotate time: {(end_time - start_time):.8f} seconds")

if __name__ == "__main__":
    main()

# Big-O Analysis (printed separately for clarity)
print("\n=== Big-O Time Complexity Analysis for Python Lists ===")
print("Access (by index): O(1) - Constant time, direct index lookup.")
print("Insert (at end): O(1) - Amortized constant time for append.")
print("Insert (at position): O(n) - Shift elements after position.")
print("Delete (by value): O(n) - Search for value and shift elements.")
print("Rotate (custom): O(n) - Slicing and concatenating list.")