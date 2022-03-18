from structs import Player
from helpers import shuffleCards, gameOver, isFace, isSlap, doSlap
import time, random, sys, os

def runSim(numP, slapPerc):
  players = []
  if len(slapPerc) != numP:
    for i in range(numP):
      slapPerc.append(float(1 / numP))
  for i in range(numP):
    players.append(Player(slapPerc[i]))
  deck = shuffleCards()
  # deal the cards
  ind = 0
  while(len(deck) > 0):
    players[ind % numP].cards.append(deck.pop(0))
    ind += 1
  # simulate game
  turnInd = 0
  faceCard = -1
  pile = []
  lastFace = -1
  while(gameOver(players) == -1):
    #print(f"{turnInd=}, {faceCard=}, p1 has {len(players[0].cards)}, p2 has {len(players[1].cards)}, pile has {len(pile)}")
    if faceCard == 0:
      players[lastFace].takePile(pile)
      pile = []
      faceCard = -1
      turnInd = (turnInd + 1) % numP
      continue
    if len(players[turnInd].cards) == 0:
      turnInd = (turnInd + 1) % numP
      continue
    nextCard = players[turnInd].cards.pop(0)
    if faceCard != -1:
      faceCard -= 1
    if isSlap(nextCard, pile):
      #print("is slap")
      pile.append(nextCard)
      doSlap(pile, players)
      faceCard = -1
      pile = []
      turnInd = (turnInd + 1) % numP
      continue
    elif isFace(nextCard) != 0:
      #print("new face card")
      faceCard = isFace(nextCard)
      lastFace = turnInd
      turnInd = (turnInd + 1) % numP
    elif faceCard == -1:
      turnInd = (turnInd + 1) % numP
    pile.append(nextCard)
  return gameOver(players)

def runReactionTime():
  print("Input the number of players: ")
  numPlayers = int(input())
  playerTimes = [[] for x in range(numPlayers)]
  for i in range(numPlayers):
    print(f"Player {i+1} will now take 5 reaction time tests. Are you ready?")
    input()
    for j in range(5):
      timeUntil = random.random() * 1.5 + 0.75
      time.sleep(timeUntil)
      print("Enter any character")
      t1 = time.time()
      throwaway = input()
      t2 = time.time()
      playerTimes[i].append(t2 - t1)
      print(f"Player {i+1}, test {j+1} took {t2 - t1} seconds")
  avgs = []
  for i in range(numPlayers):
    tot = sum(playerTimes[i])
    avgs.append(tot / len(playerTimes[i]))
  bigAvg = sum(avgs) / len(avgs)
  standard = 1.0 / numPlayers
  skills = [standard for x in range(numPlayers)]
  for i in range(numPlayers):
    diff = ((bigAvg - avgs[i]) / bigAvg) * standard
    skills[i] += diff
  print("Input the number of simulations: ")
  numSims = int(input())
  wins = [0 for i in range(numPlayers)]
  startTime = time.time()
  for i in range(numSims):
    winner = runSim(numPlayers, skills)
    wins[winner] += 1
  endTime = time.time()
  print(f"Statistics over {numSims} games")
  for i in range(numPlayers):
    print(f"Player {i+1} with {skills[i]} skill won {wins[i]} times ({wins[i] / numSims})")
  print(f"Simulations ran in {endTime - startTime} seconds")

def runNormal():
  print("Input the number of players: ")
  numPlayers = int(input())
  print("Input the respective players' skill at slapping\nConditions: 0 <= each players' skill <= 1, leave blank if equal, must sum to 1")
  chances = []
  l = input().split()
  if len(l) != numPlayers:
    print("Invalid input")
    return
  for i in l:
    chances.append(float(i))
  print("Input the number of simulations: ")
  numSims = int(input())
  wins = [0 for x in range(numPlayers)]
  startTime = time.time()
  for i in range(numSims):
    winner = runSim(numPlayers, chances)
    wins[winner] += 1
  endTime = time.time()
  print(f"Statistics over {numSims} games")
  for i in range(numPlayers):
    print(f"Player {i+1} won {wins[i]} times ({wins[i] / numSims})")
  print(f"Simulations ran in {endTime - startTime} seconds")

def main():
  print("Would you like to take reaction time tests?")
  s = input().lower()
  if s == "yes":
    runReactionTime()
  else:
    runNormal()

main()