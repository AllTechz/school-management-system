import os
import mysql.connector
import datetime
db = mysql.connector.connect(host="localhost", user="root", password="12345", database="school_management")
cursor = db.cursor()
last_success_message = None

def clear_screen():
    os.system("cls")

def display_last_success():
    global last_success_message 
    if last_success_message is not None:
        print(last_success_message + "\n")
        last_success_message = None

def call_fallback_function(fallback_functions_number):
    if fallback_functions_number == 1:
        student_menu()
    elif fallback_functions_number == 2:
        subject_menu()
    elif fallback_functions_number == 3:
        marks_management()
    elif fallback_functions_number == 4:
        view_information()

def validate(term, validate_for, fallback_function_number):
    global last_success_message
    if not term:
        last_success_message = "Invalid value"
        return False
    if validate_for.lower() == "id":
        if not term.strip().isdigit():
            last_success_message = "Id should be a integer"
            call_fallback_function(fallback_function_number)
    if validate_for.lower() == "class":  # 12A , 9E , 11
        spl = len(term)
        if term.strip()[-1].isalpha(): spl = -1
        if ((not term.strip()[:spl].isdigit()) or (not (0 < int(term.strip()[:spl]) <= 12))):
                last_success_message = "Not a valid class (Ex: 12B, 5)"
                call_fallback_function(fallback_function_number)
    if validate_for.lower() == "marks-percentage": # 45.25
        try:
            if not (0 <= float(term) <=100):
                raise Exception
        except:
            last_success_message = "Not a valid percentage (1 to 100)"
            call_fallback_function(fallback_function_number)
    if validate_for.lower() == "date":   #1998-05-12
        date_part = term.split("-")
        try:
            term = datetime.datetime(int(date_part[0]), int(date_part[1]), int(date_part[-1]))
        except:
            last_success_message = "Not a valid date (Ex: 1998-05-12)"
            call_fallback_function(fallback_function_number)
    return True

def sql_validation(validation_table, validate_for, fallback_function_number, fetch="*", enable_return = False, check_for="insert"):
    global last_success_message
    step = len(list(validate_for.keys()))
    init_step = step
    check_query = "SELECT {} FROM {} WHERE ".format(fetch, validation_table)
    for validation_key in validate_for:
        check_query+="{} = {}".format(validation_key, validate_for[validation_key])
        if step != 1:
            check_query+=" AND "
            step-=1
    cursor.execute(check_query)
    query_check = cursor.fetchone()
    key_list = list(validate_for.keys())
    if (not query_check) and init_step == 1:
        last_success_message = "{} does not exist".format(key_list[0])
        call_fallback_function(fallback_function_number)
    if (query_check) and init_step == 2 and check_for == "insert":
        last_success_message = "Marks for this {} and {} already exist.".format(key_list[0], key_list[-1])
        call_fallback_function(fallback_function_number)
    if (not query_check) and init_step == 2 and check_for == "update":
        last_success_message = "Marks for this {} and {} does not exist.".format(key_list[0], key_list[-1])
        call_fallback_function(fallback_function_number)
    if enable_return:
        return query_check

def fetch_student_details(student_id, fallback_function_number, enable_return = False):
    global last_success_message
    student = sql_validation('Students', {'student_id': student_id}, fallback_function_number, "*", True)
    last_success_message = "Current Student Information:\n"
    last_success_message += "Name: {}\n".format(student[1])
    last_success_message += "Date of Birth: {}\n".format(student[2])
    last_success_message += "Contact Info: {}\n".format(student[3])
    last_success_message += "Class: {}".format(student[4])
    if enable_return:
        return student

def sql_execution_handler(query, success_msg):
    global last_success_message
    try:
        if type(query) is not list: query = [query]
        for q in query:
            cursor.execute(q)
        db.commit()
        last_success_message = success_msg
    except mysql.connector.Error as err:
        last_success_message = "Error: {}".format(err)

def str_converter(string):
    escape_seq_vals = {"\'": r"\'", "\"": r"\""}
    result = ""
    for char in string:
        if char not in escape_seq_vals:
            result+=char
        else:
            result+=escape_seq_vals[char]
    return result

def main_menu():
    clear_screen()
    print("School Management System\n")
    display_last_success()
    print("1. Student Management")
    print("2. Subject Management")
    print("3. Marks Management")
    print("4. View Information")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        student_menu()
    elif choice == '2':
        subject_menu()
    elif choice == '3':
        marks_management()
    elif choice == '4':
        view_information()
    elif choice == '5':
        cursor.close()
        db.close()
        print("Goodbye!")
        exit()
    else:
        input("Invalid choice. Press Enter to continue...")
        main_menu()

def student_menu():
    clear_screen()
    print("Student Management\n")
    display_last_success()
    print("1. Add Student Record")
    print("2. Update Student Information")
    print("3. Delete Student Record")
    print("4. Back to Main Menu")
    choice = input("Enter your choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        update_student_info()
    elif choice == '3':
        delete_student()
    elif choice == '4':
        main_menu()
    else:
        input("Invalid choice. Press Enter to continue...")
        student_menu()

def subject_menu():
    clear_screen()
    print("Subject Management\n")
    display_last_success()
    print("1. Add Subject")
    print("2. Update Subject")
    print("3. Delete Subject")
    print("4. Back to Main Menu")
    choice = input("Enter your choice: ")
    if choice == '1':
        add_subject()
    elif choice == '2':
        update_subject()
    elif choice == '3':
        delete_subject()
    elif choice == '4':
        main_menu()
    else:
        input("Invalid choice. Press Enter to continue...")
        subject_menu()
        
def marks_management():
    clear_screen()
    print("Marks Management\n")
    display_last_success()
    print("1. Add Marks")
    print("2. Update Marks")
    print("3. Delete Marks")
    print("4. Back to Main Menu")
    choice = input("Enter your choice: ")
    if choice == '1':
        add_marks()
    elif choice == '2':
        update_marks()
    elif choice == '3':
        delete_marks()
    elif choice == '4':
        main_menu()
    else:
        input("Invalid choice. Press Enter to continue...")
        marks_management()

def view_information():
    clear_screen()
    print("View Information\n")
    display_last_success()
    print("1. View Student Details")
    print("2. View Student Marks")
    print("3. Filter Students by (class, name, avg percentage)")
    print("4. View all Subjects")
    print("5. Back to Main Menu")
    choice = input("Enter your choice: ")
    if choice == '1':
        view_student_details()
    elif choice == '2':
        view_student_marks()
    elif choice == '3':
        view_filter_students()
    elif choice == '4':
        view_subjects()
    elif choice == '5':
        main_menu()
    else:
        input("Invalid choice. Press Enter to continue...")
        view_information()

def view_student_details():
    clear_screen()
    global last_success_message
    student_id = input("Enter student's ID: ")
    if validate(student_id, "id", 4):
        fetch_student_details(student_id, 4)
    view_information()

def view_student_marks():
    clear_screen()
    global last_success_message
    student_id = input("Enter student's ID: ")
    if not validate(student_id, "id", 4):
        view_information()
    student_name, student_class = sql_validation('Students', {'student_id': student_id}, 4, "name, class", True)
    select_query = "SELECT subject_name, mark FROM Marks, Subjects WHERE Marks.subject_id = Subjects.subject_id AND Marks.student_id = {}".format(student_id)
    cursor.execute(select_query)
    marks = cursor.fetchall()
    if not marks:
        last_success_message = "No marks found for this student."
    else:
        last_success_message = "Marks for Student ID {}\n".format(student_id)
        last_success_message += "Name: {}, Class: {}\n".format(student_name, student_class)
        total_mark = 0
        for subject, mark in marks:
            last_success_message += "{}: {}\n".format(subject, mark)
            total_mark += mark
        if len(marks) > 0:
            avg_mark = total_mark / len(marks)
        else:
            avg_mark = 0
        last_success_message += "Average Mark: {:.2f}".format(avg_mark)
    view_information()

def view_filter_students():
    clear_screen()
    global last_success_message
    print("Leave the field empty if filter not required\n")
    class_level = input("Enter class: ")
    validate(class_level, "class", 4)
    name = input("Enter name: ")
    validate(name, "garbage-value", 4)
    name = str_converter(name)
    avg_percentage = input("Enter the minimum average percentage (1-100): ")
    validate(avg_percentage, "marks-percentage", 4)
    filter_query = "SELECT Students.student_id, Students.name, Students.class FROM Students WHERE "
    filter_values=[]
    if class_level:
        filter_values.append("Students.class LIKE '{}%'".format(class_level.upper()))
    if name:
        filter_values.append("name LIKE '%{}%'".format(name))
    if avg_percentage:
        filter_values.append("Students.student_id IN (SELECT student_id FROM Marks GROUP BY student_id HAVING AVG(mark) >= {})".format(avg_percentage))
    if not filter_values:
        last_success_message = "No filters selected made."
    else:
        filter_query += " AND ".join(filter_values)
        cursor.execute(filter_query)
        students = cursor.fetchall()
        if not students:
            last_success_message = "No students match the criteria."
        else:
            if name:
                last_success_message = "all \"{}\"(s)".format(name)
            else:
                last_success_message = "\nStudents"
            if class_level:
                last_success_message += " in class {}".format(class_level.upper())
            if avg_percentage:
                last_success_message += " with an average percentage of {:.2f} or greater".format(float(avg_percentage))
            last_success_message += ":\n"
            for student in students:
                last_success_message += "Student ID: {}, Name: {}, Class: {}\n".format(student[0], student[1], student[-1])
            last_success_message += "\nTotal Students: {}".format(len(students))
    view_information()

def view_subjects():
    clear_screen()
    global last_success_message
    select_query = "SELECT subject_id, subject_name FROM Subjects"
    cursor.execute(select_query)
    subjects = cursor.fetchall()
    if not subjects:
        last_success_message = "No subjects found."
    else:
        last_success_message = "\nSubjects\n"
        for subject_id, subject_name in subjects:
            last_success_message += "Subject ID: {}, Subject Name: {}\n".format(subject_id, subject_name)
    view_information()

def add_student():
    clear_screen()
    name = str_converter(input("Enter student's name: "))
    if not validate(name, "garbage-value", 1):
        student_menu()
    date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
    validate(date_of_birth, "date", 1)
    contact_info = str_converter(input("Enter Contact Info: "))
    if not validate(contact_info, "garbage-value", 1):
        student_menu()
    class_level = input("Enter class: ")
    if not validate(class_level, "garbage-value", 1):
        student_menu()
    insert_query = "INSERT INTO Students (name, date_of_birth, contact_info, class) VALUES ('{}', '{}', '{}', '{}')".format(name, date_of_birth, contact_info, class_level)
    sql_execution_handler(insert_query, "Student record added successfully!")
    student_menu()

def update_student_info():
    clear_screen()
    global last_success_message
    student_id = input("Enter student's ID: ")
    if not validate(student_id, "id", 1):
        student_menu()
    fetch_student_details(student_id, 1)
    display_last_success()
    new_name = str_converter(input("Enter the new name (leave empty to keep the current name): "))
    new_dob = input("Enter the new date of birth (YYYY-MM-DD, leave empty to keep the current date of birth): ")
    validate(new_dob, "date", 1)
    new_contact = str_converter(input("Enter the new contact info (Leave empty to keep the current contact info): "))
    new_class = input("Enter the new class (leave empty to keep the current class): ")
    validate(new_class, "class", 1)
    update_query = "UPDATE Students SET "
    update_values = []
    if new_name:
        update_values.append("name = '{}'".format(new_name))
    if new_dob:
        update_values.append("date_of_birth = '{}'".format(new_dob))
    if new_contact:
        update_values.append("contact_info = '{}'".format(new_contact))
    if new_class:
        update_values.append("class = '{}'".format(new_class))
    if not update_values:
        last_success_message = "No changes made. Student information remains the same."
    else:
        update_query += ", ".join(update_values)
        update_query += " WHERE student_id = {}".format(student_id)
        sql_execution_handler(update_query, "Student information updated successfully!")
    student_menu()

def delete_student():
    clear_screen()
    global last_success_message
    student_id = input("Enter student's ID to delete: ")
    if not validate(student_id, "id", 1):
        student_menu()
    student = fetch_student_details(student_id, 1, True)
    confirmation = input("Are you sure you want to delete {}'s record (Y/N)? ".format(student[1].strip().lower()))
    if confirmation == 'y':
        delete_query = ["DELETE FROM Students WHERE student_id = {}".format(student_id),
                        "DELETE FROM Marks WHERE student_id = {}".format(student_id)]
        sql_execution_handler(delete_query, "Student record deleted successfully!")
    else:
        last_success_message = "Deletion canceled."
    student_menu()

def add_subject():
    clear_screen()
    subject_name = str_converter(input("Enter subject name: "))
    if not validate(subject_name, "garbage-value", 2):
        subject_menu()
    insert_query = "INSERT INTO Subjects (subject_name) VALUES ('{}')".format(subject_name)
    sql_execution_handler(insert_query, "Subject added successfully!")
    subject_menu()

def update_subject():
    clear_screen()
    global last_success_message
    subject_id = input("Enter subject ID to update: ")
    if not validate(subject_id, "id", 2):
        subject_menu()
    subject = sql_validation('Subjects', {'subject_id': subject_id}, 2, "*", True)
    last_success_message = "Current Subject Information:\n"
    last_success_message += "Subject Name: {}\n".format(subject[1])
    display_last_success()
    new_subject_name = str_converter(input("Enter the new subject name (leave empty to keep the current name): "))
    if not new_subject_name:
        last_success_message = "No changes made. Subject information remains the same."
    else:
        update_query = "UPDATE Subjects SET subject_name = '{}' WHERE subject_id = {}".format(new_subject_name, subject_id)
        sql_execution_handler(update_query, "Subject information updated successfully!")
    subject_menu()

def delete_subject():
    clear_screen()
    global last_success_message
    subject_id = input("Enter subject ID to delete: ")
    if not validate(subject_id, "id", 2):
        subject_menu()
    subject = sql_validation('Subjects', {'subject_id': subject_id}, 2, "*", True)
    confirmation = input("Are you sure you want to delete > {} < (Y/N)? ".format(subject[1].strip().lower()))
    if confirmation == 'y':
        delete_query =[ "DELETE FROM Subjects WHERE subject_id = {}".format(subject_id),
                        "DELETE FROM Marks WHERE subject_id = {}".format(subject_id)]
        sql_execution_handler(delete_query, "Subject deleted successfully!")
    else:
        last_success_message = "Deletion canceled."
    subject_menu()

def add_marks():
    clear_screen()
    student_id = input("Enter student's ID: ")
    if not validate(student_id, "id", 3):
        marks_management()
    sql_validation('Students', {'student_id': student_id}, 3)
    subject_id = input("Enter subject ID: ")
    if not validate(subject_id, "id", 3):
        marks_management()
    sql_validation('Subjects', {'subject_id': subject_id}, 3)
    marks = input("Enter the marks: ")
    if not validate(marks, "marks-percentage", 3):
        marks_management()
    sql_validation('Marks', {'student_id': student_id, 'subject_id': subject_id}, 3)
    current_date = datetime.date.today()
    insert_query = "INSERT INTO Marks (student_id, subject_id, mark, date_recorded) VALUES ({}, {}, {}, '{}')".format(student_id, subject_id, marks, current_date)
    sql_execution_handler(insert_query, "Marks added successfully!")
    marks_management()

def update_marks():
    clear_screen()
    global last_success_message
    student_id = input("Enter student's ID: ")
    if not validate(student_id, "id", 3):
        marks_management()
    sql_validation('Students', {'student_id': student_id}, 3)
    subject_id = input("Enter subject ID: ")
    if not validate(subject_id, "id", 3):
        marks_management()
    subject = sql_validation('Subjects', {'subject_id': subject_id}, 3, enable_return=True)
    marks = sql_validation('Marks', {'student_id': student_id, 'subject_id': subject_id}, 3,enable_return=True, check_for="update")
    last_success_message = "\nCurrent Marks Information:\n"
    last_success_message += "Subject Name: {}, Old Marks: {}".format(subject[-1], marks[-2])
    display_last_success()
    new_mark = input("Enter the new mark: ")
    if not validate(new_mark, "marks-percentage", 3):
        marks_management()
    update_query = "UPDATE Marks SET mark = {} WHERE student_id = {} AND subject_id = {}".format(new_mark, student_id, subject_id)
    sql_execution_handler(update_query, "Marks updated successfully!")
    marks_management()

def delete_marks():
    clear_screen()
    global last_success_message
    student_id = input("Enter student's ID: ")
    if not validate(student_id, "id", 3):
        marks_management()
    sql_validation('Students', {'student_id': student_id}, 3)
    subject_id = input("Enter subject ID: ")
    if not validate(subject_id, "id", 3):
        marks_management()
    subject = sql_validation('Subjects', {'subject_id': subject_id}, 3, enable_return=True)
    marks = sql_validation('Marks', {'student_id': student_id, 'subject_id': subject_id}, 3, enable_return=True, check_for="update")
    confirmation = input("Are you sure you want to delete > {}:{} < (Y/N)? ".format(subject[-1].strip().lower(), marks[-2]))
    if confirmation == 'y':
        delete_query = "DELETE FROM Marks WHERE student_id = {} AND subject_id = {}".format(student_id, subject_id)
        sql_execution_handler(delete_query, "Marks deleted successfully!")
    else:
        last_success_message = "Deletion canceled."
    marks_management()

def main():
  while True:
    main_menu()

if __name__ == "__main__":
  main()
