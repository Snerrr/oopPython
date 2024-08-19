import abc

class View(abc.ABC):
  @abc.abstractmethod
  def print_answer(answer : str):
    pass
  @abc.abstractmethod
  def start():
    pass


    
  