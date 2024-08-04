from itterable import Itterable
from family import Family
class Itterable_family(Itterable):
  def __init__(self):
    self.__cur_Index = 0
  def has_next(self, family: Family):
    if len(family.get_humans()) > self.__cur_Index - 1:
      return True
    else:
      return False
  def next(self, family : Family):
    if self.has_next(family) == True:
      element = family.get_humans()[self.__cur_Index]
      self.__cur_Index += 1
      return element
