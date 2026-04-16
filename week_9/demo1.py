student_data = {

    "std_1": {

        "name": "Alice",

        "grades": {"Math": 85, "Science": 90, "History": 78}

    },

    "std_2": {

        "name": "Bob",

        "grades": {"Math": 70, "Art": 95}

    },

    "std_3": {

        "name": "Charlie",

        "grades": {"Science": 88, "History": 92}

    }

}

def total_students(data):

    return len(data)

 

def average_grades(data):
    for student_name, info in data.items():
        print(student_name)
        student_grades = info["grades"]
        all_grades = student_grades.values()
        return sum(all_grades) / len(all_grades)
        break

    

def top_student(data):

    pass

    

def course_counts(data):

    pass

 

def top_per_course(data):

    pass

 

def above_85_all(data):

    pass

print(total_students(student_data))

average_grades(student_data)
