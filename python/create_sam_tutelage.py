# create_sam_tutelage.py - Generate sam_tutelage.xlsx
# For King Bran Stark, counseled by Tyrion, Hand of the King, April 10, 2025

import pandas as pd

data = [
    ["Physics", "Understand forces—catapult design, castle defenses—enhancing military precision.", "Siege warfare inefficiencies; weak fortifications against dragons or trebuchets.", 10, "Stronger walls, fewer siege losses"],
    ["Chemistry", "Craft wildfire, fertilizers—control resources, boost agriculture, wield power.", "Famine from poor harvests; lack of alchemical defenses against foes like Cersei’s wildfire plots.", 15, "More crops, wildfire to deter invaders"],
    ["Mathematics", "Calculate taxes, troop logistics—ensure fair rule, efficient supply lines.", "Misallocated resources; inaccurate levies causing unrest among smallfolk.", 5, "Fair taxes, well-fed armies"],
    ["Discrete Mathematics", "Model alliances, voting systems—optimize diplomacy, council decisions.", "Feudal disputes; unclear succession lines fueling wars (e.g., War of the Five Kings).", 20, "Peaceful alliances, clear succession"],
    ["Engineering Mathematics", "Design bridges, aqueducts—improve infrastructure, unify the realm.", "Broken trade routes; flooded Riverlands disrupting food supply.", 25, "Better roads, steady food from aqueducts"],
    ["Digital Design", "Build signaling systems (e.g., raven relays)—speed communication across kingdoms.", "Slow message delivery; miscommunication sparking rebellions (e.g., Robb’s campaigns).", 30, "Faster news, fewer rebellions"],
    ["Computer Organisation and Architecture", "Structure data flow—organize royal records, troop movements digitally.", "Lost scrolls; chaotic command during battles like Blackwater.", 35, "Orderly records, swift battle commands"],
    ["Programming and Data Structures", "Code tools like `raven_tally.py`—track resources, messages, automate rule.", "Inefficient raven messaging; untracked supplies during winter sieges.", 3, "Tracked ravens, stocked granaries"],
    ["Algorithms", "Optimize travel routes, battle plans—swift decisions, minimal losses.", "Long marches exhausting armies (e.g., Stannis at Winterfell); poor tactical choices.", 40, "Shorter marches, victorious battles"],
    ["Theory of Computation", "Predict system limits—ensure scalable governance as kingdoms grow.", "Overstretched rule post-war; failing to manage expanded territories after Daenerys’s conquests.", 50, "Stable rule over vast lands"],
    ["Compiler Design", "Translate decrees to code—standardize commands for maesters, lords.", "Misinterpreted royal orders; inconsistent law enforcement across regions.", 55, "Clear laws, uniform justice"],
    ["Operating Systems", "Manage kingdom processes—allocate resources, prioritize tasks like a king’s OS.", "Overlapping duties among lords; resource hoarding by Houses like Lannister.", 60, "Fair resource split, efficient tasks"],
    ["Database Management Systems", "Store folk's data—track taxes, fealties, harvests in a royal database.", "Lost lineage records (e.g., Jon Snow’s claim); untracked grain stores leading to starvation.", 45, "Known lineage, full granaries"],
    ["Computer Networks", "Link castles digitally—fast, secure communication beyond ravens.", "Isolated holdfasts; delayed warnings of White Walker incursions.", 65, "Connected keeps, timely defense alerts"],
    ["Data Science and Big Data", "Analyze harvest trends, battle stats—predict famines, plan wars with data.", "Unforeseen shortages; repeated tactical failures against unpredictable foes like Euron Greyjoy.", 70, "Predicted harvests, winning strategies"],
    ["Robotics", "Automate labor—forge golems for fields, walls—ease burdens, bolster defenses.", "Smallfolk exhaustion; crumbling defenses against invaders (e.g., Wildlings breaching the Wall).", 80, "Rested workers, unbreached walls"],
    ["Mechanical Engineering", "Build siege engines, water mills—strengthen war and peace efforts.", "Weak trebuchets failing at sieges; insufficient grain milling during winters.", 75, "Stronger sieges, milled grain aplenty"],
    ["Aerospace Engineering", "Design dragon harnesses, air scouts—master skies, rival Daenerys’s legacy.", "Dragon unpredictability (e.g., Drogon’s rampages); no aerial defense against aerial threats like Viserion.", 90, "Controlled dragons, skyward vigilance"]
]

df = pd.DataFrame(data, columns=["Subject Name", "How it Helps in Ruling My Kingdoms", "Problems of Westeros It Can Solve", "Day to Apply", "Folk’s Gain"])
df.to_excel("docs/sam_tutelage.xlsx", index=False)
print("Royal spreadsheet forged at SevenVoices/docs/sam_tutelage.xlsx, Your Grace!")