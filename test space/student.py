class Student:
    def __init__(self , name, house):
        if not name:
            raise ValueError("enter name")
        if house not in {"gryffindor", "slytherine", "ravanclaw"}:
            raise("invalid house")
        self.name = name
        self.house = house
    

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("name: ")
    house = input("home: ")
    student = Student(name, house)
    return student

if __name__ == "__main__":
    main()