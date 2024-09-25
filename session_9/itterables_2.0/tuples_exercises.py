# 1.1 Unpacking a Tuple
# You are given a tuple with three values (name, age, and city).
# Unpack the values into separate variables and print them.
def function_task_1_1():
    person = ("Alice", 25, "New York", "Dan", 34, "Loosdrecht")
    name=person[0]
    age=person[1]
    city=person[2]
    # name, age, city=person
    print(f"Name: {name}, age: {age}, city: {city}")
    print(f"Name: {person[0]}, age: {person[1]}, city: {person[2]}")
    print(f"Name: {person[3]}, age: {person[4]}, city: {person[5]}")

# 1.3. Return Multiple Values from a Function
# Write a function that takes two numbers as input and returns both their sum and product as a tuple.
def function_task1_3(param1_int, param2_int):
    sum = param1_int + param2_int
    prod = param1_int * param2_int
    return (sum, prod)

# result = function_task1_3(12, 10)
# print(type(function_task1_3(12, 10)))
# print(f"Sum: {result[0]}")

# 1.5. Tuple of Tuples
# You are given a tuple of tuples, where each inner tuple contains the name of a student and their grade.
# Write code to extract and print all student names along with their grades.
def function_task_1_5():
    students = (("Alex", 7), ("Maria", 8), ("Ciprian", 10))
    for student in students:
        # name=student[0]
        # grade=student[1]
        name, grade = student
        print(f"Studentul {name} a luat nota {grade}")

function_task_1_5()