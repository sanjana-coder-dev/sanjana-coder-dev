class Employee:
    def __init__(self,emp_id,name,salary):
        self.emp_id=emp_id
        self.name=name
        self.salary=salary
    def dispaly(self):
            print("\n----Employee Details----")
            print("Employee Id:",self.emp_id)
            print("Name:",self.name)
            print("salary:",self.salary)
    def update_salary(self,new_salary):
            self.salry=new_salary
            print("Salary updated successfully!")
emp_id =input("Enter Employee ID:") 
name =input("Enter Employee Name:")
salary =float(input("Enter Employee Salary:"))
emp=Employee(emp_id,name,salary)    
   emp.display()
   new_salary=float(input("\nEnter Salary: "))
   emp.update_salary(new_salary)
   emp.display()
        