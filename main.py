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
        if len(value) == 10:
            self.value = value
        else:
            self.value = ''

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    
    def add_phone(self, number):
        self.phones.append(Phone(number))

    def remove_phone(self, number):
        self.phones.remove(Phone(number))

    def edit_phone(self, number, new_number):
        i = self.phones.index(Phone(number))
        self.phones[i] = Phone(new_number)

    def find_phone(self, number):
        for num in self.number:
            if num == number:
                return num

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name] = record.phones
        
    def find(self, name):
        return self.data[Record(name)]
        
    def delete(self, name):
        del self.data[name]




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
    print(john)
    # john.edit_phone("1234567890", "1112223333")
    # print(john)
    # found_phone = john.find_phone("5555555555")
    # print(f"{john.name}: {found_phone}")
    # book.delete("Jane")
    # print(book)
    # print(jane_record)
