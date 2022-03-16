import random

def shuffleCards():
  cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
  for i in range(3):
    for j in range(13):
      cards.append(cards[j])
  newCards = []
  for i in range(52):
    ind = random.randrange(0, len(cards))
    newCards.append(cards.pop(ind))
  return newCards

def gameOver(players):
  ind52 = -1
  for i in range(len(players)):
    leng = len(players[i].cards)
    if leng != 0 and ind52 == -1:
      ind52 = i
    elif leng != 0:
      return -1
  return ind52

def isFace(card : str):
  if card == "A":
    return 4
  elif card == "K":
    return 3
  elif card == "Q":
    return 2
  elif card == "J":
    return 1
  return 0

def isSlap(next, pile):
  if len(pile) == 0:
    return False
  elif len(pile) == 1:
    return (next == pile[0])
  return(next == pile[-1] or next == pile[-2])

def doSlap(pile, players):
  slapper = random.random()
  sumFloats = 0
  for i in range(len(players)):
    sumFloats += players[i].perc
    if sumFloats >= slapper:
      players[i].takePile(pile)
      return
