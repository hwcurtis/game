
print("Welcome to the Monty Python Adventure!")
print("You are about to embark on a quest for the Holy Grail. Beware of dangerous encounters!")

player_name = input("What is your name, brave adventurer? ")
print(f"Welcome, Sir {player_name} of Pythonia!")

print("A knight steps in front of you and says, 'None shall pass!'")
choice = input("Do you (1) fight the knight, or (2) try to reason with him? ")

if choice == "1":
    print("The knight draws his sword. It's time for battle!")
    # Optional: Add battle logic (e.g., reducing health points)
elif choice == "2":
    print("The knight scoffs at your attempt to reason and attacks anyway.")
else:
    print("You hesitate... and the knight charges!")
