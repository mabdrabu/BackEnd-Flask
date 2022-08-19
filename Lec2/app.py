from flask import Flask, jsonify, request

emp_list = []

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

class Employee:
    def __init__(self, id, name, address, gender, title, salary, years_of_experience, is_married):
        self.id = id
        self.name = name
        self.address= address
        self.gender = gender
        self.title = title
        self.salary = salary
        self.years_of_experience = years_of_experience
        self.is_married = is_married

    def get_employee_data(self):
        return {
            'id':self.id,
            'name':self.name,
            'address':self.address,
            'gender':self.gender.get_gender(),
            'title':self.title.get_title(),
            'salary':self.salary,
            'years_of_experience':self.years_of_experience,
            'is_married':self.is_married
        }

class Gender:
    def __init__(self, id):
        self.id = id
        if id == 1:
            self.sex = 'Male'
        else:
            self.sex = 'Female'
    def get_gender(self):
        return {'id': self.id, 'sex': self.sex}

class Title:
    def __init__(self, id):
        self.id = id
        if id == 1:
            self.title = 'Dr.'
        elif id == 2:
            self.title = 'Eng.'
        elif id == 3:
            self.title = 'Mr.'
        elif id == 4:
            self.title = 'Mrs.'
        elif id == 5:
            self.title = 'Ms.'
        else:
            self.title = None
    def get_title(self):
        return {'id':self.id, 'title':self.title}

@app.route('/employee', methods=['POST'])
def add_employee():
    emp_id = len(emp_list)+1
    emp_name = request.json['name']
    emp_address = request.json['address']
    emp_gender_id = request.json['gender_id']
    emp_title_id = request.json['title_id']
    emp_salary = request.json['salary']
    emp_years_of_experience = request.json['years_of_experience']
    emp_is_married = request.json['is_married']
    gender = Gender(emp_gender_id)
    title = Title(emp_title_id)
    employee = Employee(emp_id, emp_name, emp_address, gender, title, emp_salary, emp_years_of_experience, emp_is_married)
    emp_list.append(employee.get_employee_data())
    return jsonify(emp_list[-1])


if __name__ == '__main__':
    app.run(debug= True)

    