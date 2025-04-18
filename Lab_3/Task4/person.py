import datetime


class Person:
    def __init__(self, name, year_of_birth, address=''):
        self.name = name
        self.yob = year_of_birth
        self.address = address

    def get_age(self):
        now = datetime.datetime.now()
        return now.year - self.yob  # Исправлено: теперь правильно вычисляется возраст

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name  # Исправлено: теперь правильно устанавливается имя

    def set_address(self, address):
        self.address = address  # Исправлено: было сравнение вместо присваивания

    def get_address(self):
        return self.address

    def is_homeless(self):
        '''
        returns True if address is not set, false in other case
        '''
        return not self.address  # Исправлено: проверяем self.address вместо address