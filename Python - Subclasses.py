# -*- coding: utf-8 -*-
"""
Created on Thr Nov  19 14:54:56 2020

@author: Jerry Tetteh
"""

#class definition ----------------------------------------
class employee:
    def __init__(self, FirstName, LastName, TelNumber, RoomNumber):
        self.FirstName = FirstName
        self.LastName = LastName
        self.TelNumber = TelNumber
        self.RoomNumber = RoomNumber
        
    def DirString(self,a):
        print(a)

#create subclass
class HourlyEmployee(employee):
    def __init__(self, FirstName, LastName, TelNumber, RoomNumber, HourlyRate=12):
        super().__init__(FirstName, LastName, TelNumber, RoomNumber)
        self.HourlyRate = HourlyRate

    def set_HoursWorked(self, HoursWorked):
        self.HoursWorked = HoursWorked

class SalariedEmployee(employee):
    def __init__(self, FirstName, LastName, TelNumber, RoomNumber):
        super().__init__(FirstName, LastName, TelNumber, RoomNumber)
        
    def set_MonthlySalary(self, MonthlySalary):
        self.MonthlySalary = MonthlySalary

#prompt user to create database --------------------------
employeeList = []
#subList = []

try:
    try:
        salariedEmpCount = int(input("How many salaried employees do you want to add? \n>> "))
    except:
        salariedEmpCount = 0
    try:
        hourlyEmpCount = int(input(">> How many hourly employee do you want to add? \n>> "))
    except:
        hourlyEmpCount = 0
    print("\n")
    #create salaried employees
    count = 0
    if hourlyEmpCount != 0:
        while count < hourlyEmpCount:
            print("Enter details of hourly employee ",count + 1)
            firstname = input("Enter Employee First Name: ")
            lastname = input("Enter Employee Last Name: ")
            telnumber = input("Enter Employee Telephone Number: ")
            roomnumber = input("Enter Employee Room Number: ")
            try:
                hourlyrate = float(input("What is the hourly rate? "))
            except:
                hourlyrate = 12
            print("\n")
            #build the list
            Employee = HourlyEmployee(firstname, lastname, telnumber, roomnumber, hourlyrate)
            employeeList.append(Employee)
            count += 1
    else:
        print("\n[INFORMATION]----No hourly employee added----\n")
    #create hourly employes
    count = 0
    if salariedEmpCount is not 0:
        while count < salariedEmpCount:
            print("Enter details of salaried employee ",count + 1)
            firstname = input("Enter Employee First Name: ")
            lastname = input("Enter Employee Last Name: ")
            telnumber = input("Enter Employee Telephone Number: ")
            roomnumber = input("Enter Employee Room Number: ")
            salary = None
            while salary is None:
                try:
                    salary = float(input("Enter the salary: "))
                except:
                    print("Enter a number")
            print("\n")
            #build the list
            Employee = SalariedEmployee(firstname, lastname, telnumber, roomnumber)
            Employee.set_MonthlySalary(salary)
            employeeList.append(Employee)
            count += 1
    else:
        print("[INFORMATION]---No salaried employees added---\n")
except:
    pass

if salariedEmpCount == 0 and hourlyEmpCount == 0:
    print("[INFORMATION]------No employee list to display------")
else:
    print("\n")
    #print list of employees and show menu
    for i in range(len(employeeList)):
        print(i + 1, ". ", employeeList[i].FirstName, " ", employeeList[i].LastName, " ", employeeList[i].TelNumber, " ", employeeList[i].RoomNumber)
    print("\n ---------Menu---------")
    print("1. Show list of employees")
    print("2. Enter hours worked for a single employee")
    print("3. Print a list of pending payments")
    print("Type \"exit\" to exit program\n")
    while True:
        selection = input(">> Select an option: ")
        if selection == "exit":
            break
        else:
            if selection == "1":
                for i in range(len(employeeList)):
                    print(i + 1, ". ", employeeList[i].FirstName, " ", employeeList[i].LastName, " ", employeeList[i].TelNumber, " ", employeeList[i].RoomNumber)
            elif selection == "2":
                for i in range(len(employeeList)):
                    print(i + 1, ". ", employeeList[i].FirstName, " ", employeeList[i].LastName, " ", employeeList[i].TelNumber, " ", employeeList[i].RoomNumber)
                print("\n>> Select employee to enter hours worked...1 to ",len(employeeList)+1,"\n")
                choice = int(input()) - 1
                if isinstance(employeeList[choice], SalariedEmployee) == True:
                    print("[ERROR]----Can not set hours worked for Salaried Employee")
                else:
                    hWorked = int(input(">> Enter hours worked: "))
                    employeeList[choice].set_HoursWorked(hWorked)
            elif selection == "3":
                pendingPayments = 0
                for i in range(len(employeeList)):
                    #test if employee is an hourly employee
                    try:
                        if isinstance(employeeList[i], HourlyEmployee) is True and employeeList[i].HoursWorked > 0:
                            try:
                                print("Pending payment for ",employeeList[i].FirstName," ",employeeList[i].LastName," is ",employeeList[i].HoursWorked * employeeList[i].HourlyRate)
                                pendingPayments += 1
                            except:
                                pass
                        else:
                            pass
                    except AttributeError:
                        print("Hour worked has not yet been set for ",employeeList[i].FirstName," ",employeeList[i].LastName,". Select OPTION 2 to set it")
                if pendingPayments == 0:
                    print("There are no pending payments")
                else:
                    pass
