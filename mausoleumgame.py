from sys import exit

def dead(why):
    print(why, "Good Job!")
    exit(0)

def treasure_room():
    print("You enter a room full of treasure.")
    print("A faceless man presents you with three bags.")
    print("The first bag contains 100 gold coins.")
    print("The second bag contains 500 gold coins.")
    print("The third bag contains 2000 gold coins.")
    print("""
    The faceless man speaks:
    Choose a bag.
    100, 500, or 2000?
    But beware...
    Your actions have consequences.
    """)

    choice = input("> ")
    if "100" in choice:
        print("The man gives you 100 gold coins. Be on your way. You win!")
        exit(0)
    elif "500" in choice:
        print("The man gives you 500 gold coins. Be on your way. You win!")
        exit(0)
    elif "2000" in choice:
        print("You go to pick up the bag of 2000 gold coins.")
        print("The faceless man doesn't appreciate your greed.")
        print("He eats your face off. You lose!")
        exit(0)
    else:
        dead("The faceless man stares at you until you die of boredom.")


def critter_room():
    print("You enter a room filled with christmas decorations.")
    print("You are greeted by a cute squirrel, deer, hedgehog and bear.")
    print("The squirrel approaches you and says: Howdy partner!")
    print("The bear says: We've been waiting for you!")
    print("The deer says: We can't wait to have so much fun with you!")
    print("The squirrel says: But wait, before we continue, who is the one true lord?")
    print("""
         How do you respond?
         Jesus Christ or Hail Satan?
         """)
    critter_moved = False

    while True:
        choice = input("> ")

        if choice == "Jesus Christ":
            dead("The critters eyes light up red and you are set aflame.")
        elif choice == "Hail Satan" and not critter_moved:
            print("We knew you were one of us!")
            print("We'll take you to the treasure room!")
            print("Our friend is there waiting for you!")
            print("You are presented with a golden door.")
            critter_moved = True
        elif choice == "Jesus Christ" and critter_moved:
            dead("The critters do not appreciate betrayal. You are set aflame.")
        elif choice == "Open door" and critter_moved:
            treasure_room()
        else:
            print("I don't know what you mean by that.")

def split_or_steal():
    print("""
    You enter a dark room.
    There is one other person here; a complete random stranger.
    There is a note on the floor that says:
    1 Million Gold coins up for grabs!
    You are both presented with two golden balls.
    One says "Split" one says "Steal".
    If you both split, you'll get 500,000 gold coins each.
    If one splits and one steals, one will get nothing and the other will get all.
    If you both steal, you shall both end up with nothing.
    The choice is yours.

    Do you Split or Steal?
    """)

    choice = input("> ")
    if "split" in choice:
        dead("The stranger chose steal! They take all the coins and leave you for dead.")
    elif "steal" in choice:
        dead("You both picked steal! You're both stuck in this room for all eternity with no coins. Best make friends!")
    else:
        split_or_steal()

def start():
    print("You are in a dark room.")
    print("There are two doors infront of you.")
    print("One to your right and one to your left.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        split_or_steal()
    elif choice == "right":
        critter_room()
    else:
        dead("Your indecisiveness has been the death of you.")

start()
