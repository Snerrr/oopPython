class Family():
  def __init__(self, humans : list, name: str):
    self.__name = name
    self.__humans = humans
  def append_human(self, human : object):
    self.__humans.append(human)
  def get_name(self):
    return self.__name
  def get_humans(self):
      return self.__humans
  def view_family(self):
    for element in self.__humans:
      print(element.get_info())
  def to_dict(self):
    return {"humans":[i.to_dict() for i in self.__humans]}
  def sorting_name(self):
    name_list = []
    for element in self.__humans:
      name_list.append(element.get_name())
    name_list.sort()
    return name_list
  def sorting_age(self):
    age_list = []
    for element in self.__humans:
      age_list.append(element.get_age())
    age_list.sort()
    return age_list
  def append_dog(self, dog : object):
    self.__humans.append(dog)