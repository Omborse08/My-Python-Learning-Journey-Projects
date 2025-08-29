def line():
    print("-----------------------------------")


student_numbers = int(input("Enter Number Of Students to Register: "))
students_info = []
passed_sub = set()
total = 0
sr_no = 0
line()
for i in range(student_numbers):
    sr_no += 1
    print(f"\n       === Entering Data For Student {sr_no} ===")
    name = input("Name: ")
    age = int(input("Age: "))
    marks = float(input("Marks: "))
    course = input("Interested Courses (Seperate with comma): ").split(",")
    old_school = input("Old School Name: ")
    sport = input("Sports Participation (Yes/No): ")
    category = input("Your Category: ")
    subject = input("Passed Subjects: ")
    information = (name,age,marks,course,old_school,sport,category,subject)
    students_info.append(information)
    sub_info = subject.split(",")
    passed_sub.update(sub_info)
    line()

print("\n       ==== Students Eligibilty List ====")
for k in students_info:
    passed = k[2]
    if passed > 55:
        print(f":{k[0]} > ✅ Eligible for Admission")
        total += 1
    else:
        print(f":{k[0]} > ❌ Not Eligible for Admission")


print("\n       ==== All Unique Subjects Passed Across Students ====")
print(f"Subjects > {passed_sub}")



print("\n       ==== Intersted Courses (Index Wise) ====")
for m in students_info:
    sub = m[3]
    sub_name = m[0]
    print(f"\n>Student: {sub_name}: ")
    num = 0
    for n in sub:
        num += 1
        print(f"{num}. {n}")


print("\n         ==== RECURSIVE SUMMARY ====")
print(f"Total Students Registred: {student_numbers}")
print(f"Total Eligible Students: {total}")



