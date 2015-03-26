# Skeleton Program code for the AQA COMP1 Summer 2014 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA Programmer Team
# developed in the Python 3.2 programming environment
# version 2 edited 06/03/2014

import random, sys, pickle
from datetime import *

NO_OF_RECENT_SCORES = 3

class TCard():
  def __init__(self):
    self.Suit = 0
    self.Rank = 0

class TRecentScore():
  def __init__(self):
    self.Name = ''
    self.Score = 0
    self.Date = None

class option():
  def __init__(self, name='', value=False, opt_type=bool):
    self.name = name
    self.value = value
    self.opt_type = opt_type

Options = []
Deck = [None]
RecentScores = [None]
Choice = ''

def GetChoiceFromUser(prompt):
  accept = False
  acceptable_confirm_input = ["Y", "Yes", "yes", "y"]
  acceptable_deny_input = ["N", "No", "no", "n"]
  choice = ''
  while choice not in acceptable_confirm_input+acceptable_deny_input:
    choice = input(prompt)
    if choice in acceptable_confirm_input:
      Choice = "y"
      break
    elif choice in acceptable_deny_input:
      Choice = "n"
      break
    else:
      print("Invalid Input :(", file=sys.stderr)
      continue
  return Choice

def setOption(option_id, option_val, option_type=bool):
  global Options
  Options.append(option(option_id, option_val, option_type))

def flipOption(option_id):
  global Options

  #check if the option exists:
  try:
    tmp = Options[option_id]
    del tmp
    exists = True
  except IndexError:
    exists = False
  #if the option is a bool, and it exists, swap the value of the option
  if exists and Options[option_id].opt_type == bool:
    #the option is a bool
    Options[option_id].value = not Options[option_id].value
    print("The new value of {0} is {1}".format(Options[option_id].name, Options[option_id].value))
  #if the option isn't a bool, and it exists, offer other options
  elif exists and not Options[option_id].opt_type == bool:
    print("This option isn't a switch, it's current value is {0}, enter nothing to leave as-is, enter a value to change".format(Options[option_id].value))
    new_value = input(">>>")
    if (new_value.strip() != ""):
      Options[option_id].value = new_value
  #if the option doesn't exist, create it and give the user an option
  if not exists:
    choice = GetChoiceFromUser("This option doesn't exist, do you want to create it?")
    if choice == "y":
      new_option_name = input("Input the option's name:\n>>>")
      new_option_value = GetChoiceFromUser("Enter the options value (yes or no)")
      if new_option_value == "y":
        new_option_value = True
      elif new_option_value == "n":
        new_option_value = False
      setOption(new_option_name, new_option_value)
    else:
      print("Okay, cancelling...")
  
    
  #to set it.

def getflag(option_id):
  global Options
  for opt in Options:
    if(opt.name == option_id):
      return opt.value
  return None



getOption = getflag ## Function Assignment for shorthand and programming convention

def LoadOptions(options):
  try:
    with open("options.dat") as options_bin:
      options = pickle.load(options_bin)
  except FileNotFoundError:
    print("[  NB  ] Options file not found, loading defaults")
    setOption("AcesHigh", False, bool)
    setOption("Otherstuff", True, bool)

def ChangeOptionsMenu(options):
  print("Enter the ID of the option you want to change:")
  acceptable = False
  while not acceptable:
    try:
      choice = int(input(">>>"))
      if choice in list(range(len(options))):
        acceptable = True
      else:
        raise ValueError("oops!")
    except ValueError:
      print("Enter something valid!!!", file=sys.stderr)
  change_choice = GetChoiceFromUser("Do you want to change this value?")
  if change_choice == "y":
    flipOption(choice-1)

def DisplayOptions(options):
  print("{0:^15}  {1}".format("Option", "Value"))
  for index, opt in enumerate(options):
    print("{2} {0:<15} - {1}".format(opt.name, opt.value, index+1))
  ChangeOptionsMenu(options)    

def GetRank(RankNo):
  Rank = ''
  if RankNo == 1:
    Rank = 'Ace'
  elif RankNo == 2:
    Rank = 'Two'
  elif RankNo == 3:
    Rank = 'Three'
  elif RankNo == 4:
    Rank = 'Four'
  elif RankNo == 5:
    Rank = 'Five'
  elif RankNo == 6:
    Rank = 'Six'
  elif RankNo == 7:
    Rank = 'Seven'
  elif RankNo == 8:
    Rank = 'Eight'
  elif RankNo == 9:
    Rank = 'Nine'
  elif RankNo == 10:
    Rank = 'Ten'
  elif RankNo == 11:
    Rank = 'Jack'
  elif RankNo == 12:
    Rank = 'Queen'
  elif RankNo == 13:
    Rank = 'King'
  return Rank

def GetSuit(SuitNo):
  Suit = ''
  if SuitNo == 1:
    Suit = 'Clubs'
  elif SuitNo == 2:
    Suit = 'Diamonds'
  elif SuitNo == 3:
    Suit = 'Hearts'
  elif SuitNo == 4:
    Suit = 'Spades'
  return Suit

def DisplayMenu():
  print()
  print('MAIN MENU')
  print()
  print('1. Play game (with shuffle)')
  print('2. Play game (without shuffle)')
  print('3. Display recent scores')
  print('4. Reset recent scores')
  print('5. Options')
  print()
  print('Select an option from the menu (or enter q to quit): ', end='')

def GetMenuChoice():
  acceptable_input = ["q", "1", "2", "3", "4", "5"]
  try:
    choice = input("Enter yout choice:\n>>>")[0].lower()
  except IndexError:
    choice = ''
  while choice not in acceptable_input:
    try:
      choice = input("Invalid Input :{\nTry Again\nEnter yout choice:\n>>>")[0].lower()
    except IndexError:
      choice = ''
  return choice

def LoadDeck(Deck):
  CurrentFile = open('deck.txt', 'r')
  Count = 1
  while True:
    LineFromFile = CurrentFile.readline()
    if not LineFromFile:
      CurrentFile.close()
      break
    Deck[Count].Suit = int(LineFromFile)
    LineFromFile = CurrentFile.readline()
    Deck[Count].Rank = int(LineFromFile)
    Count = Count + 1
 
def ShuffleDeck(Deck):
  SwapSpace = TCard()
  NoOfSwaps = 1000
  for NoOfSwapsMadeSoFar in range(1, NoOfSwaps + 1):
    Position1 = random.randint(1, 52)
    Position2 = random.randint(1, 52)
    SwapSpace.Rank = Deck[Position1].Rank
    SwapSpace.Suit = Deck[Position1].Suit
    Deck[Position1].Rank = Deck[Position2].Rank
    Deck[Position1].Suit = Deck[Position2].Suit
    Deck[Position2].Rank = SwapSpace.Rank
    Deck[Position2].Suit = SwapSpace.Suit

def DisplayCard(ThisCard):
  print()
  print('Card is the', GetRank(ThisCard.Rank), 'of', GetSuit(ThisCard.Suit))
  print()

def GetCard(ThisCard, Deck, NoOfCardsTurnedOver):
  ThisCard.Rank = Deck[1].Rank
  ThisCard.Suit = Deck[1].Suit
  for Count in range(1, 52 - NoOfCardsTurnedOver):
    Deck[Count].Rank = Deck[Count + 1].Rank
    Deck[Count].Suit = Deck[Count + 1].Suit
  Deck[52 - NoOfCardsTurnedOver].Suit = 0
  Deck[52 - NoOfCardsTurnedOver].Rank = 0

def IsNextCardHigher(LastCard, NextCard):
  Higher = False
  if NextCard.Rank > LastCard.Rank:
    Higher = True
  elif getflag("AcesHigh") and NextCard.Rank == 1:
    Higher = False
  return Higher

def GetPlayerName():
  print()
  PlayerName = input('Please enter your name: ')
  while PlayerName.strip() == "":
    print("Please enter a value for your name!", sys.stderr)
    PlayerName = input("Please enter your name: ")
  print()
  return PlayerName

def DisplayEndOfGameMessage(Score):
  print()
  print('GAME OVER!')
  print('Your score was', Score)
  if Score == 51:
    print('WOW! You completed a perfect game.')
  print()

def DisplayCorrectGuessMessage(Score):
  print()
  print('Well done! You guessed correctly.')
  print('Your score is now ', Score, '.', sep='')
  print()

def ResetRecentScores(RecentScores):
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    RecentScores[Count].Name = ''
    RecentScores[Count].Score = 0

def DisplayRecentScores(RecentScores):
  #generate tabular widths:
  name_widths = []
  for score in RecentScores:
    try:
      name_widths.append(len(score.Name))
    except AttributeError:
      pass
  if max(name_widths) > 6:
    width = max(name_widths)+3
  else:
    width = 9
  print("{0:<{1}}{2:<7}{3}".format("Name", width, "Score", "Date"))
  for score in RecentScores:
    try:
      print("{0:<{1}}{2:<7}{3}".format(score.Name, width, score.Score, datetime.strftime(score.Date, "%d/%m/%y")))
    except AttributeError:
      pass
    except TypeError:
      print("End of list!")
      break
  print()
  

def UpdateRecentScores(RecentScores, Score):
  choice = GetChoiceFromUser("Do you want to add a highscore? (enter either Y or N)")
  if choice == "n":
    print("Okay :(")
    return 0
  PlayerName = GetPlayerName()
  FoundSpace = False
  Count = 1
  while (not FoundSpace) and (Count <= NO_OF_RECENT_SCORES):
    if RecentScores[Count].Name == '':
      FoundSpace = True
    else:
      Count = Count + 1
  if not FoundSpace:
    for Count in range(1, NO_OF_RECENT_SCORES):
      RecentScores[Count].Name = RecentScores[Count + 1].Name
      RecentScores[Count].Score = RecentScores[Count + 1].Score
    Count = NO_OF_RECENT_SCORES
  RecentScores[Count].Name = PlayerName
  RecentScores[Count].Score = Score
  RecentScores[Count].Date = datetime.now()

def PlayGame(Deck, RecentScores):
  LastCard = TCard()
  NextCard = TCard()
  GameOver = False
  GetCard(LastCard, Deck, 0)
  DisplayCard(LastCard)
  NoOfCardsTurnedOver = 1
  while (NoOfCardsTurnedOver < 52) and (not GameOver):
    GetCard(NextCard, Deck, NoOfCardsTurnedOver)
    Choice = ''
    while (Choice != 'y') and (Choice != 'n'):
      Choice = GetChoiceFromUser("Do you think the card will be higher or lower than the last card? (enter either 'y' or 'n') ")
    DisplayCard(NextCard)
    NoOfCardsTurnedOver = NoOfCardsTurnedOver + 1
    Higher = IsNextCardHigher(LastCard, NextCard)
    if (Higher and Choice == 'y') or (not Higher and Choice == 'n'):
      DisplayCorrectGuessMessage(NoOfCardsTurnedOver - 1)
      LastCard.Rank = NextCard.Rank
      LastCard.Suit = NextCard.Suit
    else:
      GameOver = True
  if GameOver:
    DisplayEndOfGameMessage(NoOfCardsTurnedOver - 2)
    UpdateRecentScores(RecentScores, NoOfCardsTurnedOver - 2)
  else:
    DisplayEndOfGameMessage(51)
    UpdateRecentScores(RecentScores, 51)

   

if __name__ == '__main__':
  LoadOptions(Options)
  for Count in range(1, 53):
    Deck.append(TCard())
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    RecentScores.append(TRecentScore())
  Choice = ''
  while Choice != 'q':
    DisplayMenu()
    Choice = GetMenuChoice()
    if Choice == '1':
      LoadDeck(Deck)
      ShuffleDeck(Deck)
      PlayGame(Deck, RecentScores)
    elif Choice == '2':
      LoadDeck(Deck)
      PlayGame(Deck, RecentScores)
    elif Choice == '3':
      DisplayRecentScores(RecentScores)
    elif Choice == '4':
      ResetRecentScores(RecentScores)
    elif Choice == "5":
      DisplayOptions(Options)
