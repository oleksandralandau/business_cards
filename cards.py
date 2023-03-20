# first class
class BaseContact:
    def __init__(self, name, surname, pers_phone, email):
        self.name = name
        self.surname = surname
        self.pers_phone = pers_phone
        self.email = email

    def contact(self):
        print("I'm dialing", self.pers_phone, "and calling to", self.name, self.surname)

    def label_length(self):
        print(len(self.name) + len(self.surname))


person = BaseContact(name="Kate", surname="Smith", pers_phone="+4888921422", email="katesmith@gmail.com")
person2 = BaseContact(name="John", surname="Leon", pers_phone="+4819830033", email="johnleon@gmail.com")
person3 = BaseContact(name="Michael", surname="Jackson", pers_phone="+4821910422", email="mckon2@gmail.com")
person4 = BaseContact(name="Sasha", surname="Landau", pers_phone="+4813913100", email="landau@gmail.com")
person5 = BaseContact(name="Andrew", surname="Joly", pers_phone="+4814920492", email="andrewfpf@gmail.com")


# inheritance
class BusinessContact(BaseContact):
    def __init__(self, position, company, work_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company = company
        self.work_phone = work_phone

    def contact(self):
        print("I'm dialing", self.work_phone, "and calling to", self.name, self.surname)

    def label_length(self):
        print(len(self.name) + len(self.surname))


b_contact = BusinessContact(name="Kate", surname="Smith", pers_phone="+4888921422", email="katesmith@gmail.com", company="Nestle", position="CEO", work_phone="+8914828422")
b_contact2 = BusinessContact(name="John", surname="Leon", pers_phone="+4819830033", email="johnleon@gmail.com", company="Sony", position="SMM", work_phone="+3131289422")
b_contact3 = BusinessContact(name="Michael", surname="Jackson", pers_phone="+4821910422", email="mckon2@gmail.com", company="Records", position="singer", work_phone="+1993200372")
b_contact4 = BusinessContact(name="Sasha", surname="Landau", pers_phone="+4813913100", email="landau@gmail.com", company="Friends", position="teacher", work_phone="+5235225390")
b_contact5 = BusinessContact(name="Andrew", surname="Joly", pers_phone="+4814920492", email="andrewfpf@gmail.com", company="Galaxy", position="manager", work_phone="+9970768688")


BaseContact.contact(person2)
BusinessContact.contact(b_contact2)
BaseContact.label_length(person2)
BusinessContact.label_length(b_contact3)

from faker import Faker

fake = Faker()

print(fake.name())