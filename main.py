from faker import Faker

fake = Faker("pl_PL")


class BaseContact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        self.len_card = len.__name__

    def __str__(self):
        return f"{self.name}, {self.phone}, {self.email}"

    def contact(self):
        return f"Wybieram numer {self.phone} i dzwonię do {self.name}"

    @property
    def label_lenght(self):
        return self.len_card


def create_contact(sort, amount):
    lista = []
    for i in range(amount):
        if sort == BaseContact:
            x = BaseContact(
                name=fake.name(), phone=fake.phone_number(), email=fake.email()
            )
            lista.append(x)
            return lista
        elif sort == BusinessContact:
            x = BusinessContact(
                name=fake.name(),
                phone=fake.phone_number(),
                email=fake.email(),
                firm=fake.company(),
                position=fake.job(),
                work_phone=fake.phone_number(),
            )
            lista.append(x)
            return lista


class BusinessContact(BaseContact):
    def __init__(self, work_phone, firm, position, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.work_phone = work_phone
        self.firm = firm
        self.position = position

    def __str__(self):
        return f"{self.name}, {self.phone}, {self.email},{self.firm}, {self.work_phone}, {self.position}"

    def contact(self):
        return f"Wybieram numer {self.work_phone} i dzwonię do {self.name}"


if __name__ == "__main__":
    BaseContact_one = BaseContact(
        name=fake.name(), phone=fake.phone_number(), email=fake.email()
    )
    BaseContact_two = BaseContact(
        name=fake.name(), phone=fake.phone_number(), email=fake.email()
    )
    BaseContact_three = BaseContact(
        name=fake.name(), phone=fake.phone_number(), email=fake.email()
    )
    BusinessContact_one = BusinessContact(
        name=fake.name(),
        phone=fake.phone_number(),
        email=fake.email(),
        firm=fake.company(),
        position=fake.job(),
        work_phone=fake.phone_number(),
    )
    BusinessContact_two = BusinessContact(
        name=fake.name(),
        phone=fake.phone_number(),
        email=fake.email(),
        firm=fake.company(),
        position=fake.job(),
        work_phone=fake.phone_number(),
    )
    BusinessContact_three = BusinessContact(
        name=fake.name(),
        phone=fake.phone_number(),
        email=fake.email(),
        firm=fake.company(),
        position=fake.job(),
        work_phone=fake.phone_number(),
    )

    print(BaseContact_one)
    print(BaseContact_two)
    print(BaseContact_three)
    print(BusinessContact_one)
    print(BusinessContact_two)
    print(BusinessContact_three)
    print(create_contact(BusinessContact, 10))
    print(BaseContact_one.contact())
