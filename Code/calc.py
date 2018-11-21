import sys
import re


def add(a,b):
    return a+b

def checkNum(inputString):
    return any(char.isdigit() for char in inputString)

print (checkNum("Jamie"))