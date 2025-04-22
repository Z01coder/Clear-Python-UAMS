"""
Разрабатываю систему управления учетными записями пользователей для небольшой компании. Компания разделяет сотрудников на
обычных работников и администраторов. У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа и могут добавлять или удалять
пользователя из системы.

Требования:

1. Класс `User* [1]: Этот класс должен инкапсулировать [2] данные о пользователе: ID [3], имя [4] и уровень доступа [5]
('user' для обычных сотрудников).
2. Класс Admin [6]: Этот класс должен наследоваться от класса User. Добавь дополнительный атрибут уровня доступа [7],
специфичный для администраторов ('admin'). Класс должен также содержать методы add_user [8] и remove_user [9],
которые позволяют добавлять и удалять пользователей из списка (представь, что это просто список экземпляров User).
3. Инкапсуляция данных: атрибуты классов должны быть защищены от прямого доступа и модификации снаружи. Нужно предоставить
доступ к необходимым атрибутам [10] через методы (например, get и set методы).
"""


class User:  # Класс User [1]
    def __init__(self, id, name, access_level='user'):
        self._id = id                                   # ID [3] ставлю приватность protected "_" [2]
        self._name = name                               # Имя [4] ставлю приватность protected "_" [2]
        self._access_level = access_level               # Уровень доступа [5] ставлю приватность protected "_" [2]

    # Далее использую декоратор, чтобы не писать триста раз get \ set, и сделать код более "закрытым"
    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def access_level(self):
        return self._access_level

    @id.setter                          # Доступ к ID через метод set [10]
    def id(self, value):
        self._id = value

    @name.setter                        # Доступ к имени через метод set [10]
    def name(self, value):
        self._name = value

    @access_level.setter                # Доступ к уровню доступа через метод set [10]
    def access_level(self, value):
        self._access_level = value


class Admin(User):  # Класс Admin [6] дочерний класс "User"
    def __init__(self, id, name, access_level='admin'):  # Здесь дополнительный атрибут уровня доступа 'admin' [7]
        super().__init__(id, name, access_level=access_level)

    def add_user(self, new_user):  # Доп. метод для Админа [8] добавление сотрудника
        self.users.append(new_user)

    def remove_user(self, user_to_remove):  # Доп. метод для Админа [9] удаление сотрудника
        self.users.remove(user_to_remove)
