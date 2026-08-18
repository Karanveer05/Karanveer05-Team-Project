# Exercise 1 – Student Class
# Create a class named Student.
# Attributes

# Name
# Age
# Course
# Method
# display()Print all student details.
# Create 2 student objects and display their information.
class Student :
    def __init__(self,Name,Age,Course):
        self.Name=Name
        self.Age=Age
        self.Course=Course
    def display(self):
        print(f"Student Details \nName : {self.Name}\nAGE : {self.Age}\nCourse is {self.Course}")    
        print("-"*25)
    pass
student1 = Student("Karanveer Singh", 21, "Computer Science")
student2 = Student("Amrit Pal", 22, "Data Science")


    
student1.display()
student2.display() 
   

