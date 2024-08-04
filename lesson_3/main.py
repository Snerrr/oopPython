import human
import family
import datetime
import itterable_famiy
from family_writer import Family_writer
from family_reader import Family_reader
from dog import Dog
father = human.Human("Andrey", "man", datetime.datetime.strptime("12.08.1997", "%d.%m.%Y"), [], [])
mother = human.Human("Oly", "Women", datetime.datetime.strptime("12.02.1957", "%d.%m.%Y"), [], [])
children = human.Human("Misha", "man", datetime.datetime.strptime("19.03.2005", "%d.%m.%Y"), [father, mother], [])
dog = Dog(father, "Bobik", datetime.datetime.strptime("12.08.2021", "%d.%m.%Y"))
father.append_children(children)
mother.append_children(mother)
family_1 = family.Family([],"family_1")
family_1.append_human(father)
family_1.append_human(mother)
family_1.append_human(children)
family_1.append_dog(dog)
family_1.view_family()
print("---------------------------------------------")
Family_writer().write(family_1) ## запись класса в pickle файл
family_2 = Family_reader().read("family_1") ## читаем файл который мы записали 
family_2.view_family()
print("---------------------------------------------")
itterable = itterable_famiy.Itterable_family()
print(family_1.sorting_name())
print("---------------------------------------------")
print(family_1.sorting_age())


