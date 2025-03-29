from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Auth User model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)

# Students table
class Student(Base):
    __tablename__ = "students"
    student_id = Column(String, primary_key=True, unique=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    enrollment_date = Column(Date, nullable=False)

# Courses table
class Course(Base):
    __tablename__ = "courses"
    course_id = Column(String, primary_key=True, unique=True)
    course_name = Column(String, nullable=False)
    instructor = Column(String, nullable=False)
    credits = Column(Integer, nullable=False)

# Student Course Attendance table
class StudentCourseAttendance(Base):
    __tablename__ = "student_course_attendance"
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(String, ForeignKey("students.student_id"), nullable=False)
    course_id = Column(String, ForeignKey("courses.course_id"), nullable=False)
    attendance_date = Column(Date, nullable=False)
    status = Column(String, nullable=False)  # Present, Absent, Late

    # Relationships (Optional, for easier querying)
    student = relationship("Student", backref="attendances")
    course = relationship("Course", backref="attendances")

# Create tables in the database
Base.metadata.create_all(bind=engine)
