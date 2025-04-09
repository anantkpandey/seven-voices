# arya_dynamic_array.py
knights = ["Ser Jaime", "Ser Brienne"]
print("Start:", knights, "- Size:", len(knights))

knights.append("Ser Davos")  # Grow
print("Added Davos:", knights)

knights.pop(0)  # Shrink
print("Removed Jaime:", knights)

print("Index 0 now:", knights[0])  # Brienne, shifted