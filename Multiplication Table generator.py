print("=== Multiplication Table Generator ===")
while True:
    number=int(input("Enter a number:"))
    print(f"\nMultiplication Table of {number}")
    for i in range(1,11):
        print(f"{number}X{i}={number*i}")
        choice=input("\nDo you want another table? (yes/no):").lower()
        if choice!="yes":
            print("Thank you for using the Multiplication Table generator!")
            break