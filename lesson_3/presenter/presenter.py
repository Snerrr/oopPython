import datetime
from models.family import Family
from models.human import Human
class Presenter():
  def __init__(self, Ui : object):
    self.Ui = Ui
    self.Family = Family([], "Korochinskiy")
  def view_family(self):
    self.Family.view_family()
  def append_human(self, name, gender, date):
    human = Human(name, gender, datetime.datetime.strptime(date, "%d.%m.%Y"), [], [])
    self.Family.append_human(human)
  def get_info(self):
    self.Family.get_info()
  def sorting_age(self):
    self.Family.sorting_age()
  def sorting_name(self):
    self.Family.sorting_name()
