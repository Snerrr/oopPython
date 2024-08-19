import datetime
from oopPython.lesson_3.views.view import View
from oopPython.lesson_3.presenter import Presenter
import text

class Ui(View):
  def __init__(self):
    self.__presenter = Presenter(self)
  def print_answer(answer : str):
    return answer
  def imput_answer():
    return int(str(input(text.imput_number)))
  def start(self):
    while True:
      choise = self.imput_answer()
      match choise:
            case 1:
                self.__presenter.view_family()
            case 2:
                name = str(input("Введите имя: "))
                gender = str(input("Введите пол: "))
                date = datetime.datetime.strptime(str(input(("Введите дату рождения"))), "%d.%m.%Y")
                self.__presenter.append_human(name, gender, date)
                print("Успешно добавлено")
            case 3:
                self.__presenter.get_info()
            case 4:
                self.__presenter.sorting_age()
            case 5:
                self.__presenter.sorting_name()
            case 6:
                print(text.menu_close)