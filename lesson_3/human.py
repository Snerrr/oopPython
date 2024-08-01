from dateutil.relativedelta import relativedelta 
import datetime
class Human():
  def __init__(self, name : str, gender : str, birthDate : datetime, parents : list, children : list):
    self.__name = name
    self.__gender = gender
    self.__birthDate = birthDate    ## Не хочу писать про смерть
    self.__parents = parents
    self.__children = children
  def get_age(self):
    return relativedelta(datetime.datetime.now(),self.__birthDate).years
  def append_children(self, children: object):
    self.__children.append(children)
  def to_dict(self):
    return {"name":self.__name,"gender":self.__gender, "birthDate":self.__birthDate,
            "parents":self.__parents,"children":self.__children}
  def get_info(self):
    return(f"name = {self.__name}, gender = {self.__gender}, age = {self.get_age()}")
