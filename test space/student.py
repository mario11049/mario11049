class Student:
    def __init__(self , name, house, patronus):
        self.name = name
        self.house = house
        self.patronus = patronus
    def __str__(self):
        return(f"{self.name} from {self.house}")
    def charm(self):
        match self.patronus:
            case "stag":
                return"🐴"
            case "otter":
                return"🥾"
            case "mario":
                return"🕹️"
            case _:
                return"🙏🏻"

def main():
    student = get_student()
    print(student)
    print(student.charm())

def get_student():
    name = input("name: ")
    house = input("home: ")
    patronus = input("patronus: ")
    student = Student(name, house, patronus)
    return student

if __name__ == "__main__":
    main()