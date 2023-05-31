from employee import Employee

class SalaryManagement:
    def __init__(self):
        self.employee_list = []

    def add_employee(self, id, name, salary):
        employee = Employee(id, name, salary)
        self.employee_list.append(employee)
        print("Employee added successfully.")

    def view_employees(self):
        if len(self.employee_list) == 0:
            print("No employees registered.")
        else:
            print("Employee List:")
            for employee in self.employee_list:
                print(f"ID: {employee.id}, Name: {employee.name}, Salary: {employee.salary}")

    def update_salary(self, id, new_salary):
        employee = self.find_employee(id)
        if employee is not None:
            employee.salary = new_salary
            print("Employee salary updated successfully.")
        else:
            print("Employee not found.")
            
    def update_name(self, id, new_name):
        employee = self.find_employee(id)
        if employee is not None:
            employee.name = new_name
            print("Employee name updated successfully.")
        else:
            print("Employee not found.")

    def remove_employee(self, id):
        employee = self.find_employee(id)
        if employee is not None:
            self.employee_list.remove(employee)
            print("Employee removed successfully.")
        else:
            print("Employee not found.")
            
    def remove_all_employee(self):
        self.employee_list = []

    def find_employee(self, id, display=False):
        for employee in self.employee_list:
            if employee.id == id:
                if display == True:
                    print(f"ID: {employee.id}, Name: {employee.name}, Salary: {employee.salary}")
                else:
                    return employee
        return None
    
    def ask_repeat_again(self, action_type):
        continue_input = input("Do you want to {} again? (Y/N): ".format(action_type))
        if continue_input.upper() != "Y":
            return False  
        else:
            return True  
        
    def handle_invalid_choice(self):
        print("Invalid choice. Please enter a number from 1 to 2.")
        while True:
            continue_input = input("Do you want to try again? (Y/N): ")
            if continue_input.upper() != "Y":
                return False
            else:
                return True