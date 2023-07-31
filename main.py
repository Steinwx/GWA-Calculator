def read_students_from_file(filename):
    students = []
    with open(filename, 'r') as file:
        for line in file:
            name, gwa = line.strip().rsplit(' ', 1)
            students.append((name, float(gwa)))
    return students

def get_student_with_highest_gwa(students):
    if not students:
        return None

    max_gwa_student = students[0]
    for student in students:
        if student[1] > max_gwa_student[1]:
            max_gwa_student = student
    return max_gwa_student

def main():
    input_file = "students.txt"

    students = read_students_from_file(input_file)
    highest_gwa_student = get_student_with_highest_gwa(students)

    if highest_gwa_student:
        print(f"Student with highest GWA: {highest_gwa_student[0]} - GWA: {highest_gwa_student[1]}")
    else:
        print("No students found.")

if __name__ == "__main__":
    main()
