from typing import TypedDict
class Person(TypedDict):
    name:str
    age:int

newperson : Person = {'name':'ashutosh','age':20}
print(newperson)