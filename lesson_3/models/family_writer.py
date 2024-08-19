import pickle
from family import Family
from oopPython.lesson_3.models.writer import Writer
class Family_writer(Writer):
  def __init__(self):
    pass
  def write(self,family : Family):
      with open(f'oopPython/lesson_3/{family.get_name()}.pkl', 'wb') as file:
        pickle.dump(family, file)
