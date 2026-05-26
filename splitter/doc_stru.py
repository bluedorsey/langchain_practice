# what if doc is written in diffrent formate like md files or code 

from langchain_text_splitters import RecursiveCharacterTextSplitter,Language


markdown = '''

A simple Python-based project to manage and track student data,

Project Name: Smart Student Tracker

## @. Features

- Add new students with relevant info
- View student details
- Check if a student is passing
- Easily extendable class-based design

## X Tech Stack

- Python 3.10+
- No external dependencies
'''

code = '''
class Student:
def _init_(self, name, age, grade):
self.name = name
self.age = age
self.grade = grade # Grade is a float (Like 8.5 or 9.2)

def get_details(self):
return f"Name: { self.name}, Age: {self.age}, Grade: {self.grade}"

def is_passing(self):
return self.grade >= 6.0

# Example usage
student1 = Student("Aarav", 20, 8.2)
print(student1.get_details())

if student1.is_passing():
print("The student is passing.")
else:
print ('student not passed')
'''

spliter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size = 300,
    chunk_overlap = 0,
    
)

spliter1 = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,
    chunk_size = 150,
    chunk_overlap = 0,
    )


result = spliter.split_text(code)
result2  = spliter1.split_text(markdown)
print(result)
print('*'*80)
print(result2)