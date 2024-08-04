import pickle
from family import Family
from reader import Reader
class Family_reader(Reader):
  def __init__(self):
    pass
  def read(self,family_name):
    with open(f'oopPython/lesson_3/{family_name}.pkl', 'rb') as file:
      pkl_data = pickle.load(file)
      return Family(pkl_data.get_humans(), pkl_data.get_name())