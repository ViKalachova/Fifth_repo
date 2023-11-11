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
        try:
            len(value) == 10
            self.value = value
        except ValueError:
            print (f'The entered number {value} is incorrect')

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




if __name__ == '__main__':
    book = AddressBook()
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    book.add_record(john_record)
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)
    for name, record in book.data.items():
        print(name, record)
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")
    print(john)
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")
    book.delete("Jane")
    print(book)



