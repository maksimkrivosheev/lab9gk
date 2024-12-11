# def create_report(name, age, department, salary, bonus, performance_score):
#     print(f"Name: {name}")
#     print(f"Age: {age}")
#     print(f"Department: {department}")
#     print(f"Salary: {salary}")
#     print(f"Bonus: {bonus}")
#     print(f"Performance Score: {performance_score}")


def create_report(employee_data):
    for key, value in employee_data.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
