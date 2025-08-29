def line():
    print("---------------------------------------")

def percentages():
    if percentage > 90:
        print("Grade A")
    elif percentage > 70:
        print("Grade B")
    elif percentage > 50:
        print("Grade C")
    else:
        print("Failed")

students = []
while True:
    print("\n1.Add Student")
    print("2.View Student")
    print("3.Exit")
    choose_option = int(input("Choose Option: "))
    match choose_option:

        case 1:
            for i in range(3):
                student_name = input("\nEnter Student Name: ")
                i = 0
                marks = []
                for j in range(3):
                    i += 1
                    student_mark = int(input(f"Enter Student marks for subject {i}: "))
                    marks.append(student_mark)
            
                student = (student_name,marks)
                students.append(student)
        
        case 2:
            for k in students:
                line()
                print(f"Name: {k[0]}")
                print(f"Marks: {k[1]}")
                total = sum(k[1])                         
                print(f"Total: {total}")
                percentage = (total/300) * 100
                print(f"Percentage: {percentage:.2f}")
                percentages()
            line()


        case 3:
            print("Existing")
            break

        case _:
            print("Invalid Option: ")




            