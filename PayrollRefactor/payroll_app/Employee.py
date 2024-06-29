import self


class Employee:

    employee_id= None
    name_employee= None
    Last_name_employee= None
    email= None
    password = None
    salary = None

    #Constructor me va a crear las variables de instancia

    #Encapsulamiento "__" privado "_" protegido

    #Decoradores: son los @


    def  __init__(self, employee_id, name_employee, Last_name_employee, email, psssword, salary):
        self._employee_id = employee_id
        self._name_employee = name_employee
        self._Last_name_employee = Last_name_employee
        self._email = email
        self._password = psssword
        self._salary = salary

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        self._employee_id = employee_id

    @property
    def name_employee(self):
        return self._name_employee

    @name_employee.setter
    def name_employee(self, name_employee):
        self._name_employee = name_employee

    @property
    def Last_name_employee(self):
        return self._Last_name_employee

    @Last_name_employee.setter
    def Last_name_employee(self, Last_name_employee):
        self._Last_name_employee = Last_name_employee

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email=email

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password= password

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = salary

    employees = []

    def create_user(self, employees):
        employee = []
        self._employee_id = input("Id Empleado")
        employee.append(self._employee_id)
        self._name_employee = input("Nombre del empleado")
        employee.append(self._name_employee)
        self._Last_name_employee = input("Apellido del empleado")
        employee.append(self._Last_name_employee)
        self._email = input("Email del empleado")
        employee.append(self._email)
        self._password = input("Contraseña")
        employee.append(self._password)
        self._salary = input("Salario")
        employee.append(self._salary)

        employees.append(employee)


    def list_employee_data(self, employees):
        for item in employees:
            print(item)
















