class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def print_car_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")


class Lead:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def change_name(lead):
        lead.name = "Alice"


class Student:
    def __init__(self, name, age, grades: list[float]):
        self.name = name
        self.age = age
        self.grades = grades

    def __str__(self):
        return f"{self.name}, {self.age}"

    @staticmethod
    def get_avg_grades(student: Student):
        return sum(student.grades) / len(student.grades)


car1 = Car("Toyota", "321", 2020)
car1.print_car_info()
car2 = Car("Honda", "101", 2022)
car2.print_car_info()
car3 = Car("Ford", "102", 2025)
car3.print_car_info()

print("-------------------------------------------")


def get_day(number_of_day: int) -> str:
    match number_of_day:
        case 1:
            return "Понедельник"
        case 2:
            return "Вторник"
        case 3:
            return "Среда"
        case 4:
            return "Четверг"
        case 5:
            return "Пятница"
        case 6:
            return "Суббота"
        case 7:
            return "Воскресенье"
    return None


print(get_day(5))
print(get_day(3))

print("-------------------------------------------")

numbers = [65, 85, 1, 0, -965, 542, 32, 9, 23]
max_number = numbers[0]
for number in numbers:
    if number > max_number:
        max_number = number
print(max_number)

print("-------------------------------------------")


def filter_words(words: list) -> list:
    filtered_words = []
    for word in words:
        if len(word) > 5:
            filtered_words.append(word)
    return filtered_words


words_list = ["IT", "Java", "Python", "Java Script", "ML", "Data Science"]
print(*filter_words(words_list), sep=", ")

print("-------------------------------------------")

person = Lead("Mike")
print(person.name)
Lead.change_name(person)
print(person.name)

print("-------------------------------------------")

student1 = Student(name="Mike", age=21, grades=[4.62, 5.0, 4.23])
print(Student.get_avg_grades(student1))
student2 = Student(name="Bob", age=20, grades=[3.5, 4.3, 3.63])
print(Student.get_avg_grades(student2))
student3 = Student(name="Alex", age=18, grades=[5.0, 5.0, 4.5])
print(Student.get_avg_grades(student3))

students = [student1, student2, student3]
for person in students:
    if Student.get_avg_grades(person) > 4.1:
        print(person)
