run_app = True
while(run_app):
    first_num = input("Enter first number: ")
    second_num = input("Enter second number: ")
    operation = input("Enter Operation to perform (*, /, -, +): ")

    if operation == "+":
        print(float(first_num) + float(second_num))
    elif operation == "-":
        print(float(second_num) - float(first_num))

    cont = input("Do you want to continue (y/n): ")
    run_app = True if cont.lower() == 'y' else False