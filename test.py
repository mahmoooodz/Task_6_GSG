import json

import requests


def create_student():
    while True:
        student_name = input("Enter Student Name: ")
        if student_name.strip() != "":
            break
    while True:
        age = int(input("Enter Student Age: "))
        if age > 0:
            break

    while True:
        mobile_number = input("Enter Student Mobile Number: ")
        if mobile_number.strip() != "":
            break

    while True:
        level = input("Select Student Level (A-B-C): ")
        if level.strip() in ("A", "B", "C", "a", "b", "c"):
            break
    data = {
        "full_name": student_name,
        "age": age,
        "mobile_number": mobile_number,
        "level": level
    }
    result = requests.post(url="http://staging.bldt.ca/api/method/build_it.test.register_student",
                           data=data)
    result = json.loads(result.text)
    if result['code'] == 200:
        print("Student Created Successfully")
    else:
        print("Failed to create new Student")


def edit_student():
    while True:
        m_id = input("Enter Student ID: ")
        if m_id.strip() != "":
            break

    while True:
        student_name = input("Enter Student Name: ")
        if student_name.strip() != "":
            break
    while True:
        age = int(input("Enter Student Age: "))
        if age > 0:
            break

    while True:
        mobile_number = input("Enter Student Mobile Number: ")
        if mobile_number.strip() != "":
            break

    while True:
        level = input("Select Student Level (A-B-C): ")
        if level.strip() in ("A", "B", "C", "a", "b", "c"):
            break
    data = {
        "id" : m_id,
        "full_name": student_name,
        "age": age,
        "mobile_number": mobile_number,
        "level": level
    }
    result = requests.post(url="http://staging.bldt.ca/api/method/build_it.test.edit_student",
                           data=data)
    result = json.loads(result.text)
    print(result)
    if result['code'] == 200:
        print("Student Updated Successfully")
    else:
        print("Failed to edit new student")


def delete_student():
    while True:
        m_id = input("Enter Student ID: ")
        if m_id.strip() != "":
            break

    data = {
        "id": m_id,
    }
    result = requests.post(url="http://staging.bldt.ca/api/method/build_it.test.delete_student",
                           data=data)
    result = json.loads(result.text)
    print(result)
    if result['code'] == 200:
        print("Student Deleted Successfully")
    else:
        print("Failed to delete student")


def export_students_to_file():
    result = requests.get(url="http://staging.bldt.ca/api/method/build_it.test.get_students")
    result = json.loads(result.text)
    if result.get('code') != 200:
        print("Error Occurred")
        return
    my_file = open("Students.txt","w")
    students = result.get('data')
    for student in students:
        student_details = str(student.get('id')) + " -- "\
        + str(student.get('full_name')) + " -- "\
        + str(student.get('mobile_number')) + " -- "\
        + str(student.get('age')) + " -- "\
        + str(student.get('level')) + "\n"
        my_file.write(student_details)
    my_file.close()
    print("Students Data Exported Successfully")


def export_student_details_to_file():
    while True:
        m_id = input("Enter Student ID: ")
        if m_id.strip() != "":
            break

    data = {
        "id": m_id,
    }
    result = requests.get(url="http://staging.bldt.ca/api/method/build_it.test.get_student_details",
                           data=data)
    result = json.loads(result.text)
    print(result)
    if result['code'] == 200:
        student = result.get('data')
        my_file = open(str(data['id'])+".txt","w")
        student_details = str(student.get('id')) + " -- " \
                          + str(student.get('full_name')) + " -- " \
                          + str(student.get('mobile_number')) + " -- " \
                          + str(student.get('age')) + " -- " \
                          + str(student.get('level')) + "\n"
        my_file.write(student_details)
        my_file.close()
        print("Student Details Exported Successfully")
    else:
        print("Failed to export student details")


while (True):
    x = int(input("1.Register New Student\n"
                  "2.Edit Student Details\n"
                  "3.Delete Student\n"
                  "4.Export Students to txt file\n"
                  "5.Export Student Details to txt file\n"
                  "6.Exit"))


    if x == 1:
        create_student()
    elif x == 2:
        edit_student()
    elif x == 3:
        delete_student()
    elif x == 4:
        export_students_to_file()
    elif x == 5:
        export_student_details_to_file()
    else:
        exit()
        pass
    


