# main class
class BaseContact:
    def __init__(self, name, surname, pers_phone, email):
        self.name = name
        self.surname = surname
        self.pers_phone = pers_phone
        self.email = email


person = BaseContact(name="Kate", surname="Smith", pers_phone="+4888921422", email="katesmith@gmail.com")
person1 = BaseContact(name="John", surname="Leon", pers_phone="+4819830033", email="johnleon@gmail.com")
person2 = BaseContact(name="Michael", surname="Jackson", pers_phone="+4821910422", email="mckon2@gmail.com")
person3 = BaseContact(name="Sasha", surname="Landau", pers_phone="+4813913100", email="landau@gmail.com")
person4 = BaseContact(name="Andrew", surname="Joly", pers_phone="+4814920492", email="andrewfpf@gmail.com")


# inheritance
class BusinessContact(BaseContact):
    def __init__(self, position, company, work_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company = company
        self.work_phone = work_phone


per = BusinessContact(company="Nestle", position="CEO", work_phone="+8914828422")
per1 = BusinessContact(company="Sony", position="SMM", work_phone="+313128422")
per2 = BusinessContact(company="Records", position="singer", work_phone="+199320032")
per3 = BusinessContact(company="Friends", position="teacher", work_phone="+523525390")
per4 = BusinessContact(company="Galaxy", position="manager", work_phone="+9970768688")
