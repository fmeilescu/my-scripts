#! /usr/bin/env python3

import re
import os
import string

#from time import date, clock, sleep

print("Hello World !\n")

#d=date()
#t=clock()
#print("Today is ", d.month, "/", d.day, "/", d.year, " ", t.hour, ":", t.min, ":", t.sec)

x = 2 + 3 * 3
y = [1, 2, 3, 4, 3, 5]
print("Math-Algebra: x = 2 + 3 * 3")
print("Result: x =", x)

print("\nOperations with lists:")
L = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh"]
L0 = [L[0], L[1], L[2]]
L1 = [L[1], L[-1]]
L2 = [L[2], L[-2]]
print("Lists: L=", L)
print("Lists: L0=", L0)
print("Lists: L1=", L1)
print("Lists: L2=", L2)

if 3 in y:
    y.remove(3)
    print("Lists: y(1) (remove 3) =", y)
if 3 in y:
    y.remove(3)
    print("Lists: y(2) (remove 3) =", y)
if 3 in y:
    y.remove(3)
    print("Lists: y(3) (remove 3) =", y)

print("\nOperations with tuples:")
z = ('a', 'b', 'c', 'd', 'e', 'f', 'a', 'b', 'c', 'b')
print("Tuple z = ", z)
print("Tuple z has", len(z), "elements.")
print("".join(["Tuple z has ", "element '", str(z[0]), "' ", str(z.count(z[0])), " time(s)."]))
print("".join(["Tuple z has ", "element '", str(z[1]), "' ", str(z.count(z[1])), " time(s)."]))
print("".join(["Tuple z has ", "element '", str(z[2]), "' ", str(z.count(z[2])), " time(s)."]))
print("".join(["Tuple z has ", "element '", str(z[3]), "' ", str(z.count(z[3])), " time(s)."]))
print("".join(["Tuple z has ", "element '", str(z[4]), "' ", str(z.count(z[4])), " time(s)."]))
print("".join(["Tuple z has ", "element '",       'k', "' ", str(z.count('k')),  " time(s)."]))
print("Tuple z has", "element '",       'k', "'", str(z.count('k')),  "time(s).")

print("\nOperations with strings:")

s1 = " ".join(["join", "puts", "spaces", "between", "elements"])
print("Join string:", s1.split())
s2 = ".".join(["join", "puts", "dots", "between", "elements"])
print("Join string:", s2.split())

s3 = "You can\t\t can have tabs\t\t\n \t and newlines \n\n \ mixed \\ in"
print("Split string:", s3.split())
s4 = "Mississippi"
print("Split string:", s4.split("ss"), "\n")

s5 = "     Hello , \t Kitty \t\t !   "
print(" strip:", s5.strip())
s6 = "   Hello , \t Doggy \t\t !  .   "
print("lstrip:", s6.lstrip())
s7 = "         Hello , \t Pisi \t\t !                  "
print("rstrip:", s7.rstrip())

print("Find (ss):", s4.find("ss"))
print("Find (zz):", s4.find("zz"))
print("Count (ss):", s4.count("ss"))
print("Startswith (Miss):", s4.startswith("Miss"))
print("Endswith (w):", s4.endswith("w"))
print("Replace (ss -> +++):", s4.replace("ss", "+++"))

print("string.whitespaces:", string.whitespace, end="")
print("-------------------")

print("\nOperations with dictionaries:")
dic1 = {}
dic1[0] = 'Hi'
dic1[1] = 'Good morning'
dic1["two"] = 2
dic1["pi"] = 3.1415
dic1[10] = 'Hello'
dic1[11] = 2.345
dic1[12] = 'Bye'
print("dic1:", dic1)

english_to_french = {}
english_to_french['red'] = 'rouge'
english_to_french['blue'] = 'bleu'
english_to_french['green'] = 'vert'
print("English to French: red is", english_to_french['red'])

english_to_french = {'red': 'rouge', 'blue': 'bleu', 'green': 'vert'}
print("En-Fr Dictionary has", len(english_to_french), "words.")

matrix = [[3, 0, -2, 11], [0, 9, 0, 0], [0, 7, 0, 0], [0, 0, 0, -5]]
print("Matrix [4x4] line 1:", matrix[0])
print("Matrix [4x4] line 2:", matrix[1])
print("Matrix [4x4] line 3:", matrix[2])
print("Matrix [4x4] line 4:", matrix[3])
print("Matrix [4x4] element [2,2] is:", matrix[1][1])
print("Matrix [4x4] element [4,4] is:", matrix[3][3])

print("\nOperations with files:")
f = open("test_file_1.txt", "w")
f.write("First line with necessary newline character.\n")
f.write("Second line to write to the file.\n")
f.write("Third line to write to the file.\n")
f.close()

f = open("test_file_1.txt", "r")
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
f.close()

print(line1, line2, line3)

print("\nShow OS variables:")
print("\tCurrent directory: '", os.getcwd(), "'")
#print(sys.path)

print("\n=== if-elif-else statement  ===")
a = 10
b = 20
c = 30
n = 35

if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
elif a < 0:
    pass
else:
    print("a is equal to b")

print("\n=== while loop ===")
while a < b:
    print("a=", a, "; b=", b)
    b -= 1
else:
    print("'else block from while loop'")

print("\n=== for loop ===")
for c in range(0, n+1, 5):
    print("c=", c)
    c -= 1
else:
    pass

print("\nOperations with functions:")

def function_name_1(x, y=1, z=1):
    """ This is a simple sample function. """
    print("This is 'function_name_1(x, y, z)", "curret arguments:", x, y, z)
    return 0

print("\nExecuting 'function_name_1(x, y=1, z=1). Description:", function_name_1.__doc__)
result = function_name_1(10,20,30)
print("Result from function_name_1 is", result)

def maximum(*numbers):
    """ This function returns the max value of a string of real numbers."""
    if len(numbers) == 0:
        return None
    else:
        maxnum = numbers[0]
        for n in numbers[1:]:
            if n > maxnum:
                maxnum = n
    return maxnum

print("\nExecuting function 'maximum(5, -3, 2, 7, 15, 9)'. Description:", maximum.__doc__)
maxnum = maximum(5, -3, 2, 7, 15, 9)
print("max number is:", maxnum)

def f_with_global_var():
    """ This function used a global variable. """
    global a10
    a10 = 1
    b10 = 2
    print("a10 = %s, b10 = %s", a10, b10)
    return a

a10 = "one"
b10 = "two"
print("\nExecuting function 'f_with_global_var(a, b)'. Description:", f_with_global_var.__doc__)
a10 = f_with_global_var()
print("a10 = %s, b10 = %s", a10, b10)

print("\n-------------\n*** Bye ! ***")

# ----------------------------------- End of Script -----------------------------------
