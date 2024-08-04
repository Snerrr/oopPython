import datetime
from dateutil.relativedelta import relativedelta
from human import Human
class Dog():
  def __init__(self, master : Human, name : str, birthDate : datetime):
    self.__master = master
    self.__name = name
    self.__birthDate = birthDate
  def get_master(self):
    return self.__master
  def get_name(self):
    return self.__name
  def get_age(self):
    return relativedelta(datetime.datetime.now(),self.__birthDate).years
  def get_info(self):
    return(f"name = {self.__name}, master = {self.__master}, age = {self.get_age()}")
