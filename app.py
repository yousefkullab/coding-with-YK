
import random

# Course Class
class course:
    def __init__(self, course_id, course_name, course_class):
        self.course_id = course_id
        self.course_name = course_name
        self.course_class = course_class
        
        

# Student Class
class student:
    def __init__(self, student_name, student_id, student_class):
        self.student_name = student_name
        self.student_class = student_class
        self.student_id = student_id
        self.student_course = ["Java", "C Programming"]
                
    @classmethod
    def Add_course(Cls, new_student, new_course):
         
        student_num = int(input("Enter The Student Number: "))
        if student_num == new_student.student_id:
            if new_course not in new_student.student_course:
                new_student.student_course.append(new_course)
            else:
                print("Course Is Exist")
        else:
            print("User Not Exist")
            
    @classmethod
    def all_student(Cls, student_list):
         print ("All Student")
         for s in student_list:
            print(f"{s.student_name} {s.student_class} {s.student_course}")
            

# Drive Code 

def main():
    
    print("""Select Choice Please
          1.Add New Student
          2.Remove Student
          3.Edit Student
          4.Display All Students
          5.Create New Student
          6.Add course to student
          0.Exit""")
    
    my_select = int(input("Enter You Select: "))
    
    
    # Add New Student
    if my_select == 1:
        name = input("Enter Student Name: ").capitalize()
        id = random.randint(1, 1000)  
        student_class = input("Enter Student Class(A, B, C): ").upper()
        while student_class not in ["A", "B", "C"]  :
                 student_class = input("Please Enter Class Student Again(A, B, C): ").upper()
           
        new_student = student(name, id, student_class)
        print(new_student.student_name)
        print(new_student.student_id)
        print(new_student.student_class)
        print("Student Add Successfully")
    
    # Remove Student 
    elif my_select == 2:
        new_student= student("Yousef", 10, "A")
        user_id = int(input("Enter Student Id: ")) # Enter user_id = 10 
        if user_id == new_student.student_id:
            # You Can Delete Student When Store It In Data Structure Or Table in Data Base
            print("Delete Done Successfully")
        else:
            print("User Not Exist")
    
    # Edit Student 
    elif my_select == 3:
        new_student= student("Yousef", 10, "A")
        user_id = int(input("Enter Student Id: ")) # Enter user_id = 10 
        if user_id == new_student.student_id:
            new_name = input("Enter New Name: ").capitalize()
            new_student.student_name= new_name
            new_class = input("Enter New Class(A, B, C): ").upper()
            while new_class not in ["A", "B", "C"]  :
                 new_class = input("Please Enter Class Student Again(A, B, C): ").upper()
            new_student.student_class = new_class
            
            print(f"New Student Name: {new_student.student_name}")
            print(f"New Student Class: {new_student.student_class}")
            
        else:
            print("User Not Exist")
        
    # Display All Student Method 
    elif my_select == 4:
         student_list= []
         student_list.append(student("Yousef", 1, "A"))
         student_list.append(student("Ahemd", 3, "B"))
         student_list.append(student("Ali", 4, "C"))
         
         student.all_student(student_list)
        
        
            
    # Create New User 
    elif my_select == 5:
        name = input("Enter Student Name: ").capitalize()
        id = random.randint(1, 1000)  
        student_course = "".capitalize()
        student_class = input("Enter Student Class(A, B, C): ").upper()
        while student_class not in ["A", "B", "C"]  :
                 student_class = input("Please Enter Class Student Again(A, B, C): ").upper()
           
        new_student = student(name, id, student_class)
        print(new_student.student_name)
        print(new_student.student_id)
        print(new_student.student_class)
        print("Student Created Successfully")
        
    
    # Add Course To Student 
    elif my_select == 6:
       new_student= student("Yousef", 10,"A")
       new_course = input("Enter Course Name: ").capitalize()
       student.Add_course(new_student, new_course)
       
       print(new_student.student_course)
        
    # Close Program
    elif my_select == 0:
        print("Program closed")
        exit()
        
        
main()


# Software Engineer Joseph .