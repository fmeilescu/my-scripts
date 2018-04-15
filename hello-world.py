#! /usr/bin/env python3

import re
import os

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
print("Tuple z has", "element '", z[0], "'", z.count(z[0]), "time(s).")
print("Tuple z has", "element '", z[1], "'", z.count(z[1]), "time(s).")
print("Tuple z has", "element '", z[2], "'", z.count(z[2]), "time(s).")
print("Tuple z has", "element '", z[3], "'", z.count(z[3]), "time(s).")
print("Tuple z has", "element '", z[4], "'", z.count(z[4]), "time(s).")
print("Tuple z has", "element '",  'k', "'", z.count('k'),  "time(s).")

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

print("\n=== IF  ===")
a = 10
b = 20
c = 30
n = 35

if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")

print("\n=== while loop ===")
while a < b:
    print("a=", a, "; b=", b)
    b -= 1

print("\n=== for loop ===")

for c in range(0, n+1, 5):
    print("c=", c)
    c -= 1

print("\nBye !")


# --------- End of Script ----------
