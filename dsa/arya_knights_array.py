# arya_knights_array.py - Static Arrays Lesson
# For Arya Stark, tutored by Tyrion, Hand of King Bran, April 9, 2025

# Arrays: Meaning - A fixed-size list, like a roster of knights
print("Lesson for Arya: Arrays hold knights in a fixed order!")
knights = ["Ser Jaime", "Ser Brienne", "Ser Davos", "Ser Jorah"]  # Static array (conceptually)
print("Knights roster:", knights)
print("Size (fixed):", len(knights), "knights")

# Indexing: Positions start at 0, like Arya’s strike order
print("\nIndexing - Each knight has a number:")
print("Knight at index 0:", knights[0])  # First knight
print("Knight at index 1:", knights[1])  # Second
print("Knight at index 3:", knights[3])  # Last
print("Arya’s target (index 2):", knights[2])  # Davos, third

# Memory Layout: Knights sit side-by-side in order
print("\nMemory Layout - Imagine knights in a line:")
for i in range(len(knights)):
    print(f"Slot {i}: {knights[i]}")  # Show each slot

# Accessing and using the array
print("\nArya checks the roster:")
target_index = 1  # Ser Brienne
print(f"Arya calls knight at index {target_index}: {knights[target_index]}")
print("Total knights ready for King Bran:", len(knights))

print("\nArya, arrays are your weapons—fixed, ordered, ready!")