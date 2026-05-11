#Student performance Management System

students = []

#Functionto calculate total,average, and status
def calculate_results(student):
    total = sum(student["scores"].values())
    average = total / len(student["scores"])
    
    if average >= 50:
        status = "pass"
    else:
        status = "Fail"
    student["total"] = total
    student["average"] = average
    student["status"] = status

#Function to add students
def add_students():
    num_students = int(input("Enter number of students:"))
    for i in range(num_students):
        print(f"\nEntering details for student {i+1}")

        name = input("Enter student name:")
        age = int(input("Enter age:"))
        num_subjects = int(input("Enter number of subjects:"))
        scores = {}
        for j in range(num_subjects):
            subject = input(f"Enter subject {j+1} name:")
            mark = float(input(f"Enter score for {subject}:"))
            scores[subject] = mark
            student = {
                "name":name,
                "age":age,
                "scores":scores
            }
            calculate_results(student)
            students.append(student)
# Function to display all students
def display_students():
    print("\n--Student Records---")

    for student in students:
        print(f"\nName: {student['name']}")
        print(f"Age: {student['age']}")
        print("Scores:")

        for subject, score in student["scores"].items():
            print(f" {subject}: {score}")
        print(f"Total: {student['total']}")
        print(f"Average: {student['average']:.2f}")
        print(f"Status: {student['status']}")

#Function to find top-performing student
def top_student():
    if not students:
        print("No student records available.")
        return
    top = max(students, key=lambda x:x["average"])

    print("\n---Top performance Student---")
    print(f"Name: {top['name']}")
    print(f"Average Score:  {top['average']:.2f}")

#Function to search and update student scores
def search_and_update():
    search_name = input("\nEnter student name to search:")
    for student in students:
        if student["name"].lower() == search_name.lower():

            print(f"\nStudent Found:{student['name']}")
            print("Current Scores:")
            for subject,score in student["scores"].items():
                print(f"{subject}: {score}")
                choice = input("\nDo you want to update score? (yes/no):")
                if choice.lower() == "yes":
                    for subject in student["scores"]:
                        new_score = float(input(f"Enter new score for {subject}:"))
                        student["scores"][subject] = new_score

                    calculate_results(student)
                    print("\Score update successfully!")
                    print(f"New Total: {student['total']}")
                    print(f"New Average:{student['average']:.2f}")
                    print(f"New Status: {student['status']}")
                    return
                print("Student not found.")
#Main program
while True:
    print("\n====Student management System=====")
    print("1.Add students")
    print("2.Display Student Record")
    print("3.show Top Student")
    print("4.Search and update student")
    print("5.Exit")
    choice = input("Enter your choice:")
    if choice == "1":
        add_students()
    elif choice == "2":
        display_students()
    elif choice =="3":
        top_student()
    elif choice == "4":
        search_and_update()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice.Try again.")

        

