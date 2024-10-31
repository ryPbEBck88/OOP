"""
Создайте базовый класс Person, у которого есть:
    1. метод __init__, принимающий имя и возраст человека. Их необходимо
       сохранить в атрибуты экземпляра nameи age соответственно.
    2. метод display_person_info , который печатает информацию в следующем виде:
       Person: {name}, {age}
Затем создайте класс Company , у которого есть:
    1. метод __init__, принимающий название компании и город ее основания.
       Их необходимо сохранить в атрибуты экземпляра company_name  и location
       соответственно.
    2. метод display_company_info , который печатает информацию в следующем
       виде:
       Company: {company_name}, {location}
И в конце создайте класс Employee , который:
    1. имеет метод __init__, принимающий имя человека, его возраст, название
       компании и город основания. Необходимо создать атрибут personal_data и
       сохранить в него экземпляр класса Person. И также создать атрибут work
       и сохранить в него экземпляр класса Company.
"""

class Person:
    """Класс работника."""
    def __init__(self, name: str, age: int) -> None:
        """
        Инициализирует имя и возраст работника.

        :param name: имя работника
        :param age: возраст работника
        """
        self.name = name
        self.age = age

    def display_person_info(self):
        """Выводим информацию о работнике: имя и возраст."""
        print(f"Person: {self.name}, {self.age}")


class Company:
    """Класс компании."""
    def __init__(self, company_name, location):
        """
        Инициализирует название компании и город основания.
        :param company_name: название компании.
        :param location: город основания.
        """
        self.company_name = company_name
        self.location = location

    def display_company_info(self):
        """Выводим информацию о компании: название и город основатель."""
        print(f"Company: {self.company_name}, {self.location}")


class Employee:
    """Класс сотрудника, который объединяет
    информацию о работнике и компании."""
    def __init__(self, name: str, age: int,
                 company_name: str, location: str) -> None:
        """
        Инициализирует информацию о работнике и его компании.

        :param name: имя работника
        :param age: возраст работника
        :param company_name: название компании, в которой работает сотрудник
        :param location: город, в котором находится компания
        """
        self.personal_data = Person(name, age)
        self.work = Company(company_name, location)


ivan = Person('Ivan', 32)
assert ivan.name == 'Ivan'
assert ivan.age == 32
ivan.display_person_info()

zara = Company('Zara', 'Prague')
assert zara.company_name == 'Zara'
assert zara.location == 'Prague'
zara.display_company_info()


emp = Employee('Jessica', 28, 'Google', 'Atlanta')
assert isinstance(emp.personal_data, Person)
assert isinstance(emp.work, Company)

assert emp.personal_data.name == 'Jessica'
assert emp.personal_data.age == 28
emp.personal_data.display_person_info()

assert emp.work.company_name == 'Google'
assert emp.work.location == 'Atlanta'
emp.work.display_company_info()

emp2 = Employee('Kolya', 11, 'Facebook', 'Seattle')
assert isinstance(emp2.personal_data, Person)
assert isinstance(emp2.work, Company)

assert emp2.personal_data.name == 'Kolya'
assert emp2.personal_data.age == 11
emp2.personal_data.display_person_info()

assert emp2.work.company_name == 'Facebook'
assert emp2.work.location == 'Seattle'
emp2.work.display_company_info()
