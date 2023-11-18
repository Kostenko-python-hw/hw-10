from collections import UserDict
from utils import sanitize_phone_number


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        self.validate(value)
        super().__init__(value)
    
    def validate(self, phone):
        int(sanitize_phone_number(phone))
        sunitized_phone = sanitize_phone_number(phone)
        if len(sunitized_phone) != 10:
            raise ValueError()


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        filtred_array = list(filter(lambda el: el.value != phone, self.phones))
        if len(filtred_array) != len(self.phones):
            self.phones = filtred_array
        else:
            raise ValueError()

    def edit_phone(self, old_phone, new_phone):
        _index = None
        for index, el in enumerate(self.phones):
            if el.value == old_phone:
                _index = index
                break
        if _index is None:
            raise ValueError('The phone you want to change was not found')
        else:
            _new_Phone = Phone(new_phone)
            self.phones[_index] = _new_Phone

    def find_phone(self, phone):
        for el in self.phones:
            if phone == el.value:
                return el

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    
    def add_record(self, record):
        if record.name.value in self.data:
            raise ValueError(f"Record with name '{record.name.value}' already exists.")
        
        self.data[record.name.value] = record

    def find(self, name):
     
        if name in self.data:
            return self.data[name]

    def delete(self, name):
        if name in self.data:
            del self.data[name]
