from flask import Flask, jsonify

app = Flask(__name__)

class Employee:
    def __init__(self, id, name, tel, salary):
        self.id = id
        self.name = name
        self.tel = tel
        self.salary = salary

    def getData(self):
        return {'id':self.id, 'name':self.name, 'tel':self.tel, 'salary':self.salary}

e1 = Employee(1, "Ali", "01111111", 5000)
e2 = Employee(2, "Ali", "01111111", 6000)
e3 = Employee(3, "Sami", "01111111", 54000)
e4 = Employee(4, "Hassam", "01111111", 5000)


@app.route('/hello', methods=['GET'])
def helloworld():
    employees = [e1.getData(), e2.getData(), e3.getData(), e4.getData()]
    return jsonify(employees)

# app.run(debug=True)
if __name__ == '__main__':
    app.run(debug=True)
else:
    print('hi ahmed')