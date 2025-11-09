# new_dict = {new_key: new_value for (key, value) in dict.items()}
# DICTIONARY Comprehension

#Create new dictionary students_score but by comprehension method
import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores = {student: random.randint(30, 100) for student in names}
print(students_scores)

#Create new dictionary passed_students for those who passed >= 60
passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)

print("\n")
#TODO: How to Iterate over a Pandas DataFrame

#Loop through dictionaries
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
for (key, value) in student_dict.items():
    print(value)

print("\n")
import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#Loop through a data frame
for(key, value) in student_data_frame.items():
    print(value)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)
