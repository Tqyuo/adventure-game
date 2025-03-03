user_name = input("What is your name? ")
playing_status = input("Would you like to play this decision based story game? (Y/N)").lower()
if playing_status == "y":
    decision = input(f"""Welcome {user_name},
                    you find yourself walking on a road under heavy rain.
                    You reach a split in the road where you must decide to go either left or right.
                    Which do you choose? (L/R) --->""").lower()
    if decision == "l":
        print("""   You have chosen to proceed left.
                    You begin walking on the left path.
                    This time you stumble across a sketchy wooden bridge above a wide river.
                    Do you cross the bridge or attempt to swim across? (cross/swim) """)
    elif decision == "r":
        decision = input("""You have chosen to proceed right.
                    Walking right you began to walk down a dark road,
                    eventually you come across another intersection where
                    the road splits left or straight. Down the left path,
                    in the distance you can make out what appears to be a village.
                    Straight is just thick vegetation. You do have a machete on you,
                    but keep in mind it is still raining. (l/s)""").lower()
else:
    print("Goodbye")
