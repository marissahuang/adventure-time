#======================= Intro =======================

# Hello! My name is Marissa, and this is my adventure game. I worked on this from the 12th - 25th of January.
# This is a scary(?) game that you can potentially die in. I also added elements of randomness.
# p.s. Try using the duster a few times in a certain room...

#======================= Map =======================
'''

I made a map to help me plan the layout of my story and the house it takes place in. I put {?} where items are available for
interaction and pickup upon investigation. I have 10 official rooms.


                         Attic
                        |   {?}|
                        |      |
                         ------
                           || 
     ______    Second    __||__   ________
    |?}    |   Floor    |   x  |=|       x|=====
    |      |============|      | |      {?|    ||
     ------      ||      ------   --------     ||
    Bathroom     ||      Bedroom  Library      ||
               __||__    ______    _________   ---- ----
              |      |  |      |  |      {?}| |         |
              |?}    |==|      |==|         | |         |
              |x     |   ------    ---------  |    x    |
              |      |   Kitchen    Dining||   ---"-"---
              |______|               Hall ||    Basement
                 " "                      ||     (Exit)
              Main Hall  --------    --------
              (Start)   |        |  |{?}     |
                        |    {?} |==|        |  
                        |        |   --------
                         --------     Living
                        Greenhouse     Room


'''

#======================= About the Player =======================

# Data Structure holding the player's name, # of lives, # of coins, inventory, # of times dusted, # of unique items,
# and the # of room visits
player = ["Stranger",{"lives":3},{"coins":5},{"matches":0,"keys":0,"dusters":0,"ropes":0},{"dusted":1},{"items":0},{"hall":0,"kitchen":0,
        "dining room":0,"living room":0,"greenhouse":0,"upper hall":0,"bathroom":0,"bedroom":0,"attic":0,"library":0,"basement":0}]

# asks the player for their name and gives them a chance to correct it if they make a typo 
def yourName():
    name = input("\nNow, what was your name again?\n")
    ans = input("\n%s, was it? \n" %name) 
    while ans.lower() != "yes":
        name = input("What was your name again?\n")
        ans = input("\n%s, was it? Yes or no?\n" %name)    
    if ans.lower() == "yes":
        print("\nRight, of course. How could I forget?")
    return name

# tells the player how many lives they have left
def yourLives():
    print("\nYou have",player[1]["lives"],"lives.")

#======================= Gold =======================

# tells the player how many gold coins they have
def goldCheck():
    print("\nYou have",player[2]["coins"],"gold coins")
    
#======================= Inventory =======================

# tells the player the contents of their inventory and how many of each item they carry along with the total
def invCheck():
    player[5]["items"] = (player[3]["matches"] + player[3]["keys"] + player[3]["dusters"] + player[3]["ropes"])
    itemCheck = print("\n",player[3], "You have",player[5]["items"],"items in total.")

#======================= Rooms =======================

# tells the player the number times they've been in a room
def roomCheck():
    rooms = print("\nTimes you have visited each room:",player[6])

#======================= Actions =======================

# basic options available, asks the player what they want to do, returns the player's choice as action
def infoOption():
    print("\nN = go north, E = go east, S = go south, W = go west, look = look around, I = open inventory, G = check how much "
          "gold you have, H = check how many lives you have, R = check how many times you've been in this room")
    action = input("\nWhat do you want to do? \n")    
    return action

# player information check: items, individual and total number of each, total rooms visited, money, and lives
def statCheck(action):
    if action.lower() == "i":
        invCheck()    
    elif action.lower() == "g":
        goldCheck()
    elif action.lower() == "h":
        yourLives()
    elif action.lower() == "r":
        roomCheck()
    else:
        print("Sorry, that's not one of the available options here. Try again.")

# main hall options for the painting
def hallOption():
    print("\nN = go north, E = go east, S = go south, W = go west, L = light the candles, then take the painting down "
          "\nT = take the painting down, look = look around, I = open inventory, G = check how much gold you have, "
          "\nH = check how many lives you have, R = check how many times you've been in this room")
    action = input("\nWhat do you want to do? \n")    
    return action

# dining hall options once player notices the duster
def diningOption():
    print("\nN = go north, E = go east, S = go south, W = go west, P = pick up the duster, look = look around, I = open inventory, "
          "\nG = check how much gold you have, H = check how many lives you have, R = check how many times you've been in this room")
    action = input("\nWhat do you want to do? \n")    
    return action

# bathroom options once player notices key
def bathOption():
    print("\nN = go north, E = go east, S = go south, W = go west, P = pull the drain plug, look = look around, I = open inventory, "
          "\nG = check how much gold you have, H = check how many lives you have, R = check how many times you've been in this room")
    action = input("\nWhat do you want to do? \n")    
    return action

# bedroom options once player notices attic door
def bedOption():
    print("\nN = go north, E = go east, S = go south, W = go west, C = climb on top of the dresser, look = look around, "
          "\nI = open inventory, G = check how much gold you have, H = check how many lives you have, R = check how many times "
          "you've been in this room")
    action = input("\nWhat do you want to do? \n")    
    return action

# attic options to return to the bedroom
def atticOption():
    if player[3]["dusters"] >= 1:
        print("\nN = go north, E = go east, S = go south, W = go west, C = climb back through the door, D = dust away!, "
              "\nlook = look around, I = open inventory, G = check how much gold you have, H = check how many lives you "
              "have, R = check how many times you've been in this room")
    else:
        print("\nN = go north, E = go east, S = go south, W = go west, C = climb back through the door, look = look around, "
              "\nI = open inventory, G = check how much gold you have, H = check how many lives you have, R = check how many times "
              "you've been in this room")
    action = input("\nWhat do you want to do? \n")    
    return action

# library options once player notices the secret passage
def libraryOption():
    print("\nNE = go northeast and down the secret passage, E = go east, S = go south, W = go west, look = look around, "
          "\nI = open inventory, G = check how much gold you have, H = check how many lives you have, R = check how many times "
          "you've been in this room")
    action = input("\nWhat do you want to do? \n")    
    return action

# basement options
def basementOption():
    if player[3]["ropes"] >= 1:
        print("\nN = go north, back to the library, E = go east, S = go south, W = go west, C = use your rope to climb out the "
              "window, look = look around, I = open inventory, G = check how much gold you have, H = check how many lives you "
              "have, R = check how many times you've been in this room")
    else:
        print("\nN = go north, back to the library, E = go east, S = go south, W = go west, look = look around, "
          "\nI = open inventory, G = check how much gold you have, H = check how many lives you have, R = check how many times "
          "you've been in this room")
    action = input("\nWhat do you want to do? \n")
    return action

#======================= Hall Actions =======================

# player commands and actions taken in the hall, action parameter is the player's input when asked what to do       
def hallStuff(action):
    if action.lower() == "n":
        player[6]["upper hall"] = player[6]["upper hall"] + 1
        print("\nYou come to another hallway. There are two doors: one to the west and one to the east. To the south is the main "
              "hall. The door to the west is splintered and hanging off its hinges. The chandelier swings slowly...")
        action = infoOption()
        secondStuff(action)   
    elif action.lower() == "e":
        player[6]["kitchen"] = player[6]["kitchen"] + 1
        print("\nYou stroll into the kitchen. It, like the rest of the house is extremely dirty. Definitely not up to health code. "
              "The door to the west goes into the main hall, while the door to the east leads to the dining room.")
        action = infoOption()
        kitchenStuff(action)
    elif action.lower() == "s":
        print("\nYou walk up to the door, and having already tested the integrity of it, find that it is still locked. "
              "That's not surprising at all.")
    elif action.lower() == "w":
        print("\nYou walk over to the west wall to stand in front of the portrait. There are unlit candles on the table in front "
              "of the painting.")
        action = hallOption()
        hallStuff(action)
    elif action.lower() == "look":
        print("\nYou look around and see an empty hall. There doesn't appear to be anyone around but you feel a strange presence. "
              "\nYou notice a grand staircase north of your location which leads to the second floor. "
              "\nThere's a painting on the west wall of a woman who gives off an air of mysteriousness and arrogance. "
              "To the east is what appears to be the kitchen, and a door to the south that looks like the main entrance. "
              "")
    elif action.lower() == "l":
        if player[3]["matches"] >= 1:
            print("You light the candles in front of the portrait and take the painting down, revealing a safe with a combination "
                  "lock. You wonder if there's a combination around here somewhere.")
            try:
                safe = int(input("\nWhat is the four digit combination to the safe?\n"))
                if safe == 1235:
                      print("The safe opens! You marvel at the vast amount of gold. In total, you pick up 45 pieces of gold.")
                      player[2]["coins"] = player[2]["coins"] + 45
                      goldCheck()
                else:
                  print("You try the numbers, but the safe fails to open.")
            except ValueError:
                print("That's not a number!")
        else:
            print("You don't have anything to light these candles. Matches would be handy right about now.")
        action = hallOption()
        hallStuff(action)
    elif action.lower() == "t":
        print("You choose to take the painting down, without lighting the candles. This proves to be a horrible mistake. "
              "You hear a shriek: 'You dare to disrespect my image in my own home?'. Everything goes black. ")
        player[1]["lives"] = player[1]["lives"] - 1
        if player[1]["lives"] <= 0:
            print("You have run out of lives. This is game over for you.")
            start()
        else:
            print("You have lost a life. You have",player[1]["lives"],"lives left.")
        action = hallOption()
        hallStuff(action)
    else:
        statCheck(action)
    action = infoOption()
    hallStuff(action)
    
#======================= Kitchen Actions =======================

# player commands and actions taken in the kitchen, action parameter is the player's input when asked what to do       
def kitchenStuff(action):
    if action.lower() == "w":
        player[6]["hall"] = player[6]["hall"] + 1
        print("\nYou are in the main hall of the house. To the north is the grand staircase, leading to the second floor. "
              " To the south is the locked main door, and to the east is the kitchen.")
        action = infoOption()
        hallStuff(action)
    elif action.lower() == "e":
        player[6]["dining room"] = player[6]["dining room"] + 1
        print("\nYou arrive in the dining room. To the west is the kitchen, and to the south is the living room.") 
        action = infoOption()
        diningStuff(action)  
    elif action.lower() == "look":
        print("\nAny food left in the kitchen is either canned or pickled. Thankfully, the kitchen doesn't smell particularly "
              "awful. Maybe the ghosts in this house cleaned out the fridge before deciding to spend the rest of eternity haunting "
              "it. How thoughtful. To the west is the main hall, and to the east is the dining room.")
    else:
        statCheck(action)
    action = infoOption()
    kitchenStuff(action)
    return action

#======================= Dining Room Actions =======================

# player commands and actions taken in the dining room
def diningStuff(action):
    if action.lower() == "w":
        player[6]["kitchen"] = player[6]["kitchen"] + 1
        print("\nYou stroll into the kitchen. It, like the rest of the house is extremely dirty. Definitely not up to health code. "
              "The door to the west goes into the main hall, while the door to the east leads to the dining room. Was the door "
              "to the pantry open when you got here...?")
        action = infoOption()
        kitchenStuff(action)
    elif action.lower() == "s":
        player[6]["living room"] = player[6]["living room"] + 1
        print("\nYou enter the living room. As expected, there are no undead hanging about. There's a large grandfather clock in "
              "the corner of the room. The north doorway leads to the dining room and the west door to the greenhouse.")
        action = infoOption()
        livingStuff(action)
    elif action.lower() == "look":
        print("In the centre of the room is the dining table. It is a classic long wooden table. \nYou wonder if you sat at the "
              "head of the table if a person seated at the opposite end would be able to hear you without shouting."
              "There's a duster resting on one of the placemats. To the west is the kitchen, and to the south is the living room.")
        action = diningOption()
        diningStuff(action)
    elif action.lower() == "p":
        print("\nYou pick up the duster and add it to your backpack. This whole house is in desperate need of dusting.")
        player[3]["dusters"] = player[3]["dusters"] + 1
        invCheck()
    else:
        statCheck(action)
    action = infoOption()
    diningStuff(action)
    return action

#======================= Living Room Actions =======================

def livingStuff(action):
    if action.lower() == "n":
        player[6]["dining room"] = player[6]["dining room"] + 1
        print("\nYou arrive in the dining room. To the west is the kitchen, and to the south is the living room.")
        action = infoOption()
        diningStuff(action)
    elif action.lower() == "w":
        player[6]["greenhouse"] = player[6]["greenhouse"] + 1
        print("\nYou step into the greenhouse. The room is filled with overgrowth, and you can hear the wind whistling outside."
              "\nYou see a sturdy looking rope on one of the workbenches. You decide to take it, since it seems useful.")
        player[3]["ropes"] = player[3]["ropes"] + 1
        invCheck()
        action = infoOption()
        greenStuff(action)
    elif action.lower() == "look":
        print("\nNothing in this room is of interest except the exceptionally carved grandfather clock. It seems to be made of "
              "mahoghany, and its hands are stopped at 12:35. To the north is the dining room, and the greenhouse is to the west.")
    else:
        statCheck(action)
    action = infoOption()
    livingStuff(action)
    return action

#======================= Greenhouse Actions =======================

def greenStuff(action):
    if action.lower() == "e":
        player[6]["living room"] = player[6]["living room"] + 1
        print("\nYou enter the living room. As expected, there are no undead hanging about. There's a large grandfather clock in "
              "the corner of the room. The north doorway leads to the dining room and the west door leads to the greenhouse.")
        action = infoOption()
        livingStuff(action)
    elif action.lower() == "look":
        print("\nThe light casted from the moonlight is tinted green from the glass. While investigating the area, you come "
              "across a rusted old knife. From what you can make out, its blade is dark brown. Whether it is rust or something "
              "more sinister, you can't tell. It looks like it was disposed of rather quickly, maybe by someone fleeing the house. "
              "\nYou decide this item should be left where you found it. To the east is the living room.")
    else:
        statCheck(action)
    action = infoOption()
    greenStuff(action)
    return action
#======================= Second Floor Hallway Actions =======================

# player commands and actions taken in the hall on the second floor    
def secondStuff(action):
    if action.lower() == "w":
        player[6]["bathroom"] = player[6]["bathroom"] + 1
        print("\nYou head into the bathroom. The mirror is dirty and cracked. For a moment you swear you see something move "
              "behind you. Maybe you're just tired.")
        action = infoOption()
        bathStuff(action)
    elif action.lower() == "s":
        player[6]["hall"] = player[6]["hall"] + 1
        print("\nYou are in the main hall of the house. To the north is the grand staircase, leading to the second floor. "
              " To the south is the locked main door, and to the east is the kitchen.")
        action = infoOption()
        hallStuff(action)
    elif action.lower() == "e":
        player[6]["bedroom"] = player[6]["bedroom"] + 1
        print("\nYou stand in a bedroom. The bed is dirty, with its sheets across the floor and the dresser is open with"
              "clothes tossed haphazardly into a suitcase sitting on the ground. The fire in the fireplace has been out for a "
              "very long time. There is a door on the east side of the bedroom and the hallway to the west.")
        action = infoOption()
        bedStuff(action)  
    elif action.lower() == "look":
        print("\nThe hallway you're in is long and narrow. The windows in front of you are covered with thick cobwebs. It looks "
              "like this place hasn't been disturbed in a long time. To the east is the bedroom, and to the west is the bathroom.")
    else:
        statCheck(action)
    action = infoOption()
    secondStuff(action)
    return action

#======================= Bath Actions =======================

# player commands and actions taken in the bathroom
def bathStuff(action):
    if action.lower() == "e":
        player[6]["upper hall"] = player[6]["upper hall"] + 1
        print("\nYou stand in a hallway. There are two doors: one to the west and one to the east. To the south is the main hall. "
              "The door to the west is splintered and hanging off its hinges. The chandelier starts swinging violently...")
        action = infoOption()
        secondStuff(action)
    elif action.lower() == "look":
        print("\nYou inspect the tiles of the bathroom closer. There seems to be remnants of dried blood... "
              "Something horrible happened here. Looking into the claw-footed bathtub, you see dirty water but spot something "
              "shiny on the floor of the tub. To the east is the upper hallway you came from.")
        action = bathOption()
        bathStuff(action)
    elif action.lower() == "p":
        print("\nYou reach in the dirty water and pull the drain plug. Once all the water drains out, you see what was at the "
              "bottom of the tub - a silver key.")
        player[3]["keys"] = player[3]["keys"] + 1
        invCheck()
    else:
        statCheck(action)
    action = infoOption()
    bathStuff(action)
    return action

#======================= Bedroom Actions =======================

# player commands and actions taken in the bedroom
def bedStuff(action):
    if action.lower() == "w":
        player[6]["upper hall"] = player[6]["upper hall"] + 1
        print("\nYou stand in a hallway. There are two doors: one to the west and one to the east. To the south is the main hall. "
              "The door to the west is splintered and hanging off its hinges. The chandelier is completely still.")
        action = infoOption()
        secondStuff(action)
    elif action.lower() == "e":
        if player[3]["keys"] >= 1:
            player[6]["library"] = player[6]["library"] + 1
            print("The door opened! You step east, into a vast library. This room is mysteriously lit by candles. You can't help "
                  "but wonder who lit them. \nFire also doesn't seem like a smart choice for lighting a room full of paper but "
                  "you don't spend too long thinking about the potential fire hazard.")
            action = infoOption()
            libraryStuff(action)
        else:
            print("The door doesn't budge. You look through the keyhole but see only orbs of light surrounded by what looks to be "
                  "wooden shelves. There should be a key to this door somewhere around here...")
            action = infoOption()
            bedStuff(action)
    elif action.lower() == "look":
        print("\nUpon closer inspection, there is a charred and burnt journal sitting on the logs of the fireplace. Flipping "
              "through the journal yields no information - the pages are burnt beyond use. Scanning the room again, you see a "
              "door on the ceiling over the dresser, presumably leading to an attic. To your east is the door to the library "
              "and to the west, the door to the upper hallway.")
        action = bedOption()
        bedStuff(action)
    elif action.lower() == "c":
        if player[2]["coins"] >= 2:
            player[6]["attic"] = player[6]["attic"] + 1
            print("\nYou clumsily climb on top of the dresser, but as you fumble to get your footing, you drop 2 coins. Mourning "
                  "the loss of your precious money, you decide to pick up the pieces of your life and move on. You push open the "
                  "door above you and climb into the attic.")
            player[2]["coins"] = player[2]["coins"] - 2
            goldCheck()
        else:
            player[6]["attic"] = player[6]["attic"] + 1
            print("\nYou clumsily attempt to climb on top of the dresser, and with the energy only a tired, confused person can "
                  "muster, you eventually heave yourself on top of the structure. You push open the door above you with the "
                  "remaining energy left in your body, wondering if this dusty room was worth the struggle.")
        action = atticOption()
        atticStuff(action)
    else:
        statCheck(action)
    action = infoOption()
    bedStuff(action)
    return action

#======================= Attic Actions =======================

def atticStuff(action):
    if action.lower() == "c":
        player[6]["bedroom"] = player[6]["bedroom"] + 1
        print("\nYou are back in the bedroom. The bed is dirty, with its sheets across the floor and the dresser is open with"
              "clothes tossed haphazardly into a suitcase sitting on the ground. The fire in the fireplace has been out for a "
              "very long time. There is a door on the east side of the bedroom, and the hallway to the west.")
        action = infoOption()
        bedStuff(action)
    elif action.lower() == "look":
        print("\nThis is an exceptionally dusty room. It's hard to see in here, but it looks like the attic is filled with "
              "useless junk. Below you is the bedroom you came from.")   
    elif action.lower() == "d":
        if player[4]["dusted"] == 4:
            print("\nWow, after all that dusting you actually found something! You pick up a box of matches.")
            player[3]["matches"] = player[3]["matches"] + 1
            invCheck()
        else:
            print("\nYou dust furiously! You have dusted",player[4]["dusted"],"times")
            player[4]["dusted"] = player[4]["dusted"] + 1
    else:
        statCheck(action)
    action = atticOption()
    atticStuff(action)

#======================= Library Actions =======================

def libraryStuff(action):
    if action.lower() == "w":
        player[6]["bedroom"] = player[6]["bedroom"] + 1
        print("\nYou are back in the bedroom. The bed is dirty, with its sheets across the floor and the dresser is open with"
              "clothes tossed haphazardly into a suitcase sitting on the ground. The fire in the fireplace has been out for a "
              "very long time. There is a door on the east side of the bedroom, and the hallway to the south.")
        action = infoOption()
        bedStuff(action)
    elif action.lower() == "look":
        print("\nYou stand in a magnificent library. The smell of old books is overwhelming. While the idea of spending the night "
              "in this room reading is tempting, the need to get out overpowers that. While inspecting the northeast wall, "
              "you notice a door expertly hidden by the bookcases. It seems to be a stone passageway, leading downwards. "
              "To the west is the bedroom.")
        action = libraryOption()
        libraryStuff(action)
    elif action.lower() == "ne":
        player[6]["basement"] = player[6]["basement"] + 1
        if player[6]["attic"] >= 2:
            print("\nYour constant climbing up and down the dresser to the attic really took a toll on you. While you go down "
                  "the stairs, your legs give out and you tumble down the stone steps.")
            player[1]["lives"] = player[1]["lives"] - 1
            if player[1]["lives"] <= 0:
                print("You have run out of lives. This is game over for you.")
                start()
            else:
                print("You have lost a life. You have",player[1]["lives"],"lives left.")
        else:
            print("\nYou open the hidden door and venture into the passage. The dim light of the library behind you is seemingly "
                  "useless as the darkness in front of you seems to swallow any light. As you stumble down the steps, it dawns "
                  "on you that you have gone down two floors already, and as the area you step into opens up, you arrive in the "
                  "basement.")
        action = basementOption()
        basementStuff(action)
    else:
        statCheck(action)
    action = libraryOption()
    libraryStuff(action)

#======================= Basement Actions =======================

def basementStuff(action):
   if action.lower() == "n":
       print("\nYou stand in a vast library. Five of the candles flicker and go out. To the northeast is the passage to the "
             "basement, and to the west is the bedroom.")
       action = libraryOption()
       libraryStuff(action)
   elif action.lower() == "s":
        print("\nYou walk up to the window and stand under it. It is roughly 12 ft up on the wall.")
        action = input("\nAttempt to climb up the brick with your bare hands? Y/N?\n")
        if action.lower() == "y":
             print("\nYou greatly overestimate your rock climbing abilities, and fall off the wall. You hit the floorboards "
                   "with so much force that you break through the rotten wood and fall down to the cavern beneath the house. "
                   "You lose all your lives. Game over.")
             start()
        else:
             print("\nYou stand in the middle of the basement and do nothing.")
   elif action.lower() == "c":
         print("\nMaking a sort of grappling hook with the metal laying about, you use your rope and climb up and out the window. "
               "\nCongratulations!! You've escaped the house!"
               "\nYour stats:\n")
         yourLives()          
         invCheck()
         goldCheck()
         roomCheck()
         action = input("\nRestart? Y/N?\n")
         if action.lower() == "y":
                start()
   elif action.lower() == "look":
        print("\nIt's too dark in here to see anything. You can faintly make out a window on the south side of the basement. "
              "To the north are the stairs up to the library.")
   else:
        statCheck(action)
   action = basementOption()
   basementStuff(action)
   
#======================= You Wake Up... =======================
    
def start():
    print("\nWelcome to Marissa's text adventure game! In this game you can collect items, use them to unlock secrets, "
          "and find a way out. Many of the events are random, or based on an unknown condition. "
          "Be careful though, you can die in this game. You start out with 3 lives."
          "\nMake sure to look for all the items you can in order to progress and make it out of the house safely!"
          "\nGood luck.")
    
    print("\n################################## Amnesia ##################################\n"
          "\nYou wake up on the floor of a dimly lit dusty mansion, with no recollection of how you got there or why you are there. "
          "\nThe moonlight streams in from the cracks in the painted over windows, indicating that it is some time at night. "
          "You investigate further and find out that the main entrance is locked from the outside, so you decide to search the house "
          "for a way out. \n"
          "\nReaching in your pocket, you find 5 gold coins. Your messenger bag is empty however.")
    
    player[0] = yourName() # replaces 'Stranger' with the player's name    
    action = infoOption()
    hallStuff(action)
start()    
