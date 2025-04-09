# arya_array_ops.py - Array Operations Lesson: Traversal, Insertion, Deletion
# For Arya Stark, tutored by Tyrion, Hand of King Bran, April 9, 2025

# Theory: Array Operations
print("Arya’s Final Lesson: Array Operations - Master Your Foes!")
print("1. Traversal: Walk the list, see each foe.")
print("2. Insertion: Add a foe, place them right.")
print("3. Deletion: Strike a foe, remove their name.")

# Start with Arya’s foes - a Python list (dynamic array)
foes = ["Frey", "Bolton", "Cersei"]
print("\nStarting foes:", foes)

# Traversal: Walk the array
print("\nTraversal - List your targets:")
for i in range(len(foes)):
    print(f"Index {i}: {foes[i]}")
# Simpler way - direct walk
print("Or, strike them all:")
for foe in foes:
    print(f"- {foe}")

# Insertion: Add foes
print("\nInsertion - New foes join the list!")
# Append - add to end
foes.append("Joffrey")
print("After append 'Joffrey':", foes)
# Insert - add at specific index
foes.insert(1, "Tywin")  # Index 1, shifts others
print("After insert 'Tywin' at index 1:", foes)

# Deletion: Remove foes
print("\nDeletion - Cross them off!")
# Pop - remove by index, returns it
killed = foes.pop(0)  # Remove index 0 (Frey)
print(f"Killed {killed} with pop(0):", foes)
# Remove - remove by value
foes.remove("Cersei")  # Remove Cersei by name
print("After remove 'Cersei':", foes)

# Final Traversal: Check the list
print("\nFinal Traversal - Who remains?")
for i, foe in enumerate(foes):  # Index and value
    print(f"Slot {i}: {foe}")

print("\nArya, your array bends—traverse, insert, delete like Needle’s strikes!")