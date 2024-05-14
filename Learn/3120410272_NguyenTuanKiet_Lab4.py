import mysql.connector
import datetime


def connect_mysql():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
    )
    return connection


def create_database(database_name):
    connection = connect_mysql()
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS " + database_name)
    cursor.execute("USE " + database_name)
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS Employee (employeeid varchar(10) primary key, fullname varchar(100), birthday date, phone varchar(20))")
    return connection


def insert_employee(connection, employeeid, fullname, birthday, phone):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Employee (employeeid, fullname, birthday, phone) VALUES (%s, %s, %s, %s)",
                   (employeeid, fullname, birthday, phone))
    connection.commit()
    cursor.close()


def delete_employee(connection, employeeid):
    cursor = connection.cursor()
    count = cursor.execute(
        "DELETE FROM Employee WHERE employeeid = %s", (employeeid,))
    connection.commit()
    cursor.close()
    if count > 0:
        print("Successfully deleted employee with id: " + employeeid)
    else:
        print("Employee with id: " + employeeid + " not found")


def show_employees(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Employee")
    employees = cursor.fetchall()
    print("=============Employee table=============")
    print("Employee ID\tFull Name\tBirthday\tPhone")
    print("--------------------------------------------------------------")
    for employee in employees:
        employee_id, full_name, birthday, phone = employee
        print(f"{employee_id}\t\t{full_name}\t\t{birthday}\t{phone}")
    cursor.close()

def update_employee(connection, employee_id, full_name, birthday, phone):
    cursor = connection.cursor()
    cursor.execute("UPDATE Employee SET fullname = %s, birthday = %s, phone = %s WHERE employeeid = %s",
                   (full_name, birthday, phone, employee_id))
    connection.commit()
    cursor.close()

def edit_employee(connection):
    while (True):
        employee_id = input("Enter employee ID: ")
        full_name = input("Enter full name: ")
        birthday = input("Enter birthday (yyyy-mm-dd): ")
        phone = input("Enter phone: ")
        update_employee(connection, employee_id, full_name, birthday, phone)
        print("Employee updated successfully")
        show_employees(connection)
        choice = input("Do you want to continue? (y/n): ")
        if choice.lower() == 'n':
            break

def input_employee(connection):
    while (True):
        employee_id = input("Enter employee ID: ")
        full_name = input("Enter full name: ")
        birthday = input("Enter birthday (yyyy-mm-dd): ")
        phone = input("Enter phone: ")
        insert_employee(connection, employee_id, full_name, birthday, phone)
        print("Employee inserted successfully")
        show_employees(connection)
        choice = input("Do you want to continue? (y/n): ")
        if choice.lower() == 'n':
            break


def find_employee(connection, employee_name):
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM Employee WHERE fullname = %s", (employee_name,))
    print("============================Result============================")
    print("Employee ID\tFull Name\tBirthday\tPhone")
    print("--------------------------------------------------------------")
    employees = cursor.fetchall()
    for employee in employees:
        employee_id, full_name, birthday, phone = employee
        print(f"{employee_id}\t\t{full_name}\t\t{birthday}\t{phone}")
    cursor.close()
    return employee


if __name__ == "_main_":
    connection = create_database("EmployeeDB")
    while (True):
        print("1. Insert employee")
        print("2. Delete employee")
        print("3. Show employees")
        print("4. Update employee")
        print("5. Find employee")
        print("0. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            input_employee(connection)
        elif choice == '2':
            employee_id = input("Enter employee ID: ")
            delete_employee(connection, employee_id)
        elif choice == '3':
            show_employees(connection)
        elif choice == '4':
            edit_employee(connection)
        elif choice == '5':
            employee_name = input("Enter employee name: ")
            find_employee(connection, employee_name)
        elif choice == '0':
            break
        else:
            print("Invalid choice")