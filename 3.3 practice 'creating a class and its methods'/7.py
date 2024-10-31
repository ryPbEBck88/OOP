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


emp = Employee('Jessica', 28, 'Google', 'Atlanta')
print(emp.personal_data.name)
print(emp.personal_data.age)
emp.personal_data.display_person_info()
print(emp.work.company_name)
print(emp.work.location)
emp.work.display_company_info()
