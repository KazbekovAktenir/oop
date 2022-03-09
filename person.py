class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Jack(Person):
    def __init__(self, first_name, last_name, phone_number, balance):
        super().__init__(first_name, last_name)
        self.phone_number = phone_number
        self.balance = balance


dog = Jack('Sam', 'Black', '12345', 99)


class Vito(Jack):
    num = 70

    def __init__(self, first_name, last_name, phone_number, balance):
        super().__init__(first_name, last_name, phone_number, balance)

    def cat(self):
        p = dog.balance - self.num
        t = self.balance + p
        print(f'Cat:', t)


brad = Vito('Brad', 'Bone', '98765', 34)
Vito.cat(brad)
