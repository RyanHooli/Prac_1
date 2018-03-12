"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

score = float(input("Enter score: "))
if score < 0 or score >100:
    score = float(input("Enter score: "))
elif score >= 50:
        print("Passable mark")
elif score >= 90:
        print("Excellent mark")
else:
    print("Bad mark")