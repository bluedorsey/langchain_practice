from pydantic import BaseModel, EmailStr , Field
from typing import Optional

#better validation for the variable
class Student (BaseModel):
    Name : str
    age : Optional[int] = None #can pass 32 as a str it explicitly does the data conversion (pydantic)
    email : Optional[EmailStr]= None#build in email validation 
    cgpa : Optional[float]=Field(gt=0,lt=10,description='the given decimal value is cgpa of the student', default=6.00)

New_student = {'Name':'Ashutosh Sahu','email':'sahuashutosh563@gmail.com','cgpa':'7.44'}
student = Student(**New_student)
print(student.model_dump_json())
print(dict(student))