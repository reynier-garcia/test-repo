from .school import School


def main():
    school = School("Cujae")
    school.add_student("Bertha", 30, 5)
    school.add_student("Max", 28, 2)


if __name__ == "__main__":
    main()
