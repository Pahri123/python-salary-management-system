from salary_management import SalaryManagement
sm = SalaryManagement()

while True:
    print('''
Employee CRUD Python
=====================
1) Create
2) Read
3) Update
4) Delete
5) Exit      
      ''')
    choice = int(input("Choose an option (1-5): "))
    if choice == 1:
        print("Create New Employee")
        while True:
            id = str(input("Insert ID: "))
            name = str(input("Insert Name: "))
            salary = int(input("Insert Salary: "))
            sm.add_employee(id, name, salary)
            
            if not sm.ask_repeat_again("create"):
                break
            
    elif choice == 2:
        print('''
Read Employee
1) View all
2) Search Employee''')
        while True:
            readChoice = int(input("Choose an option (1-2): "))
            if readChoice == 1:
                sm.view_employees()
            elif readChoice == 2:
                readId = str(input("Insert ID: "))
                sm.find_employee(readId, True)
            else:
                if not sm.handle_invalid_choice():
                    break
                else:
                    continue
            if readChoice in [1, 2] and not sm.ask_repeat_again("read"):
                break
            
                
    elif choice == 3:
        print('''
Update Employee
1) Update name
2) Update salary''')
        while True:
            updateChoice = int(input("Choose an option (1-2): "))
            if updateChoice == 1:
                updateId = str(input("Insert ID: "))
                updateName = str(input("Insert New Name: "))
                sm.update_name(updateId, updateName)
            elif updateChoice == 2:
                updateId = str(input("Insert ID: "))
                updateSalary = int(input("Insert New Salary: "))
                sm.update_salary(updateId, updateSalary)
            else:
                if not sm.handle_invalid_choice():
                    break
                else:
                    continue
            if updateChoice in [1, 2] and not sm.ask_repeat_again("update"):
                break
            
    elif choice == 4:
        print('''
Delete Employee
1) Find and delete 
2) Delete all''')
        while True:
            deleteChoice = int(input("Choose an option (1-2): "))
            if deleteChoice == 1:
                deleteId = str(input("Insert ID: "))
                sm.remove_employee(deleteId)
            elif deleteChoice == 2:
                sm.remove_all_employee()
            else:
                if not sm.handle_invalid_choice():
                    break
                else:
                    continue
            if readChoice in [1, 2] and not sm.ask_repeat_again("delete"):
                break
            
    elif choice == 5:
        print("Exiting...")
        break
    else:
        if not sm.handle_invalid_choice():
            print("Exiting...")
            break