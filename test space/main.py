import csv
students = []
while True:
    print("*" * 25)
    print("enter your choice")
    print("1.enter name and city")
    print("2.view the names and cities")
    print("3.delete the name")
    print("4.exit")
    print("*" * 25)
    choice = input("enter ouur choice")
    if choice == "1":
        with open("hellow.txt", "a") as file:
            name = input("enter your name: ")
            town = input("enter your town: ")
            writer = csv.writer(file)
            writer.writerow([name, town])
            print("name and town succefully stored!!")
    elif choice == "2":
        with open("hellow.txt","r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append({"name": row["name"], "town": row["town"]})
        for student in sorted(students,key=lambda student: student["name"]):
            print(f"{student['name']} is living in {student['town']}")
    elif choice == "3":
        print("enter the details you need to delete")
        try:
            name = input("enter the name you wamt to delete: ")
            town = input("enter the town you want to delete: ")
            rows = []
            with open("hellow.txt", "r") as file:
                reader = csv.reader(file)
                header = next(reader)
                for row in reader:
                    if row != [name , town]:
                        rows.append(row)
                    else:
                        with open("hellow.txt", "w", newline="") as file:
                            writer.writerow(header)
                            wtiter = csv.writer(file)
                            writer.writerow(rows)
            print("name and town deleted!!")
        except:
            print("enter valid name and town if you has any doubt please view them once")
    elif choice == "4":
        print("thanks for choosing our code!!!")
        break
    else:
        print("enter valid choice!!")