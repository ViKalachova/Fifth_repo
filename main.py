from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and int(value):
            self.value = value
        else:
            raise ValueError

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    
    def add_phone(self, number):
        self.phones.append(Phone(number).value)

    def remove_phone(self, number):
        self.phones.remove(Phone(number).value)

    def edit_phone(self, number, new_number):
        pass
        # i = self.phones.index(number)
        # self.phones[i] = new_number

    def find_phone(self, number):
        for num in self.phones:
            if num == number:
                return num

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record.phones
        
    def find(self, name):
        for key, value in self.data.items():
            if str(key) == name:
                return value

    def delete(self, name):
        for key in list(self.data.keys()):
            if str(key) == name:
                del self.data[key]