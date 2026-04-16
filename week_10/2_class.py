class Student:
    def __init__(self, first_name, last_name, gpa):
        self.first_name = first_name
        self.last_name = last_name
        self.gpa = gpa

    def get_gpa(self):
        return self.gpa

    def get_last(self):
        return self.last_name


class Roster:
    def __init__(self):
        self.roster = []

    def add_student(self, student):
        self.roster.append(student)

    def course_size(self):
        return len(self.roster)

    def get_roster(self):
        return self.roster

    def get_dean_list(self):
        dean_list = [
            student.get_last() for student in self.roster if student.get_gpa() >= 3.5
        ]
        return dean_list


s1 = Student("Elon", "Musk", 3.5)
s2 = Student("Bill", "Gate", 3.9)
roster = Roster()
roster.add_student(s1)
roster.add_student(s2)


print(s1.get_gpa())
print(s2.get_gpa())
print(roster.get_roster())
print(roster.course_size())
print(roster.get_dean_list())
