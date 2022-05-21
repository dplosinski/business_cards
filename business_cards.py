from faker import Faker

fake = Faker()

class Card:
    def __init__(self, name, surname, company, position, email):
        self.name = name
        self.surname = surname
        self.company = company
        self.position = position
        self.email = email
    def __str__(self):
        return f'{self.name} {self.surname} {self.company} {self.position} {self.email}'


class Base_contact(Card):
    def __init__(self, name, surname, company, position, email, phone_number):
        super().__init__(name, surname, company, position, email)
        self.phone_number = phone_number
        self._name_length = 0
    def __repr__(self):
        return f'Base_contact("{self.name}", "{self.surname}", "{self.company}", "{self.position}", "{self.email}", "{self.phone_number}")'

    def contact(self):
        print("Kontakuję sie z " + str(self.phone_number))
    @property
    def name_length(self):
        _name_length = len(self.name) + len(self.surname)
        print(_name_length)


class Business_contact(Card):
    def __init__(self, name, surname, company, position, email, business_phone_number):
        super().__init__(name, surname, company, position, email)
        self.business_phone_number = business_phone_number
        self._name_length = 0
    def __repr__(self):
        return f'Business_contact("{self.name}", "{self.surname}", "{self.company}", "{self.position}", "{self.email}", "{self.business_phone_number}")'
    def contact(self):
        print("Kontakuję sie z " + str(self.business_phone_number))
    @property
    def name_length(self):
        _name_length = len(self.name) + len(self.surname)
        print(_name_length)

def create_contacts(type, number):
    empty = []
    for i in range(0, number):
        if type == 'business':
            first_name = fake.first_name()
            last_name = fake.last_name()
            emails = fake.email()
            business_phone_numbers = fake.phone_number()
            positions = fake.job()
            companies = fake.company()
            i = Business_contact(name = first_name, surname=last_name, email=emails, business_phone_number=business_phone_numbers, position=positions, company=companies)
            empty.append(i)
        elif type == 'base':
            first_name = fake.first_name()
            last_name = fake.last_name()
            emails = fake.email()
            phone_numbers = fake.phone_number()
            positions = fake.job()
            companies = fake.company()
            i = Base_contact(name = first_name, surname=last_name, email=emails, phone_number=phone_numbers, position=positions, company=companies)
            empty.append(i)
            
    print(empty)

create_contacts('business', 1)
create_contacts('base', 1)

