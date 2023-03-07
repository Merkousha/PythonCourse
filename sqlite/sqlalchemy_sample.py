from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# create the database engine and session
engine = create_engine('db_sample')
Session = sessionmaker(bind=engine)
session = Session()

# create the base class for our table definitions
Base = declarative_base()

# define our student table class
class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    grade = Column(float)
    name = Column(String)

# create the table if it doesn't exist
Base.metadata.create_all(engine)

# create a new student
def create_student(name, grade):
    student = Student(name=name, grade=grade)
    session.add(student)
    session.commit()

# retrieve a student by id
def read_student(id):
    student = session.query(Student).filter_by(id=id).first()
    return student

# update a student's name or grade
def update_student(id, name=None, grade=None):
    student = read_student(id)
    if name:
        student.name = name
    if grade:
        student.grade = grade
    session.commit()

# delete a student
def delete_student(id):
    student = read_student(id)
    session.delete(student)
    session.commit()



# create a new student
create_student(name='Alice', grade=16)

# retrieve a student by id
student = read_student(id=1)
print(student.name, student.grade)

# update a student's name and/or grade
update_student(id=1, name='Bob')
update_student(id=1, grade=15.7)

# delete a student
delete_student(id=1)