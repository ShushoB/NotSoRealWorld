from abstract_classes import *
from concrete_classes import *
from abc import ABC, abstractmethod


Shahen = Child("Shahen", 2, "Male", None)
Beqa = Child("Beqa Lobjanidze", 27, "Male", None)
Beqa.verify()
Beqa = Adult("Beqa Lobjanidze", 27, "Male", "Engineer")
Shahen.job()
Shahen.verify()
print(Beqa.full_name)
Beqa.job()
Shushan = Adult("Shushan Barseghyan", 29, "Female", "Software developer")
Shushan.job()
Shushan.get_name()
Shushan.set_name("Shushanik Barseghyan")
oPhone = Phone("iPhone", Shushan.full_name)
Shushan.call(oPhone, Beqa.full_name)
Armenia = Country("Armenia")
Armenia.recognize_Artsakh()
Armenia.win_Eurovision('yes')
Georgia = Country("Georgia")
Georgia.win_Eurovision('no')
Shushan.travel(Georgia)
Beqa.travel(Armenia)
Puka = Cat('Puka', 'cat', 'black', 'female')
Puka.make_sound()
Beqa.adopt_pet(Puka)