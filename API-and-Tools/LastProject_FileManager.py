import os
import shutil
import time
import psutil
import requests

class files:
    def __init__(self):
        pass
    def browes(self):
        a = len(os.listdir("D:\Project\DATA"))
        for i in range(a):
            print(f"{i}.",os.listdir(f"D:\Project\DATA")[i])

    def copy_file(self,copy,paste):
        a1 = time.time()
        shutil.copy(f"D:\Project\{copy}",f"D:\{paste}")
        a2 = time.time()
        print(f"\nDuration: {a2-a1:.2f}")
        print("\n> File Copied Successfully..")

    def move_file(self,move,paste1):
        b1 = time.time()
        shutil.move(f"D:\Project\DATA\{move}",f"D:\{paste1}")
        b2 = time.time()
        print(f"\nDuration: {b2-b1:.2f}")
        print("\n> File Moved Successfully..")
    
    def delete_file(self,delete):
        shutil.rmtree(f"D:\Project\DATA\{delete}")
        print("\n> File Deleted Successfully..")
    
    def search_file(self,filename,search):
        c1 = time.time()
        for i,k in  os.walk(search):
            if filename in k:
                print(f"\n> Found: ",os.path.join(i,filename))
                return
            print("\n> File Not Found")
        c2 = time.time()
        print(f"\n> Duration: {c2-c1}")
    
    def system_info(self):
        print("\nSystem Info:")
        print("CPU Usage:", psutil.cpu_percent(), "%")
        mem = psutil.virtual_memory()
        print("RAM Usage:", round(mem.used / (1024**3), 2), "GB /", round(mem.total / (1024**3), 2), "GB")
        print("Disk Usage:", psutil.disk_usage('/').percent, "%")

    def menu(self):
        print("""1 Browes Files
2.Copy File
3.Move File
4.Delete File/Folder
5.Download Photos To Files
6.Backup Files
7.Search Files
8.System Info
9.Exit""")

file = files()
print("> File Locations: [D:\Project\DATA\....]\n")
file.menu()
while True:
    try:
        choose = int(input("\n> Enter Your Choice: "))
        match choose:
            case 1:
                print("\n> In Folder...")
                file.browes()
            
            case 2:
                copy_file_name = input("Enter File Name To Copy: ")
                paste_file_name = input("Enter Where To Paste: ")
                file.copy_file(copy_file_name,paste_file_name)
            
            case 3:
                move_file_name = input("Enter File Name To Move: ")
                move_to_file = input("Enter File Location To Move: ")
                file.move_file(move_file_name,move_to_file)
            
            case 4:
                delete_file = input("Enter File Name To Delete: ")
                sure = input("Are You Sure (y/n): ").lower()
                if sure == "y":
                    file.delete_file(delete_file)
                else:
                    print("\n> Deletetion Cancelled..")
            
            case 5:
                download_file = input("Enter Url To Download: ")
                save_name = input("Enter File Name To Save: ")
                resource = requests.get(download_file)
                open(f"{save_name}", "wb").write(resource.content)
                print("✅ Download complete!")


            case 6:
                backup_name = input("Enter Folder Name To Backup: ")
                Backup_destination = input("Enter Backup Destination From (Home): ")
                file.copy_file(backup_name,Backup_destination)
            
            case 7:
                search_name = input("Search File By Name: ")
                search_docu = input("Enter Locality To Find: ")
                file.search_file(search_name,search_docu)

            case 8:
                file.system_info()

            case 9:
                print("Thank You For Using Our Services: ")
                break
                
            case _:
                print("\n> Invalid Option...")
    except Exception:
        print("\n> Error Not Detectable...")