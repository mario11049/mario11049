import csv
name = input("whasts your name? ")
home = input("whats your house? ")
with open("hellow.txt", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])
students = []
with open("hellow.txt") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")