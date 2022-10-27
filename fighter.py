import os

class Fighter:

  def __init__(self, name: str, health: float, attack: float, defence: float, delay: float) -> None:
    self.name = name.capitalize()
    self.health = health
    self.attack = attack
    self.defence = defence
    self.delay = delay        
    self.time = 0


  def print_info(self) -> None:
    print(f'{(self.name)}\nHealth: {self.health}\nAttack: {self.attack}\nDefence: {self.defence}\nDelay: {self.delay}')


  def set_rival(self, rival: object) -> None:
      self.rival = rival


  def strike(self) -> None:
    self.actual_attack = round((self.attack - (self.attack * self.rival.defence / 100)), 2)
    self.rival.health = round((self.rival.health - self.actual_attack), 2)
    self.time += self.delay

    if self.rival.health < 0: self.rival.health  = 0

    print(f'{round(self.time, 2)} s\t\t{self.name} lyö ja tekee {self.actual_attack} vahinkoa.\t{self.rival.name}lle jäi {self.rival.health} Health')

  def is_winner(self) -> None:
    if self.rival.health == 0:
      print(self.name, 'voitti')
      os._exit(0) 