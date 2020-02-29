from src.bubble_types import BubbleTypes

class Bubble:

  def __init__(self, type):
    self.type = type

  # returns the bubble's current health points (no. of touches left until it gets destroyed)
  def current_hp(self):
    return int(self.type)
  
  # decrements the bubble's health points
  def decrement_hp(self):
    if self.type != BubbleTypes.Empty:
      hp = self.current_hp() - 1
      self.type = BubbleTypes(hp)

  def __str__(self):
    return str(self.type.value)

  def __eq__(self, other):
    if not isinstance(other, Bubble):
      return False
    
    return self.type == other.type
