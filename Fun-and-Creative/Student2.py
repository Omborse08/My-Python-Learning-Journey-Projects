import os

if not os.path.exists("ReportSave.txt"):
    open("ReportSave.txt",'w').close()
    print("ReportSave.txt File Created")
else:
    print("Its Already Exist")

class reports:
    def __init__(self):
        self.reportss = {}
    
    def menu(self):
        print("""
1. Add Student
2. Remove Student
3. Update Student Marks
4. View All Reports
5. Search Student
6. Save Report to File
7. Show Topper & Lowest
8. Exit
""")
    
    def student_add(self,name,id,marks):
        self.reportss[id] = {
            "Name":name,
            "Marks":{
                "Math":marks[0],
                "Physics":marks[1],
                "Chemistry":marks[2]
            }
        }
    @staticmethod
    def grades(sys):
        if sys > 90:
            return "A"
        elif sys > 75:
            return "B"
        elif sys > 60:
            return "C"
        else:
            return "F"

    def student_remove(self,removed):
        if removed in self.reportss:
            self.reportss.pop(removed)
            print("\nStudent Removed Successfully!")
        else:
            print("\nNo Id Available")

    def student_show(self):
        print(f"{self.reportss}")
        

    def students_info(self):
        for n,m in self.reportss.items():
            total = sum(map(int, m["Marks"].values()))
            percentage = ((total/300) * 100)
            print(f"{n}. {m['Name']} - Total {total} | Precentage {percentage:.2f}% - Grade {self.grades(percentage)}")
    
    def search_student(self,search):
        if search in self.reportss:
            print("\nFound...")
            print(self.reportss[search])
        else:
            print("\nNot Found... ")

    def save_reports(self):
        with open('ReportSave.txt','w') as file:
            for n,m in self.reportss.items():
                total = sum(map(int, m["Marks"].values()))
                percentage = ((total/300) * 100)
                file.write(f"{n}. {m['Name']} - Total {total} | Percentage {percentage:.2f}% - Grade {self.grades(percentage)}\n")
    
    def update_marks(self,roll,new_marks):
        if roll in self.reportss:
            self.reportss[roll]['Marks'] = {
                "Math": new_marks[0],
                "Physics": new_marks[1],
                "Chemistry": new_marks[2]
            }
            print("\nStudent Marks Updated! ")
        else:
            print("\nStudent Id Not Found!")

    def show_topper(self):
        topper_name = ""
        topper_roll = None
        topper_marks = -1

        for roll1, mangos in self.reportss.items():
            total = sum(map(int, mangos["Marks"].values()))
            if total > topper_marks:
                topper_marks = total
                topper_name = mangos["Name"]
                topper_roll = roll1

        print("Topper:", topper_name)
        print("Roll No:", topper_roll)
        print("Total Marks:", topper_marks)

repo = reports()    
repo.menu()
while True:
    try:
        choose = int(input("Choose Option: "))
        match choose:
            case 1:
                student_name = input("Enter Name: ")
                student_roll_no = input("Enter Roll No: ")
                student_marks = input("Enter Marks (math , physics , chemistry): ").split(" ")
                repo.student_add(student_name,student_roll_no,student_marks)
                print("\nStudent Added Successfully! ")

            case 2:
                student_remove_id = input("Enter Student ID to Remove Student: ")
                repo.student_remove(student_remove_id)  
            
            case 3:
                roll = input("Enter Student ID to Update: ")
                new_marks = input("Enter New Marks (Math Physics Chemistry): ").split(" ")
                repo.update_marks(roll, new_marks)

            case 4:
                print("=== Show Report Card ===")
                repo.students_info()

            case 5:
                search_student = input("Enter Student Id: ")
                repo.search_student(search_student)
            
            case 6:
                repo.save_reports()
                print("\nReport Saved Successfully")
            
            case 7:
                print("=== Show Topper ===")
                repo.show_topper()
            
            case 8:
                print("\nThank You For Using Services")
                break

    except Exception:
        print("\nInvalid Option! ")