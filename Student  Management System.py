subject1=input("Enter first subject: ")
subject2=input("Enter second subject: ")
subject3=input("Enter third subject: ")
subjects=(subject1,subject2,subject3)
name=input("Enter student name: ")
age=int(input("Enter student age: "))
marks1=int(input(f"Enter {subject1} marks: "))
marks2=int(input(f"Enter {subject2} marks: "))
marks3=int(input(f"Enter {subject3} marks: "))
student={
    "name":name,
    "age":age,
    "subjects":subjects,
    "marks":{
        subject1:marks1,
        subject2:marks2,
        subject3:marks3
    }
}
print("\nStudent details")
print(student)
