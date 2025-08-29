print("===Student Marks Manage===")
name = []
marks = []
ave = 0
total = 0
print("> Capacity of 100 Student <")
while True:
    print("\n1.Add Student")
    print("2.View All")
    print("3.Search")
    print("4.Topper")
    print("5.Average")
    print("6.Exit")
    a = int(input("Enter Your Choice: "))
    match a:
        case 1:
            b = input("Enter Student Name: ")
            name.append(b)
            c = int(input("Enter Marks: "))
            marks.append(c)
            total = total + c
            print("Student Added Successfully.")
            ave += 1
        case 2:
            if len(name) == 0:
                print("No Student Found! ")
            else:
                print("\nAll Students:")
                for i in range(len(name)):
                    print("-",name[i],":",marks[i])

        case 3:
            if len(name) == 0:
                print("No Student Available: ")
            else:
                d = input("Enter name to search: ")
                if d in name:
                    h = name.index(d)
                    print("Found Name:",d,"Marks:",marks[h])
                else:
                    print("Name not found!")

        case 4:
            if len(name) == 0:
                print("No Student Available: ")
            else:
                print("\nTopper in list is: ")
                high = max(marks)
                ind = marks.index(high)
                print(name[ind],"with",marks[ind])

        case 5:
            if len(name) == 0:
                print("No Student Available:")
            else:
                avega = total / ave
                print("Average of all marks is",avega)

        case 6:
            print("Existing Bye..")
            break

