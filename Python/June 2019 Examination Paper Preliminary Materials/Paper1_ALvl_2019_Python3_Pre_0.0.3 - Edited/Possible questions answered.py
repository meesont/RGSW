#Skeleton Program code for the AQA A Level Paper 1 Summer 2019 examination
#this code should be used in conjunction with the Preliminary Material
#written by the AQA Programmer Team
#developed in the Python 3.5.1 programming environment

import random
import pickle
import os
import struct

INVENTORY = 1001
MINIMUM_ID_FOR_ITEM = 2001
ID_DIFFERENCE_FOR_OBJECT_IN_TWO_LOCATIONS = 10000
INVENTORYLIMIT = 5
PLACESVISITED = []
MAP = {}

class Place():
  def __init__(self):
    self.Description = ""
    self.ID = self.North = self.East = self.South = self.West = self.Up = self.Down = 0

class Character():
  def __init__(self):
    self.Name = self.Description = ""
    self.ID = self.CurrentLocation = 0

class Item():
  def __init__(self):
    self.ID = self.Location = 0
    self.Description = self.Status = self.Name = self.Commands = self.Results = ""


# ADDITION: new functions in order to
def Teleport(You, Location):
    You.CurrentLocation = int(location)
    return You, True

def Save(Characters,Items,Places):
    print('What would you like to save the file as?')
    filename = input('> ')
    with open(filename +'.gme', 'wb') as f:

        pickle.dump(len(Characters), f)
        for i in range(len(Characters)):
            pickle.dump(Characters[i].ID, f)
            pickle.dump(Characters[i].Name, f)
            pickle.dump(Characters[i].Description, f)
            pickle.dump(Characters[i].CurrentLocation, f)

        pickle.dump(len(Places), f)
        for i in range(len(Places)):
            pickle.dump(Places[i].ID,f)
            pickle.dump(Places[i].Description,f)
            pickle.dump(Places[i].North,f)
            pickle.dump(Places[i].East,f)
            pickle.dump(Places[i].South,f)
            pickle.dump(Places[i].West,f)
            pickle.dump(Places[i].Up,f)
            pickle.dump(Places[i].Down,f)

        pickle.dump(len(Items), f)
        for i in range(len(Items)):
            pickle.dump(Items[i].ID,f)
            pickle.dump(Items[i].Description,f)
            pickle.dump(Items[i].Status,f)
            pickle.dump(Items[i].Location,f)
            pickle.dump(Items[i].Name,f)
            pickle.dump(Items[i].Commands,f)
            pickle.dump(Items[i].Results,f)

def AddCharacter():
    TempCharacter = Character()
    TempCharacter.Name = input('Input the name of the chracter: ')
    TempCharacter.Description = input('Input the description of the chracter: ')
    TempCharacter.ID = int(input('Input the ID of the chracter: '))
    TempCharacter.CurrentLocation = int(input('Input the current location of the character: '))
    return TempCharacter

def Drop(Items, Characters, ItemToDrop, CurrentLocation):
    count = 0
    IndexOfItem = GetIndexOfItem(ItemToDrop, -1, Items)

    if IndexOfItem != -1:
        if Items[IndexOfItem].Name == ItemToDrop and Items[IndexOfItem].Location  == INVENTORY:
            print(Items[IndexOfItem].Name + " was dropped")
            Items[IndexOfItem].Location = CurrentLocation
            return Items
        else:
            print('You cannot find ' + ItemToDrop + ' to drop.')
    else:
        Say('This item does not exist, sorry try again!')

def LookForSpaceInInventory(Items):
    spaceInInventory = INVENTORYLIMIT
    for i in Items:
        if i.Location == INVENTORY:
            spaceInInventory -= 1
    return spaceInInventory

def CheckIfAttackPossible(Items, Characters, CharacterToAttack):
    PlayerHasWeapon = False
    PlayersInSameRoom = False
    IndexOfOtherCharacter = -1
    IndexoOfPlayerWeapon = -1
    for i in Items:
        if i.Location == INVENTORY and 'weapon' in i.Status:
            PlayerHasWeapon = True
            IndexOfPlayerWeapon = GetIndexOfItem("", i.ID, Items)
    count = 1
    while count < len(Characters) and not PlayersInSameRoom:
        if Characters[0].CurrentLocation == Characters[count].CurrentLocation and Characters[count].Name = CharacterToAttack:
            PlayersInSameRoom = True
        count += 1
    return (PlayerHasWeapon and PlayersInSameRoom), IndexOfPlayerWeapon, IndexOfOtherCharacter

def UseWeapon(Characters, Items, CharacterToAttack):
    AttackPossible, IndexOfPlayerWeapon, IndexOfOtherCharacter = CheckIfAttackPossible(Items, Characters, CharacterToAttack)
    if not AttackPossible:
        print("You can't hit!")
    else:
        print('You wacked ' + CharacterToAttack)
        Items = TakeItemFromOtherCharacter(Items, Characters[IndexOfOtherCharacter].ID)
    return Items

#BELOW BEGINS SUBROUTINES FOR CREATING THE DYNAMIC MAP
def createRoom(printOrder):
  #how each room is printed.
  placeHolder = "%-2s"
  line1 = ""
  line2 = ""
  line3 = ""
  line4 = ""
  line5 = ""
  for room in printOrder:
    if room == 0:
      line1 = line1+"       "
      line2 = line2+"       "
      line3 = line3+"       "
      line4 = line4+"       "
      line5 = line5+"       "
    else:
      line1 = line1+" _____ "
      line2 = line2+" |   | "
      line3 = line3+" | "+ placeHolder % (str(room)) +"| "
      line4 = line4+" |   | "
      line5 = line5+" ̅̅̅̅̅ "  #this is a bar across - something wrong with wikibooks?

  print(line1)
  print(line2)
  print(line3)
  print(line4)
  print(line5)

def ShowMap():
    smallestx, smallesty, largestx, largesty = 0, 0, 0, 0
    for key in MAP:
        if MAP[key][4] < smallesty:
            smallesty = MAP[key][4]
        if MAP[key][3] < smallestx:
            smallesx = MAP[key][3]
        if MAP[key][4] > largesty:
            largesty = MAP[key][4]
        if MAP[key][3] > largestx:
            largestx = MAP[key][3]
    for i in range(smallesty, largesty+1):
        printOrder = []
        for j in range(smallestx, largestx+1):
            for key in MAP:
                if MAP[key][3] == j and MAP[key][4] == i:
                    foundRoom = key
                    break
            printOrder.append(foundRoom)
        createRoom(printOrder)

        print('\n')

def BuildMap(currentPlace, directionFromParentRoom, ParentRoom):
    yoffset, xoffset = 0, 0
    if ParentRoom != 'null':
        parentRoomx = MAP[ParentRoom][3]
        parentRoomy = MAP[ParentRoom][4]
        if directionFromParentRoom == "west":
          yoffset = parentRoomy
          xoffset = parentRoomx - 1
        if directionFromParentRoom == "east":
          yoffset = parentRoomy
          xoffset = parentRoomx + 1
        if directionFromParentRoom == "north":
          xoffset = parentRoomx
          yoffset = parentRoomy - 1
        if directionFromParentRoom == "south":
          xoffset = parentRoomx
          yoffset = parentRoomy + 1
    MAP[currentPlace] = [currentPlace, directionFromParentRoom, ParentRoom, xoffset, yoffset]

def EatItem(Items, ItemToUse, CurrentLocation, Places):
    IndexOfItem = GetIndexOfItem(ItemToUse, -1, Items)
    if IndexOfItem != -1:
        if Items[IndexOfItem].Location == INVENTORY and 'edible' in Items[IndexOfItem].Status:
            Items = ChangeLocationOfItem(Item, IndexOfItem, 0)
            print('You ate the ' + Items[IndexOfItem].Name)
            return Items
        print("You can't eat that!")
        return Items
#END ADDITION

def GetInstruction():
  print(os.linesep)
  Instruction = input("> ").lower()
  return Instruction

def ExtractCommand(Instruction):
  Command = ""
  if " " not in Instruction:
    return Instruction, Instruction
  while len(Instruction) > 0 and Instruction[0] != " ":
    Command += Instruction[0]
    Instruction = Instruction[1:]
  while len(Instruction) > 0 and Instruction[0] == " ":
    Instruction = Instruction[1:]
  return Command, Instruction

def Go(You, Direction, CurrentPlace):
  ParentRoom = CurrentPlace.ID
  Moved = True
  if Direction == "north":
    if CurrentPlace.North == 0:
      Moved = False
    else:
      You.CurrentLocation = CurrentPlace.North
  elif Direction == "east":
    if CurrentPlace.East == 0:
      Moved = False
    else:
      You.CurrentLocation = CurrentPlace.East
  elif Direction == "south":
    if CurrentPlace.South == 0:
      Moved = False
    else:
      You.CurrentLocation = CurrentPlace.South
  elif Direction == "west":
    if CurrentPlace.West == 0:
      Moved = False
    else:
      You.CurrentLocation = CurrentPlace.West
  elif Direction == "up":
    if CurrentPlace.Up == 0:
      Moved = False
    else:
      You.CurrentLocation = CurrentPlace.Up
  elif Direction == "down":
    if CurrentPlace.Down == 0:
      Moved = False
    else:
      You.CurrentLocation = CurrentPlace.Down
  else:
    Moved = False
  #ADDED IN ORDER TO WORK WTH THE NEW MAP FUNCTION
  if Moved and You.CurrentLocation not in PLACESVISITED:
      PLACESVISITED.append(You.CurrentLocation)
      BuildMap(You.CurrentLocation, Direction, ParentRoom)
  if not Moved:
    print("You are not able to go in that direction.")
  return You, Moved

def DisplayDoorStatus(Status):
  if Status == "open":
    print("The door is open.")
  else:
    print("The door is closed.")

def DisplayContentsOfContainerItem(Items, ContainerID): #Container item may be shelf for example
  print("It contains: ", end = "")
  ContainsItem = False
  for Thing in Items:
    if Thing.Location == ContainerID:
      if ContainsItem:
        print(", ", end = "")
      ContainsItem = True
      print(Thing.Name, end = "")
  if ContainsItem:
    print(".")
  else:
    print("nothing.")

#CAN EDIT EXAMINE METHOD TO FOLLOWING IN ORDER TO ACCEPT ROOMS AND EXAMINE ROOMS
# def Examine(Items, Characters, ItemToExamine, CurrentLocation, Places):
#   Count = 0
#   elif ItemToExamine == "room":
#     print(Places[Characters[0].CurrentLocation - 1].Description)
#     DisplayGettableItemsInLocation(Items, Characters[0].CurrentLocation)
#   else:
#     CONTINUE REST OF CODE
def Examine(Items, Characters, ItemToExamine, CurrentLocation):
  Count = 0
  if ItemToExamine == "inventory": #Allows player to exmaine own inventory and see which items they have in their posession
    DisplayInventory(Items)
  else:
    IndexOfItem = GetIndexOfItem(ItemToExamine, -1, Items)
    if IndexOfItem != -1:
      if Items[IndexOfItem].Location == INVENTORY or Items[IndexOfItem].Location == CurrentLocation:
        print(Items[IndexOfItem].Description)
        if "door" in Items[IndexOfItem].Name:
          DisplayDoorStatus(Items[IndexOfItem].Status)
        if "container" in Items[IndexOfItem].Status:
          DisplayContentsOfContainerItem(Items, Items[IndexOfItem].ID)
        return
    while Count < len(Characters):
      if Characters[Count].Name == ItemToExamine and Characters[Count].CurrentLocation == CurrentLocation:
        print(Characters[Count].Description)
        return
      Count += 1
    print("You cannot find " + ItemToExamine + " to look at.")

def GetPositionOfCommand(CommandList, Command):
  Position = Count = 0
  while Count <= len(CommandList) - len(Command):
    if CommandList[Count:Count + len(Command)] == Command:
      return Position
    elif CommandList[Count] == ",":
      Position += 1
    Count += 1
  return Position

def GetResultForCommand(Results, Position):
  Count = 0
  CurrentPosition = 0
  ResultForCommand = ""
  while CurrentPosition < Position and Count < len(Results):
    if Results[Count] == ";":
      CurrentPosition += 1
    Count += 1
  while Count < len(Results):
    if Results[Count] == ";":
      break
    ResultForCommand += Results[Count]
    Count += 1
  return ResultForCommand

def Say(Speech):
  print()
  print(Speech)
  print()

def ExtractResultForCommand(SubCommand, SubCommandParameter, ResultForCommand):
  Count = 0
  while Count < len(ResultForCommand) and ResultForCommand[Count] != ",":
    SubCommand += ResultForCommand[Count]
    Count += 1
  Count += 1
  while Count < len(ResultForCommand):
    if ResultForCommand[Count] != "," and ResultForCommand[Count] != ";":
      SubCommandParameter += ResultForCommand[Count]
    else:
      break
    Count += 1
  return SubCommand, SubCommandParameter

def ChangeLocationReference(Direction, NewLocationReference, Places, IndexOfCurrentLocation, Opposite):
  ThisPlace = Place()
  ThisPlace = Places[IndexOfCurrentLocation]
  if Direction == "north" and not Opposite or Direction == "south" and Opposite:
    ThisPlace.North = NewLocationReference
  elif Direction == "east" and not Opposite or Direction == "west" and Opposite:
    ThisPlace.East = NewLocationReference
  elif Direction == "south" and not Opposite or Direction == "north" and Opposite:
    ThisPlace.South = NewLocationReference
  elif Direction == "west" and not Opposite or Direction == "east" and Opposite:
    ThisPlace.West = NewLocationReference
  elif Direction == "up" and not Opposite or Direction == "down" and Opposite:
    ThisPlace.Up = NewLocationReference
  elif Direction == "down" and not Opposite or Direction == "up" and Opposite:
    ThisPlace.Down = NewLocationReference
  Places[IndexOfCurrentLocation] = ThisPlace
  return Places

def OpenClose(Open, Items, Places, ItemToOpenClose, CurrentLocation):
  Count = 0
  Direction = ""
  DirectionChange = ""
  ActionWorked = False
  if Open:
    Command = "open"
  else:
    Command = "close"
  while Count < len(Items) and not ActionWorked:
    if Items[Count].Name == ItemToOpenClose:
      if Items[Count].Location == CurrentLocation:
        if len(Items[Count].Commands) >= 4:
          if Command in Items[Count].Commands:
            if Items[Count].Status == Command:
              return -2, Items, Places
            elif Items[Count].Status == "locked":
              return -3, Items, Places
            Position = GetPositionOfCommand(Items[Count].Commands, Command)
            ResultForCommand = GetResultForCommand(Items[Count].Results, Position)
            Direction, DirectionChange = ExtractResultForCommand(Direction, DirectionChange, ResultForCommand)
            Items = ChangeStatusOfItem(Items, Count, Command)
            Count2 = 0
            ActionWorked = True
            while Count2 < len(Places):
              if Places[Count2].ID == int(CurrentLocation):
                Places = ChangeLocationReference(Direction, int(DirectionChange), Places, Count2, False)
              elif Places[Count2].ID == int(DirectionChange):
                Places = ChangeLocationReference(Direction, CurrentLocation, Places, Count2, True)
              Count2 += 1
            if Items[Count].ID > ID_DIFFERENCE_FOR_OBJECT_IN_TWO_LOCATIONS:
              IndexOfOtherSideOfDoor = GetIndexOfItem("", Items[Count].ID - ID_DIFFERENCE_FOR_OBJECT_IN_TWO_LOCATIONS, Items)
            else:
              IndexOfOtherSideOfDoor = GetIndexOfItem("", Items[Count].ID + ID_DIFFERENCE_FOR_OBJECT_IN_TWO_LOCATIONS, Items)
            Items = ChangeStatusOfItem(Items, IndexOfOtherSideOfDoor, Command)
            Count = len(Items) + 1
    Count += 1
  if not ActionWorked:
    return -1, Items, Places
  return int(DirectionChange), Items, Places

def GetIndexOfItem(ItemNameToGet, ItemIDToGet, Items):
  Count = 0
  StopLoop = False
  while not StopLoop and Count < len(Items):
    if (ItemIDToGet == -1 and Items[Count].Name == ItemNameToGet) or Items[Count].ID == ItemIDToGet:
      StopLoop = True
    else:
      Count += 1
  if not StopLoop:
    return -1
  else:
    return Count

def ChangeLocationOfItem(Items, IndexOfItem, NewLocation):
  ThisItem = Item()
  ThisItem = Items[IndexOfItem]
  ThisItem.Location = NewLocation
  Items[IndexOfItem] = ThisItem
  return Items

def ChangeStatusOfItem(Items, IndexOfItem, NewStatus):
  ThisItem = Item()
  ThisItem = Items[IndexOfItem]
  ThisItem.Status = NewStatus
  Items[IndexOfItem] = ThisItem
  return Items

def GetRandomNumber(LowerLimitValue, UpperLimitValue):
  return random.randint(LowerLimitValue, UpperLimitValue)

def RollDie(Lower, Upper):
  LowerLimitValue = 0
  if Lower.isnumeric():
    LowerLimitValue = int(Lower)
  else:
    while LowerLimitValue < 1 or LowerLimitValue > 6:
      LowerLimitValue = int(input("Enter minimum: "))
  UpperLimitValue = 0
  if Upper.isnumeric():
    UpperLimitValue = int(Upper)
  else:
    while UpperLimitValue < LowerLimitValue or UpperLimitValue > 6:
      UpperLimitValue = int(input("Enter maximum: "))
  return GetRandomNumber(LowerLimitValue, UpperLimitValue)

def ChangeStatusOfDoor(Items, CurrentLocation, IndexOfItemToLockUnlock, IndexOfOtherSideItemToLockUnlock):
  if CurrentLocation == Items[IndexOfItemToLockUnlock].Location or CurrentLocation == Items[IndexOfOtherSideItemToLockUnlock].Location:
    if Items[IndexOfItemToLockUnlock].Status == "locked":
      Items = ChangeStatusOfItem(Items, IndexOfItemToLockUnlock, "close")
      Items = ChangeStatusOfItem(Items, IndexOfOtherSideItemToLockUnlock, "close")
      Say(Items[IndexOfItemToLockUnlock].Name + " now unlocked.")
    elif Items[IndexOfItemToLockUnlock].Status == "close":
      Items = ChangeStatusOfItem(Items, IndexOfItemToLockUnlock, "locked")
      Items = ChangeStatusOfItem(Items, IndexOfOtherSideItemToLockUnlock, "locked")
      Say(Items[IndexOfItemToLockUnlock].Name + " now locked.")
    else:
      Say(Items[IndexOfItemToLockUnlock].Name + " is open so can't be locked.")
  else:
    Say("Can't use that key in this location.")
  return Items

def UseItem(Items, ItemToUse, CurrentLocation, Places):
  StopGame = False
  SubCommand = ""
  SubCommandParameter = ""
  IndexOfItem = GetIndexOfItem(ItemToUse, -1, Items)
  if IndexOfItem != -1:
    if Items[IndexOfItem].Location == INVENTORY or (Items[IndexOfItem].Location == CurrentLocation and "usable" in Items[IndexOfItem].Status):
      Position = GetPositionOfCommand(Items[IndexOfItem].Commands, "use")
      ResultForCommand = GetResultForCommand(Items[IndexOfItem].Results, Position)
      SubCommand, SubCommandParameter = ExtractResultForCommand(SubCommand, SubCommandParameter, ResultForCommand)
      if SubCommand == "say":
        Say(SubCommandParameter)
      elif SubCommand == "lockunlock":
        IndexOfItemToLockUnlock = GetIndexOfItem("", int(SubCommandParameter), Items)
        IndexOfOtherSideItemToLockUnlock = GetIndexOfItem("", int(SubCommandParameter) + ID_DIFFERENCE_FOR_OBJECT_IN_TWO_LOCATIONS, Items)
        Items = ChangeStatusOfDoor(Items, CurrentLocation, IndexOfItemToLockUnlock, IndexOfOtherSideItemToLockUnlock)
      elif SubCommand == "roll":
        Say("You have rolled a " + str(RollDie(ResultForCommand[5], ResultForCommand[7])))
      return StopGame, Items
  print("You can't use that!")
  return StopGame, Items

def ReadItem(Items, ItemToRead, CurrentLocation):
  SubCommand = ""
  SubCommandParameter = ""
  IndexOfItem = GetIndexOfItem(ItemToRead, -1, Items)
  if IndexOfItem == -1:
    print("You can't find " + ItemToRead + ".")
  elif not "read" in Items[IndexOfItem].Commands:
    print("You can't read " + ItemToRead + ".")
  elif Items[IndexOfItem].Location != CurrentLocation and Items[IndexOfItem].Location != INVENTORY:
    print("You can't find " + ItemToRead + ".")
  else:
    Position = GetPositionOfCommand(Items[IndexOfItem].Commands, "read")
    ResultForCommand = GetResultForCommand(Items[IndexOfItem].Results, Position)
    SubCommand, SubCommandParameter = ExtractResultForCommand(SubCommand, SubCommandParameter, ResultForCommand)
    if SubCommand == "say":
      Say(SubCommandParameter)

def GetItem(Items, ItemToGet, CurrentLocation):
  SubCommand = ""
  SubCommandParameter = ""
  CanGet = False
  IndexOfItem = GetIndexOfItem(ItemToGet, -1, Items)
  if IndexOfItem == -1:
    print("You can't find " + ItemToGet + ".")
  elif Items[IndexOfItem].Location == INVENTORY:
    print("You have already got that!")
  elif not "get" in Items[IndexOfItem].Commands:
    print("You can't get " + ItemToGet + ".")
  elif Items[IndexOfItem].Location >= MINIMUM_ID_FOR_ITEM and Items[GetIndexOfItem("", Items[IndexOfItem].Location, Items)].Location != CurrentLocation:
    print("You can't find " + ItemToGet + ".")
  elif Items[IndexOfItem].Location < MINIMUM_ID_FOR_ITEM and Items[IndexOfItem].Location != CurrentLocation:
    print("You can't find " + ItemToGet + ".")
  elif LookForSpaceInInventory(Items) == 0: #Added to support new feature resolving around looking for space in inventory
    print('Sorry your inventory is full!')
    CanGet = False
  else:
    CanGet = True
  if CanGet:
    Position = GetPositionOfCommand(Items[IndexOfItem].Commands, "get")
    ResultForCommand = GetResultForCommand(Items[IndexOfItem].Results, Position)
    SubCommand, SubCommandParameter = ExtractResultForCommand(SubCommand, SubCommandParameter, ResultForCommand)
    if SubCommand == "say":
      Say(SubCommandParameter)
    elif SubCommand == "win":
      Say("You have won the game")
      return True, Items
    if "gettable" in Items[IndexOfItem].Status:
      Items = ChangeLocationOfItem(Items, IndexOfItem, INVENTORY)
      print("You have got that now.")
  return False, Items

def CheckIfDiceGamePossible(Items, Characters, OtherCharacterName):
  PlayerHasDie = False
  PlayersInSameRoom = False
  IndexOfPlayerDie = -1
  IndexOfOtherCharacter = -1
  IndexOfOtherCharacterDie = -1
  OtherCharacterHasDie = False
  for Thing in Items:
    if Thing.Location == INVENTORY and "die" in Thing.Name:
      PlayerHasDie = True
      IndexOfPlayerDie = GetIndexOfItem("", Thing.ID, Items)
  Count = 1
  while Count < len(Characters) and not PlayersInSameRoom:
    if Characters[0].CurrentLocation == Characters[Count].CurrentLocation and Characters[Count].Name == OtherCharacterName:
      PlayersInSameRoom = True
      for Thing in Items:
        if Thing.Location == Characters[Count].ID and "die" in Thing.Name:
          OtherCharacterHasDie = True
          IndexOfOtherCharacterDie = GetIndexOfItem("", Thing.ID, Items)
          IndexOfOtherCharacter = Count
    Count += 1
  return PlayerHasDie and PlayersInSameRoom and OtherCharacterHasDie, IndexOfPlayerDie, IndexOfOtherCharacter, IndexOfOtherCharacterDie

def TakeItemFromOtherCharacter(Items, OtherCharacterID):
  ListOfIndicesOfItemsInInventory = []
  ListOfNamesOfItemsInInventory = []
  Count = 0
  while Count < len(Items):
    if Items[Count].Location == OtherCharacterID:
      ListOfIndicesOfItemsInInventory.append(Count)
      ListOfNamesOfItemsInInventory.append(Items[Count].Name)
    Count += 1
  Count = 1
  print("Which item do you want to take?  They have:", end = "")
  print(ListOfNamesOfItemsInInventory[0], end = "")
  while Count < len(ListOfNamesOfItemsInInventory) - 1:
    print(",", ListOfNamesOfItemsInInventory[Count], end = "")
    Count += 1
  print(".")
  ChosenItem = input()
  if ChosenItem in ListOfNamesOfItemsInInventory:
    print("You have that now.")
    Pos = ListOfNamesOfItemsInInventory.index(ChosenItem)
    Items = ChangeLocationOfItem(Items, ListOfIndicesOfItemsInInventory[Pos], INVENTORY)
  else:
    print("They don't have that item, so you don't take anything this time.")
  return Items

def TakeRandomItemFromPlayer(Items, OtherCharacterID):
  ListOfIndicesOfItemsInInventory = []
  Count = 0
  while Count < len(Items):
    if Items[Count].Location == INVENTORY:
      ListOfIndicesOfItemsInInventory.append(Count)
    Count += 1
  rno = GetRandomNumber(0, len(ListOfIndicesOfItemsInInventory) - 1)
  print("They have taken your " + Items[ListOfIndicesOfItemsInInventory[rno]].Name + ".")
  Items = ChangeLocationOfItem(Items, ListOfIndicesOfItemsInInventory[rno], OtherCharacterID)
  return Items

def PlayDiceGame(Characters, Items, OtherCharacterName):
  PlayerScore = 0
  OtherCharacterScore = 0
  DiceGamePossible, IndexOfPlayerDie, IndexOfOtherCharacter, IndexOfOtherCharacterDie = CheckIfDiceGamePossible(Items, Characters, OtherCharacterName)
  if not DiceGamePossible:
    print("You can't play a dice game.")
  else:
    Position = GetPositionOfCommand(Items[IndexOfPlayerDie].Commands, "use")
    ResultForCommand = GetResultForCommand(Items[IndexOfPlayerDie].Results, Position)
    PlayerScore = RollDie(ResultForCommand[5], ResultForCommand[7])
    print("You rolled a " + str(PlayerScore) + ".")
    Position = GetPositionOfCommand(Items[IndexOfOtherCharacterDie].Commands, "use")
    ResultForCommand = GetResultForCommand(Items[IndexOfOtherCharacterDie].Results, Position)
    OtherCharacterScore = RollDie(ResultForCommand[5], ResultForCommand[7])
    print("They rolled a " + str(OtherCharacterScore) + ".")
    if PlayerScore > OtherCharacterScore:
      print("You win!")
      Items = TakeItemFromOtherCharacter(Items, Characters[IndexOfOtherCharacter].ID)
    elif PlayerScore < OtherCharacterScore:
      print("You lose!")
      Items = TakeRandomItemFromPlayer(Items, Characters[IndexOfOtherCharacter].ID)
    else:
      print("Draw!")
  return Items

def MoveItem(Items, ItemToMove, CurrentLocation):
  SubCommand = ""
  SubCommandParameter = ""
  IndexOfItem = GetIndexOfItem(ItemToMove, -1, Items)
  if IndexOfItem != -1:
    if Items[IndexOfItem].Location == CurrentLocation:
      if len(Items[IndexOfItem].Commands) >= 4:
        if "move" in Items[IndexOfItem].Commands:
          Position = GetPositionOfCommand(Items[IndexOfItem].Commands, "move")
          ResultForCommand = GetResultForCommand(Items[IndexOfItem].Results, Position)
          SubCommand, SubCommandParameter = ExtractResultForCommand(SubCommand, SubCommandParameter, ResultForCommand)
          if SubCommand == "say":
            Say(SubCommandParameter)
          else:
            print("You can't move " + ItemToMove + ".")
        else:
          print("You can't move " + ItemToMove + ".")
      return
  print("You can't find " + ItemToMove + ".")

def DisplayInventory(Items): #Returns a list of strings for the items in inventory (list of strings not returned rather printed directly to user)
  print()
  print("You are currently carrying the following items:")
  for Thing in Items:
    if Thing.Location == INVENTORY:
      print(Thing.Name)

def DisplayGettableItemsInLocation(Items, CurrentLocation):
  ContainsGettableItems = False
  ListOfItems = "On the floor there is: "
  for Thing in Items:
    if Thing.Location == CurrentLocation and "gettable" in Thing.Status:
      if ContainsGettableItems:
        ListOfItems += ", "
      ListOfItems += Thing.Name
      ContainsGettableItems = True
  if ContainsGettableItems:
    print(ListOfItems + ".")

def DisplayOpenCloseMessage(ResultOfOpenClose, OpenCommand):
  if ResultOfOpenClose >= 0:
    if OpenCommand:
      Say("You have opened it.")
    else:
      Say("You have closed it.")
  elif ResultOfOpenClose == -3:
    Say("You can't do that, it is locked.")
  elif ResultOfOpenClose == -2:
    Say("It already is.")
  elif ResultOfOpenClose == -1:
    Say("You can't open that.")

def PlayGame(Characters, Items, Places):
  BuildMap(Places[Chracters[0].CurrentLocation-1].ID, 'null', 'null')
  StopGame = False
  Moved = True
  while not StopGame:
    if Places[Characters[0].CurrentLocation-1].ID not in PLACESVISITED:
      PLACESVISITED.append(Places[Characters[0].CurrentLocation-1].ID)
    if Moved:
      print()
      print()
      print(Places[Characters[0].CurrentLocation-1].Description)
      DisplayGettableItemsInLocation(Items, Characters[0].CurrentLocation)
      Moved = False
    Instruction = GetInstruction()
    Command, Instruction = ExtractCommand(Instruction)
    if Command == "get":
      StopGame, Items = GetItem(Items, Instruction, Characters[0].CurrentLocation)
    elif Command == "use":
      StopGame, Items = UseItem(Items, Instruction, Characters[0].CurrentLocation, Places)
    elif Command == "go":
      Characters[0], Moved = Go(Characters[0], Instruction, Places[Characters[0].CurrentLocation - 1])
    elif Command == "read":
      ReadItem(Items, Instruction, Characters[0].CurrentLocation)
    elif Command == "examine":
        if Instruction == 'room':
            Moved = True
        else:
            Examine(Items, Characters, Instruction, Characters[0].CurrentLocation)
    elif Command == "open":
      ResultOfOpenClose, Items, Places = OpenClose(True, Items, Places, Instruction, Characters[0].CurrentLocation)
      DisplayOpenCloseMessage(ResultOfOpenClose, True)
    elif Command == "close":
      ResultOfOpenClose, Items, Places = OpenClose(False, Items, Places, Instruction, Characters[0].CurrentLocation)
      DisplayOpenCloseMessage(ResultOfOpenClose, False)
    elif Command == "move":
      MoveItem(Items, Instruction, Characters[0].CurrentLocation)
    elif Command == "say":
      Say(Instruction)
    elif Command == "playdice":
      Items = PlayDiceGame(Characters, Items, Instruction)
    elif Command == "quit":
      Say("You decide to give up, try again another time.")
      StopGame = True

    # ADDITION: addition of new commands to further optimise or expand the game
    elif Command == 'eat':
        Items = EatItem(Items, Instruction, Characters[0].CurrentLocation, Places)
    elif Command == 'showmap':
        ShowMap()
    elif Command == 'hit':
        Items = UseWeapon(Characters, Items, Instruction)

    elif Command == 'teleport':
        Characters[0], Moved = Teleport(Characters[0], Instruction)

    elif Command == 'save':
        Save(Characters, Items, Places)

    elif Command == "help":
        cmds = ['get','use','go','read','examine','open','close','move','say','playdice']
        print('Commands: ')
        for cmd in cmds:
            print(i,end="\n")

    elif Command == 'addcharacter':
        Characters.append(AddCharacter())
    #END ADDITION

    else:
      print("Sorry, you don't know how to " + Command + ".")
  input()

def LoadGame(Filename, Characters, Items, Places):
  try:
    f = open(Filename, "rb")
    NoOfCharacters = pickle.load(f)
    for Count in range(NoOfCharacters):
      TempCharacter = Character()
      TempCharacter.ID = pickle.load(f)
      TempCharacter.Name = pickle.load(f)
      TempCharacter.Description = pickle.load(f)
      TempCharacter.CurrentLocation = pickle.load(f)
      Characters.append(TempCharacter)
    NoOfPlaces = pickle.load(f)
    for Count in range(0, NoOfPlaces):
      TempPlace = Place()
      TempPlace.ID = pickle.load(f)
      TempPlace.Description = pickle.load(f)
      TempPlace.North = pickle.load(f)
      TempPlace.East = pickle.load(f)
      TempPlace.South = pickle.load(f)
      TempPlace.West = pickle.load(f)
      TempPlace.Up = pickle.load(f)
      TempPlace.Down = pickle.load(f)
      Places.append(TempPlace)
    NoOfItems = pickle.load(f)
    for Count in range(0, NoOfItems):
      TempItem = Item()
      TempItem.ID = pickle.load(f)
      TempItem.Description = pickle.load(f)
      TempItem.Status = pickle.load(f)
      TempItem.Location = pickle.load(f)
      TempItem.Name = pickle.load(f)
      TempItem.Commands = pickle.load(f)
      TempItem.Results = pickle.load(f)
      Items.append(TempItem)
    return True, Characters, Items, Places
  except:
    return False, Characters, Items, Places

def Main():
  Items = []
  Characters = []
  Places = []
  Filename = input("Enter filename> ") + ".gme"
  print()
  GameLoaded, Characters, Items, Places = LoadGame(Filename, Characters, Items, Places)
  if GameLoaded:
    PlayGame(Characters, Items, Places)
  else:
    print("Unable to load game.")
    input()

if __name__ == "__main__":
  Main()
