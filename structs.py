# Used to be a Card class, but cards are only their value in a string

class Player:
  def __init__(self, slapSkill):
    self.cards = []
    self.perc = slapSkill

  def takePile(self, pile):
    self.cards.extend(pile)