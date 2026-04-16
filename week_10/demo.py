# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

#     def __str__(self):
#         return f"rectangle: {self.width} - {self.height}"

#     def areaDifference(self, rect):
#         diff = abs(self.area() - rect.area() )
#         return diff


# r1 = Rectangle(4,3)
# r2 = Rectangle(2,1)

# # assert r1.area() == 11, "something is wrong"
# # assert r2.area()  == 2

# print(r1.area(), r2.area())
# print(r1)
# print(r1.areaDifference(r2))

# class Course:
#     college = "Cal Poly Pomona"
#     def __init__(self, course_name="Unknown"):
#         course_number = "CS 2520"
#         self.course_name = course_name

# c = Course()
# print(c.college)
# print(c.course_name)
# print(c.course_number)


class A:
    pass


class B(A):
    pass


print(isinstance(B(), A))
