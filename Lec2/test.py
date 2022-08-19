class Employee:
    
    def __init__(self, name, address, years_of_experience, gender):
        self.name = name
        self.address = address
        self.years_of_experience = years_of_experience
        if years_of_experience >= 1 and years_of_experience <=5:
            self.salary = 5000
        elif years_of_experience >= 6 and years_of_experience <=10:
            self.salary = 7000
        else:
            self.salary = 10000
        self.gender = gender

    def __repr__(self):
        return f'{self.name}'

    def print_data(self):
        return {'name':self.name, 'address': self.address, 'year_of_experience': self.years_of_experience, 'salary':self.salary, 'gender':self.gender.print_data()}


class Gender:
    def __init__(self, id):
        self.id = id
        if id == 1:
            self.sex = 'male'
        else:
            self.sex = 'female'
    def print_data(self):
        return {'id': self.id, 'sex':self.sex}



e1 = Employee('Ali', 'Faysal', 7, Gender(2))
print(e1)

# print(e1.print_data())

# # e2 = Employee('Kareem', 'Haram', 3)



# # print(e2.print_data()) 

# l = []
# print(len(l))