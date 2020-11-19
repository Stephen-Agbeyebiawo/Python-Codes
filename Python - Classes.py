# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 14:54:56 2020

@author: Stephen Agbeyebiawo
"""


class employee(object):
    def __init__(self, FirstName, LastName, TelNumber, RoomNumber):
        self.FirstName = FirstName
        self.LastName = LastName
        self.TelNumber = TelNumber
        self.RoomNumber = RoomNumber
        
    def DirString(self,a):
        print(a)

employeeList = []
subList = []
count = 0
employeecount = int(input("How many employee enteries do you want to create? "))
while count < employeecount:
    print("Select 1 to enter new employee data manually or 2 to specify file name to load data from file:")
    choice = input(">> ")
    if choice == "1":
        firstname = input("Enter Employee First Name: ")
        lastname = input("Enter Employee Last Name: ")
        telnumber = input("Enter Employee Telephone Number: ")
        roomnumber = input("Enter Employee Room Number: ")
    elif choice == "2":
        filename = input("Enter name of the file: ")
        with open(filename) as fn:
            content = fn.readlines()
        content = [x.strip() for x in content]
        for i in content:
            firstname = content[0]
            lastname = content[1]
            telnumber = content[2]
            roomnumber = content[3]
    else:
        print("Enter 1 or 2")

    Employee = employee(firstname,lastname,telnumber,roomnumber)
    subList = [Employee.FirstName,Employee.LastName,Employee.TelNumber,Employee.RoomNumber]

    employeeList.append(subList)
        
    count = count + 1

Employee.DirString(employeeList)       
