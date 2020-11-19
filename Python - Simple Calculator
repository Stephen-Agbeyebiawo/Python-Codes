# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 19:54:03 2020

Last updated on Sat Oct 03 18:24:06 2020

@author: Stephen
"""

import math

def Adding(a,b):
	return a + b
def Subt(a,b):
	return a - b
def divi(a,b):
	return a/b
def mult(a,b):
	return a * b

operands = ['+','-','*','/', 'x']
QuitList = ['x','q','exit','quit']
Exp1 = ""
print("Enter your expression, separating operator and numbers by spaces. Log(), Log2() and In() as shown here:")
while True:
	Exp2 = input(">> ").strip().lower()

	if Exp2 in QuitList:
		break
	#Exp2 = Exp1.strip().lower()
	try:
		
		if Exp2[0:4] == "log(" and len(Exp2.replace("("," ").replace(")"," ").strip().split(" ")) < 3:
			parsedExp2 = Exp2.replace("("," ").replace(")"," ").strip().split(" ")
			try:
				Num1 = float(parsedExp2[1])
			except ValueError:
				print(parsedExp2[1] + " is not a number")
				continue
			Results1 = math.log10(Num1)
			print(Results1)
		elif Exp2[0:4] == "log2" and len(Exp2.replace("("," ").replace(")"," ").strip().split(" ")) < 3:
			parsedExp2 = Exp2.replace("("," ").replace(")"," ").strip().split(" ")
			try:
				Num1 = float(parsedExp2[1])
			except ValueError:
				print(parsedExp2[1] + " is not a number")
				continue
			Results1 = math.log2(Num1)
			print(Results1)
		elif Exp2[0:3] == "in(" and len(Exp2.replace("("," ").replace(")"," ").strip().split(" ")) < 3:
			parsedExp2 = Exp2.replace("("," ").replace(")"," ").strip().split(" ")
			try:
				Num1 = float(parsedExp2[1])
			except ValueError:
				print(parsedExp2[1] + " is not a number")
				continue
			Results1 = math.log(Num1)
			print(Results1)
		else:
			if " " not in Exp2:
				print("Make sure to separate numbers and operands with spaces")
			parsedExp = Exp2.split(" ")
			if len(parsedExp) == 3:
				Opr1 = parsedExp[1]
				
				if parsedExp[0][0:4] == "log(":
					parsedExp2 = parsedExp[0].replace("("," ").replace(")"," ").strip().split(" ")
					try:
						Part1 = float(parsedExp2[1])
					except ValueError:
						print(parsedExp2[1] + " is not a number")
						continue
					Num1 = math.log10(Part1)
					Num2 = float(parsedExp[2])
				elif parsedExp[0][0:4] == "log2":
					parsedExp2 = parsedExp[0].replace("("," ").replace(")"," ").strip().split(" ")
					try:
						Part1 = float(parsedExp2[1])
					except ValueError:
						print(parsedExp2[1] + " is not a number")
						continue
					Num1 = math.log2(Part1)
					Num2 = float(parsedExp[2])
				elif parsedExp[0][0:3] == "in(":
					parsedExp2 = parsedExp[0].replace("("," ").replace(")"," ").strip().split(" ")
					try:
						Part1 = float(parsedExp2[1])
					except ValueError:
						print(parsedExp2[1] + " is not a number")
						continue
					Num2 = float(parsedExp[2])
					Num1 = math.log(Part1)
				elif parsedExp[2][0:4] == "log(":
					parsedExp2 = parsedExp[2].replace("("," ").replace(")"," ").strip().split(" ")
					try:
						Part2 = float(parsedExp2[1])
					except ValueError:
						print(parsedExp2[1] + " is not a number")
						continue
					Num2 = math.log10(Part2)
					Num1 = float(parsedExp[0])
				elif parsedExp[2][0:4] == "log2":
					parsedExp2 = parsedExp[2].replace("("," ").replace(")"," ").strip().split(" ")
					try:
						Part2 = float(parsedExp2[1])
					except ValueError:
						print(parsedExp2[1] + " is not a number")
						continue
					Num2 = math.log2(Part2)
					Num1 = float(parsedExp[0])
				elif parsedExp[2][0:3] == "in(":
					parsedExp2 = parsedExp[2].replace("("," ").replace(")"," ").strip().split(" ")
					try:
						Part2 = float(parsedExp2[1])
					except ValueError:
						print(parsedExp2[1] + " is not a number")
						continue
					Num2 = math.log(Part2)
					Num1 = float(parsedExp[0])
				else:
					try:
						Num1 = float(parsedExp[0])
						Num2 = float(parsedExp[2])
					except ValueError:
						print("Operation must be done on numbers")
						continue
				
				if Opr1 not in operands:
					print(Opr1 + " is not a recognized operand. Use +, -, / or x")
				else:
					if Opr1 == "+":
						Results1 = Adding(Num1,Num2)
						print(Results1)
					elif Opr1 == "-":
						Results1 = Subt(Num1,Num2)
						print(Results1)
					elif Opr1 == "*" or Opr1 == "x":
						Results1 = mult(Num1,Num2)
						print(Results1)
					elif Opr1 == "/":
						Results1 = divi(Num1,Num2)
						print(Results1)
			
			if len(parsedExp) == 5:
				try:
					Num1 = float(parsedExp[0])
					Opr1 = parsedExp[1]
					Num2 = float(parsedExp[2])
					Opr2 = parsedExp[3]
					Num3 = float(parsedExp[4])
				except ValueError:
					print("Operation must be done on numbers")
					continue
				
				if Opr1 not in operands and Opr2 not in operands:
					print(Opr1 + " and " + Opr2 + " are not a recognized operands. Use +, -, / or x")
				elif Opr1 not in operands:
					print(Opr1 + " is not a recognized operand. Use +, -, / or x")
				elif Opr2 not in operands:
					print(Opr2 + " is not a recognized operand. Use +, -, / or x")
				else:
					if Opr1 == "*" or Opr1 == "/":
						if Opr1 == "*" or Opr1 == "x":
							Results1 = mult(Num1,Num2)
							#print(Results1)
						else:
							#Opr1 == "/":
							Results1 = divi(Num1,Num2)
							#print(Results1)
							
						
						if Opr2 == "+":
							Results2 = Adding(Results1,Num3)
							print(Results2)
						elif Opr2 == "-":
							Results2 = Subt(Results1,Num2)
							print(Results2)
						elif Opr2 == "*" or Opr1 == "x":
							Results2 = mult(Results1,Num2)
							print(Results2)
						elif Opr2 == "/":
							Results2 = divi(Results1,Num2)
							print(Results2)
					else:
						if Opr1 == "+":
							Results1 = Adding(Num1,Num2)
							#print(Results1)
						elif Opr1 == "-":
							Results1 = Subt(Num1,Num2)
							#print(Results1)
						elif Opr1 == "*" or Opr1 == "x":
							Results1 = mult(Num1,Num2)
							#print(Results1)
						elif Opr1 == "/":
							Results1 = divi(Num1,Num2)
							#print(Results1)
							
						if Opr2 == "+":
							Results2 = Adding(Results1,Num3)
							print(Results2)
						elif Opr2 == "-":
							Results2 = Subt(Results1,Num2)
							print(Results2)
						elif Opr2 == "*" or Opr1 == "x":
							Results2 = mult(Results1,Num2)
							print(Results2)
						elif Opr2 == "/":
							Results2 = divi(Results1,Num2)
							print(Results2)
	except ValueError:
		print(Exp1 + " can't be computed. Input numbers and operands separated by spaces. e.g: 3 + 4, 5 - 2 x 4.")
	except ZeroDivisionError:
		print("Can't divide by Zero.")
	except:
		print("Error. Enter your expression, separating operator and numbers by spaces. Log(), Log2() and In() as shown here:")
