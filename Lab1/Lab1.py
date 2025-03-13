import csv
import shutil


class LoginUser():
    def __init__(self, email_address, password):
        self.email_address = email_address
        self.password = password

    def login(self):
        with open('/Users/louisas/Documents/Data 200 - Python/Lab1/Login.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if self.email_address in row[0]:
                    if self.password == row[1]:
                        return True,row[0],row[1],row[2]
                    else:
                        return False,None,None,None


    def logout(self):
        return "Logging Out"

    def change_password(self):
        login = self.login()
        status, email_address, password, role = login 
        if status:
            new_password = input("Please enter your new password: ")
            

    def encrypt_password(self):
        pass

    def decrypt_password(self):
        pass


class Student():
    def __init__(self, email_address, first_name, last_name, course_id, grade, mark):
        self.email_address = email_address
        self.first_name = first_name
        self.last_name = last_name
        self.course_id = course_id
        self.grade = grade
        self.mark = mark
        self.students = []
        self.file_path = '/Users/louisas/Documents/Data 200 - Python/Lab1/Student.csv'

    def display_student_records(self):
        print("Displaying student records...")
        with open(self.file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader) #skip header
            for row in reader:
                student = Student(
                    email_address=row[0],
                    first_name=row[1],
                    last_name=row[2],
                    course_id=row[3],
                    grade=row[4],
                    mark=row[5]
                )
                self.students.append(student)
        if self.students:
            for student in self.students:
                print(f"Email: {student.email_address}, Name: {student.first_name} {student.last_name}, "
                      f"Course ID: {student.course_id}, Grade: {student.grade}, Mark: {student.mark}")
        else:
            print("No student records found.")

    def add_new_student(self, email_address, first_name, last_name, course_id, grade, mark):
        new_student = [email_address, first_name, last_name, course_id, grade, mark]

        with open(self.file_path, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(new_student)
        
        print(f"New student: '{self.first_name} {self.last_name}' added.")


    def delete_student(self, email_address):
        students = []
        try:
            with open(self.file_path, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) > 0 and row[0] != email_address:  # Ensure row is not empty
                        students.append(row)

            with open(self.file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(students)  # Write back filtered data

            print(f"✅ Student with email {email_address} has been deleted.")
        
        except Exception as e:
            print(f"⚠️ Error deleting student: {e}")


    def update_student_record(self):
        pass

    def check_my_grades(self):
        pass

class Professor():
    def __init__(self, email_address, first_name, last_name, rank, course_id):
        self.email_address = email_address
        self.first_name = first_name
        self.last_name = last_name
        self.rank = rank
        self.course_id = course_id
        self.professors = []
        self.file_path = '/Users/louisas/Documents/Data 200 - Python/Lab1/Professor.csv'

    def display_professors(self):
        print("Displaying professor records...")
        with open(self.file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader) #skip header
            for row in reader:
                professor = Professor(
                    email_address=row[0],
                    first_name=row[1],
                    last_name=row[2],
                    rank=row[3],
                    course_id=row[4],
                )
                self.professors.append(professor)
        if self.professors:
            for professor in self.professors:
                print(f"Email: {professor.email_address}, Name: {professor.first_name} {professor.last_name}, "
                      f"Rank: {professor.rank}, Course ID: {professor.course_id}")
        else:
            print("No professor records found.")


    def add_new_professor(self, email_address, first_name, last_name, rank, course_id):
        new_professor = [email_address, first_name, last_name, rank, course_id]

        with open(self.file_path, mode='a', newline=' ', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(new_professor)
        
        print(f"New professor: '{self.first_name} {self.last_name}' added.")

    def delete_professor(self, email_address):
        professors = []
        try:
            with open(self.file_path, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) > 0 and row[0] != email_address:  # Ensure row is not empty
                        professors.append(row)

            with open(self.file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(professors)  # Write back filtered data

            print(f"Professor with email {email_address} has been deleted.")
        
        except Exception as e:
            print(f"Error deleting professor: {e}")

    def update_professor(self):
        pass

    def show_course_details_by_professor(self):
        pass


class Course():
    def __init__(self, course_id, course_name, description):
        self.course_id = course_id
        self.course_name = course_name
        self.description = description
        self.courses = []
        self.file_path = '/Users/louisas/Documents/Data 200 - Python/Lab1/Course.csv'

    def display_courses(self):
        print("Displaying course records...")
        with open(self.file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader) #skip header
            for row in reader:
                course = Course(
                    course_id=row[0],
                    course_name=row[1],
                    description=row[2]
                )
                self.courses.append(course)
        if self.courses:
            for course in self.courses:
                print(f"Course id: {course.course_id}, Course Name: {course.course_name}, Description: {course.description}, ")
        else:
            print("No course records found.")

    def add_new_course(self, course_id, course_name, description):
        new_course = [course_id, course_name, description]

        with open(self.file_path, mode='a', newline=' ', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(new_course)
        
        print(f"New course: '{self.course_id} - {self.course_name}' added.")

    def delete_course(self, course_id):
        courses = []
        try:
            with open(self.file_path, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) > 0 and row[0] != course_id:  # Ensure row is not empty
                        courses.append(row)

            with open(self.file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(courses)  # Write back filtered data

            print(f"Course with id '{course_id}' has been deleted.")
        
        except Exception as e:
            print(f"Error deleting professor: {e}")

    def update_course(self):
        pass        

    def average_grade_by_course(self):
        pass



def get_new_student_details():
    email_address = input("Please enter the email address of the new student: ")
    first_name = input("Please enter the first name of the new student: ")
    last_name = input("Please enter the last name of the new student: ")
    course_id = input("Please enter the new student's course id: ")
    grade = input("Please enter the new student's associated grade: ")
    mark = input("Please enter the new student's associated mark: ")
    return email_address.strip(), first_name.strip(), last_name.strip(), course_id.strip(), grade.strip(), mark.strip()

def get_new_professor_details():
    email_address = input("Please enter the email address of the new professor: ")
    first_name = input("Please enter the first name of the new professor: ")
    last_name = input("Please enter the last name of the new professor: ")
    rank = input("Please enter the rank of the new professor: ")
    course_id = input("Please enter the new professor's course id: ")
    return email_address.strip(), first_name.strip(), last_name.strip(), rank.strip(), course_id.strip()

def get_new_course_details():
    course_id = input("Please enter the new course's id: ")
    course_name = input("Please enter the new course's name: ")
    description = input("Please enter the new course's description: ")
    return course_id.strip(), course_name.strip(), description.strip()

def get_student_email():
    student_email = input("Please enter the student's email: ")
    return student_email

def get_professor_email():
    professor_email = input("Please enter the professor's email: ")
    return professor_email

def get_course_id():
    cid = input("Please enter the course id: ")
    return cid

def checkmygrade_main_menu():
    while True:
        columns = shutil.get_terminal_size().columns
        print("================================".center(columns))
        print("Welcome to CheckMyGrade".center(columns))
        print("================================".center(columns))
        print("\n CheckMyGrade Main Menu:")
        print("1. Login")
        print("2. Signup")
        print("3. Exit")
        choice = input("Please select an option: ")
        if choice == '1':
            print("Executing option 1...")
            email_address = input("Enter your email address: ")
            password = input("Enter your password: ")
            login1=LoginUser(email_address.strip(),password.strip())
            status,user_id,password,role=login1.login()
            if status:
                print("Logging in...")
                if role == 'student':
                    student1 = Student()
                    while True:
                        print("================================".center(columns))
                        print("Welcome to CheckMyGrade".center(columns))
                        print("================================".center(columns))
                        print("\n CheckMyGrade Student Main Menu:")
                        print("1. View grades")
                        print("2. Check my marks")
                        print("3. Update personal details")
                        print("4. Update login details")
                        print("5. View course details")
                        print("6. View professor details")
                        print("7. Exit")
                        choice = input("Please select an option: ")
                        if choice == '1':
                            pass
                        if choice == '2':
                            pass
                        if choice == '3':
                            pass
                        if choice == '4':
                            pass
                        if choice == '5':
                            pass
                        if choice == '6':
                            pass
                        if choice == '7':
                            print("\nLogging Out...")
                            break
                if role == 'professor':
                    while True:
                        print("================================".center(columns))
                        print("Welcome to CheckMyGrade".center(columns))
                        print("================================".center(columns))
                        print("\n CheckMyGrade Professor Main Menu:")
                        print("1. Update personal details")
                        print("2. Update login details")
                        print("3. Add/delete/modify student")
                        print("4. Add/delete/modify grade")
                        print("5. View grade report")
                        print("6. Exit")
                        choice = input("Please select an option: ")
                        if choice == '1':
                            pass
                        if choice == '2':
                            pass
                        if choice == '3':
                            print("\n1. Add Student")
                            print("2. Delete Student")
                            #print("3. Modify Student")
                            choice = input("Please select an option: ")
                            if choice == '1':
                                print("\nAdding new student...")
                                semail, sfirst, slast, scourseid, sgrade, smark = get_new_student_details()
                                student = Student(semail, sfirst, slast, scourseid, sgrade, smark)
                                student.add_new_student(semail, sfirst, slast, scourseid, sgrade, smark)
                            elif choice == '2':
                                print("\nDeleting student...")
                                semail = get_student_email()
                                student = Student('','','','','','')
                                student.delete_student(semail)
                            elif choice == '3':
                                pass
                        if choice == '4':
                            pass
                        if choice == '5':
                            pass
                        if choice == '6':
                            print("\nLogging Out...")
                            break
                if role == 'admin':
                    while True:
                        print("================================".center(columns))
                        print("Welcome to CheckMyGrade".center(columns))
                        print("================================".center(columns))
                        print("\n CheckMyGrade Admin Main Menu:")
                        print("1. Professor details")
                        print("2. Course details")
                        print("3. Student records")
                        print("4. Add/delete/modify professor")
                        print("5. Add/delete/modify course")
                        print("6. Add/delete/modify student")
                        print("7. Exit")
                        choice = input("Please select an option: ")
                        if choice == '1':
                            professor1 = Professor('', '', '', '', '')
                            professor1.display_professors()
                        if choice == '2':
                            course1 = Course('', '', '')
                            course1.display_courses()
                        if choice == '3':
                            student1 = Student('', '', '', '', '', '')
                            student1.display_student_records()
                        if choice == '4':
                            print("\n1. Add Professor")
                            print("2. Delete Professor")
                            #print("3. Modify Professor")
                            choice = input("Please select an option: ")
                            if choice == '1':
                                print("\nAdding new professor...")
                                pemail, pfirst, plast, prank, pcourseid = get_new_professor_details()
                                professor = Professor(pemail, pfirst, plast, prank, pcourseid)
                                professor.add_new_professor(pemail, pfirst, plast, prank, pcourseid)
                            elif choice == '2':
                                print("\nDeleting professor...")
                                pemail = get_professor_email()
                                professor = Professor('','','','','')
                                professor.delete_professor(pemail)
                        if choice == '5':
                            print("\n1. Add Course")
                            print("2. Delete Course")
                            #print("3. Modify Course")
                            choice = input("Please select an option: ")
                            if choice == '1':
                                print("\nAdding new course...")
                                cid, cname, cdescription = get_new_course_details()
                                course = Course(cid, cname, cdescription)
                                course.add_new_course(cid, cname, cdescription)
                            elif choice == '2':
                                print("\nDeleting course...")
                                cid = get_course_id()
                                course = Course('','','')
                                course.delete_course(cid)
                        if choice == '6':
                            print("\n1. Add Student")
                            print("2. Delete Student")
                            #print("3. Modify Student")
                            choice = input("Please select an option: ")
                            if choice == '1':
                                print("\nAdding new student...")
                                semail, sfirst, slast, scourseid, sgrade, smark = get_new_student_details()
                                student = Student(semail, sfirst, slast, scourseid, sgrade, smark)
                                student.add_new_student(semail, sfirst, slast, scourseid, sgrade, smark)
                            elif choice == '2':
                                print("\nDeleting student...")
                                semail = get_student_email()
                                student = Student('','','','','','')
                                student.delete_student(semail)
                        if choice == '7':
                            print("\nLogging Out...")
                            break




if __name__ == '__main__':
    checkmygrade_main_menu()