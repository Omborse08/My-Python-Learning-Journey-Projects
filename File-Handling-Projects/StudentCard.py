school = {}
attendance = {}
subjects = set()

while True:
    print("""
    1. Add Student
    2. Mark Attendance
    3. View Report
    4. Search Student
    5. All Subjects
    6. Exit
    """)
    choose_option = int(input("Choose Option: "))
    match choose_option:
        case 1:
            name = input("Enter Student Name: ")
            number = (input("Enter Roll No: "))
            
            try:
                if int(number) + 1:
                    school[number] = name
                    attendance[number] = set()
                    print(f"Student {name} Added Succesfully✅")
            except:
                print("Invalid Number! Try Again ❌")
        
        case 2:
            roll = (input("Enter Roll Number: "))
            subject = input("Enter Subject: ").split(",")
            subjects.update(subject)
            if roll in attendance:
                attendance[roll].add(subject)
                print(f"✅Attendance For {school[roll]} In {subject}.")
            else:
                print("❌Roll Number Not Found Try Again")

        case 3:
            for i in school and attendance:
                print(f"\nRoll Number: {i} \n   Name: {school[i]} \n   Attended Lec: {attendance[i]}")

        case 4:
            search_stu = input("Enter Roll Number: ")
            if search_stu in school and attendance:
                print(f"\nName: {school[search_stu]} \nattendance: {attendance[search_stu]}")

        case 5:
            print(f"Subjects: {(subjects)}")
        
        case 6:
            print("Thank you for using our services")
            break

            