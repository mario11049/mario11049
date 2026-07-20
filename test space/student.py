def main():
    student = get_student()
    if student["name"] == "manoj":
        student["home"] = "tgv"
    print(f"{student['name']} is from {student['home']}")

def get_student():
    name = input("name: ")
    home = input("home: ")
    return {"name":name, "home":home}

if __name__ == "__main__":
    main()