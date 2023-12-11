import doctest


class Worker:
    """Класс, описывающий работника"""

    def __init__(self, worker_name: str, worker_age: int, average_salary: float,):
        """
        Атрибуты:
        :param worker_name: имя работника
        :param worker_age: возраст работника
        :param average_salary: средняя зарплата работника
        Примеры:
        >>> worker = Worker("Danila" , 22, 120000.05) # Инициализация объекта класса с параметрами
        """

        self.student_name = worker_name
        self.student_age = worker_age
        self.average_ = average_salary

        if worker_age < 0:
            raise TypeError("Возраст работника не может быть меньше нуля")

        if not isinstance(worker_name, str):
            raise TypeError("Имя должно быть типа string")

        if average_salary < 0:
            raise TypeError("Зарплата не может быть меньше нуля")

    def get_information(self) -> str:
        """Метод получения информации о работнике
        return: Возвращает строку с тремя аргументами (имя, возраст, средняя зарплата работника)
        """

    def set_avg_salary(self, average_salary) -> int:
        """Метод, позволяющий изменить среднюю зарплату работникка
        Атрибуты:
        :param average_salary: новый атрибут new_average_salary, задающий новую среднюю зарплату работника
        return: Возвращает строку с обновленной средней зарплатой работника
        """


class Bookshelf:
    """Класс, описывающий книжную полку"""

    def __init__(self, amount_of_books: int, books: list):
        """
        Атрибуты:
        :param amount_of_books: количество книг на книжной полке
        :param books: книги, представленные в виде списка
        Примеры:
        >>> bookshelf = Bookshelf( 3, ["А.С Пушкин - Капитанская дочка", "И.С. Тургенев - Отцы и дети", "И.А. Гончаров - Обломов"]) # создание экземляра класса с параметрами
        """

        self.amount_of_books = amount_of_books
        self.books = books

        if amount_of_books < 0:
            raise TypeError("Ошибка! Количество книг не может быть отрицательным.")

        if not isinstance(books, list):
            raise TypeError("Ошибка! Книги должны быть представлены в виде списка.")

    def add_book(self, new_book) -> None:
        """Метод, позволяющирй добавлять новые книги на книжную полку
        :param new_book: книга, которая добавляется на книжную полку
        """

    def find_book(self) -> bool:
        """Метод, позволяющий найти книгу на книжной полке
        return: возвращает 1 если книга есть на книжной полке, 0 если книги нет
        """


class Phone:
    """Класс, описывающий телефон"""

    def __init__(self, brand: str, type_of_phone: str):
        """
        Атрибуты:
        :param brand: марка телефона
        :param type_of_phone: тип телефона (смартфон, стационарный, ...)
        Пример:
        >>> phone = Phone("IPhone", "Смартфон") # инициализация объекта класса с параметрами
        """

        self.brand = brand
        self.type_of_phone = type_of_phone

        if not isinstance(brand, str):
            raise TypeError("Ошибка! Бренд должен быть указан в виде строки!")

        if not isinstance(type_of_phone, str):
            raise TypeError("Ошибка! Тип телефона должен быть указан в виде строки!")

    def turn_on(self) -> None:
        """Метод для включения телефона"""

    def turn_off(self) -> None:
        """Метод для выключения телефона"""

    def call(self) -> None:
        """Метод звонка с телефона"""


if __name__ == "__main__":
    doctest.testmod()
    pass
