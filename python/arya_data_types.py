# arya_data_types.py - Data Types Lesson: Type Conversion & String Manipulation
# For Arya Stark, tutored by Tyrion, Hand of King Bran, April 9, 2025

# Theory: Data Types
print("Arya's Lesson: Data Types - The Weapons of Code!")
print("1. Strings: Text, like names - 'Arya Stark'")
print("2. Integers: Whole numbers, like kills - 5")
print("3. Floats: Decimals, like distances - 3.14")
print("4. Booleans: True or False, like 'Is foe dead?' - True")

# Problem 1: Type Conversion
print("\nProblem 1: Type Conversion - Change the Form!")
# String to Integer
kills_str = "7"  # Arya’s kills as text
kills_int = int(kills_str)  # Convert to integer
print(f"Kills as string: {kills_str} (type: {type(kills_str)})")
print(f"Kills as int: {kills_int} (type: {type(kills_int)})")
print(f"Add 1 kill: {kills_int + 1}")  # Math works now!

# Integer to String
enemies = 10
enemies_str = str(enemies)
print(f"Enemies as int: {enemies} (type: {type(enemies)})")
print(f"Enemies as string: '{enemies_str}' + ' foes' = '{enemies_str + ' foes'}'")

# Float to Integer
distance = 5.75  # Miles to target
distance_int = int(distance)  # Drops decimal
print(f"Distance as float: {distance} (type: {type(distance)})")
print(f"Distance as int: {distance_int} (type: {type(distance_int)})")

# Boolean to String
is_armed = True
is_armed_str = str(is_armed)
print(f"Armed? {is_armed} (type: {type(is_armed)})")
print(f"Armed as string: '{is_armed_str}'")

# Problem 2: String Manipulation
print("\nProblem 2: String Manipulation - Wield the Text!")
name = "Arya Stark"
# Slicing - Get parts
first_name = name[0:4]  # Index 0 to 3
last_name = name[5:]    # Index 5 to end
print(f"Full name: {name}")
print(f"First name (slice 0:4): {first_name}")
print(f"Last name (slice 5:): {last_name}")

# Concatenation - Join strings
title = "The Faceless"
full_title = first_name + " " + title
print(f"Concatenate: {full_title}")

# Case Change
shout = name.upper()
whisper = name.lower()
print(f"Shout: {shout}")
print(f"Whisper: {whisper}")

# Problem 3: Mixed Challenge
print("\nProblem 3: Mix It Up!")
foes = "3"  # String
steps = 2.5  # Float
active = False  # Boolean
# Convert and compute
foes_int = int(foes)
total_steps = foes_int + steps
active_str = str(active)
print(f"Foes: {foes} (string) -> {foes_int} (int)")
print(f"Steps: {steps} (float)")
print(f"Total steps: {total_steps} (type: {type(total_steps)})")
print(f"Active? {active} -> '{active_str}' + ' mission' = '{active_str + ' mission'}'")

print("\nArya, master these—your data bends to your blade!")