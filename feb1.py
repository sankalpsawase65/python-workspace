 # Input
name1 = input("Enter name 1: ")
roll1 = eval(input("Enter roll number 1: "))
marks1 = eval(input("Enter marks 1: "))

name2 = input("Enter name 2: ")
roll2 = eval(input("Enter roll number 2: "))
marks2 = eval(input("Enter marks 2: "))

name3 = input("Enter name 3: ")
roll3 = eval(input("Enter roll number 3: "))
marks3 = eval(input("Enter marks 3: "))

# Finding sorted order of marks
low = min(marks1, marks2, marks3)
high = max(marks1, marks2, marks3)
mid = marks1 + marks2 + marks3 - low - high

# Printing table
print("{:<15}{:<15}{:<10}".format("Name", "Roll No", "Marks"))
print("-" * 40)
print("{:<15}{:<15}{:<10}".format(name1, roll1, marks1))
print("{:<15}{:<15}{:<10}".format(name2, roll2, marks2))
print("{:<15}{:<15}{:<10}".format(name3, roll3, marks3))

