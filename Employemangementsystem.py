#Employee Management System
# 1. Look up an employee
# 2. Add a new employee
# 3. Change an existing employee's details
# 4. Delete an employee
# 5. Quit


class Person:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def display(self):
        print(f"Name: {self.name}, Phone Number: {self.phone}")

class Employee(Person):
    def __init__(self, name, phone, employeeId, Department):
        super().__init__(name, phone)
        self.employeeId = employeeId
        self.Department = Department

    def display(self):
        print(f"ID: {self.employeeId}, Name: {self.name}, Phone Number: {self.phone}, Department: {self.Department}")

class EmployeeManagementSystem:
    def __init__(self):
        self.employees = {}

    def look_up_employee(self, emp_id):
        if emp_id in self.employees:
            self.employees[emp_id].display()
        else:
            print("Employee not found!")

    def add_employee(self):
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        emp_id = input("Enter employee ID: ")
        department = input("Enter department: ")
        new_employee = Employee(name, phone, emp_id, department)
        self.employees[emp_id] = new_employee
        print("Employee added successfully!")

    def change_employee_details(self):
        emp_id = input("Enter employee ID to update: ")
        if emp_id in self.employees:
            name = input("Enter new name: ")
            phone = input("Enter new phone number: ")
            department = input("Enter new department: ")
            self.employees[emp_id].name = name
            self.employees[emp_id].phone = phone
            self.employees[emp_id].Department = department  # Use the correct field name
            print("Employee details updated successfully!")
        else:
            print("Employee not found!")

    def delete_employee(self):
        emp_id = input("Enter employee ID to delete: ")
        if emp_id in self.employees:
            del self.employees[emp_id]
            print("Employee deleted successfully!")
        else:
            print("Employee not found!")

    def menu(self):
        while True:
            print("\nEmployee Management System")
            print("1. Look up an employee")
            print("2. Add a new employee")
            print("3. Change an existing employee's details")
            print("4. Delete an employee")
            print("5. Quit")
            choice = input("Enter your choice: ")

            if choice == "1":
                emp_id = input("Enter employee ID to look up: ")
                self.look_up_employee(emp_id)
            elif choice == "2":
                self.add_employee()
            elif choice == "3":
                self.change_employee_details()
            elif choice == "4":
                self.delete_employee()
            elif choice == "5":
                print("Exiting the system.")
                break
            else:
                print("Invalid choice! Please try again.")


# Running the system
if __name__ == "__main__":
    system = EmployeeManagementSystem()
    system.menu()
