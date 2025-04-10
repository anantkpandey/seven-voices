# bran_succession.py - Tyrion builds succession for King Bran
print("King Bran’s Succession - A Democratic Decree")

# Candidate data (example - replace with real lords!)
candidate = "Sansa"       # Name
votes = 60               # Percentage of smallfolk votes (0-100)
age = 25                 # Years lived
council_approved = True  # Hand and council’s approval

# Decision logic with if-else and logical operators
if votes >= 50 and age >= 18 and council_approved:
    print(f"{candidate} is chosen as successor!")
    print(f"Votes: {votes}%, Age: {age}, Council Approved: Yes")
elif votes >= 50 and age >= 18 and not council_approved:
    print(f"{candidate} has votes ({votes}%) and age ({age}), but the council says nay.")
    print("Succession delayed—call a new vote, Your Grace!")
elif votes < 50 and age >= 18:
    print(f"{candidate} lacks votes ({votes}%)—the smallfolk spurn her, though age ({age}) suffices.")
elif votes >= 50 and age < 18:
    print(f"{candidate} has votes ({votes}%), but too young at {age}—wait a few winters!")
else:
    print(f"{candidate} fails all counts—votes {votes}%, age {age}, council shuns.")
    print("No successor yet—chaos looms, Bran!")

# A jest from your Hand
if candidate != "Tyrion" or votes < 100:
    print("Why not me, Tyrion? I’d rule with wine and wisdom!")