def male_female_count(student_list):
    male_count = 0
    female_count = 0
    for student in student_list:
        if student.lower() == 'male':
            male_count += 1
        elif student.lower() == 'female':
            female_count += 1
    answer = [("Male", male_count), ("Female", female_count)]
    return answer


student = ["Male", "Female", "male", "male", "female", "Male"]
check_list = male_female_count(student)
print(check_list)
