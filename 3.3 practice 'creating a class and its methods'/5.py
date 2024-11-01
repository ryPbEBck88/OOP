# Создайте класс Worker, у которого есть:
#     1. Метод __init__, принимающий 4 аргумента: имя, зарплата
#        пол и паспорт. Необходимо сохранить их в следующих атрибутах: name,
#        salary, gender и passport
#     2. Метод get_info, который распечатает информацию о сотруднике в
#        следующем виде: "Worker {name}; passport-{passport}"

persons = [
    ('Allison Hill', 334053, 'M', '1635644202'),
    ('Megan Mcclain', 191161, 'F', '2101101595'),
    ('Brandon Hall', 731262, 'M', '6054749119'),
    ('Michelle Miles', 539898, 'M', '1355368461'),
    ('Donald Booth', 895667, 'M', '7736670978'),
    ('Gina Moore', 900581, 'F', '7018476624'),
    ('James Howard', 460663, 'F', '5461900982'),
    ('Monica Herrera', 496922, 'M', '2955495768'),
    ('Sandra Montgomery', 479201, 'M', '5111859731'),
    ('Amber Perez', 403445, 'M', '0602870126')
]


class Worker:

    def __init__(self, name: str, salary: int, gender: str, passport: str) -> None:
        """
        Инициализация работника.

        :param name: Имя работника
        :param salary: Зарплата работника
        :param gender: Пол работника
        :param passport: Номер паспорта работника
        """
        self.name = name
        self.salary = salary
        self.gender = gender
        self.passport = passport

    def get_info(self):
        """
        Выводим имя и паспорт работника.
        """
        print(f"Worker {self.name}; passport-{self.passport}")


worker_objects = []
for person in persons:
    worker_objects.append(Worker(*person))

for worker_object in worker_objects:
    worker_object.get_info()
