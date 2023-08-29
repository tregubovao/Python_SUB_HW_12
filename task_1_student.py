# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО 
# на первую заглавную букву и наличие только букв.
from os import system
system('cls')

class Requirements:

    def __set_name__(self, owner, name):
            self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        first_letter = ord(value[0])        
        START_CAP_LETTER = 1040
        FINISH_CAP_LETTER = 1071
        START_LOWERCASE = 1072
        FINISH_LOWERCASE = 1103
        if (first_letter <= START_CAP_LETTER 
            or first_letter >= FINISH_CAP_LETTER):
            raise ValueError('Неверный формат. Имя или фамилия начинаются НЕ с заглавной буквы')
        for i in range(2, len(value)):
            cur_letter = ord(value[i])
            if (cur_letter <= START_LOWERCASE 
                or cur_letter >= FINISH_LOWERCASE):
                raise ValueError(f'Неверный формат. В имени или фамилии присутствуют недопустимые символы.')
       
class Student:
    _name = Requirements()
    _surname = Requirements()

    def __init__(self, _name: str, _surname: str):
        self._name = _name
        self._surname = _surname


st1 = Student('Макс', 'Петров')
st2 = Student('вася', 'пупкин')
# st3 = Student('Мак1', 'Петро2')
# st1 = Student('МакС', 'ПетроВ')

print(st1._name, st1._surname)
# print(st2._name, st2._surname)
# print(st3._name, st3._surname)

