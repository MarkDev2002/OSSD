class Person:
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob

    def describe(self):
        pass

class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.grade = grade

    def describe(self):
        print(f"Student: {self.name}, Year of Birth: {self.yob}, Grade: {self.grade}")

class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        print(f"Teacher: {self.name}, Year of Birth: {self.yob}, Subject: {self.subject}")

class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        print(f"Doctor: {self.name}, Year of Birth: {self.yob}, Specialist: {self.specialist}")

class Ward:
    def __init__(self, ward_name):
        self.ward_name = ward_name
        self.people = []

    def addPerson(self, person):
        self.people.append(person)

    def describe(self):
        print(f"Ward: {self.ward_name}")
        for person in self.people:
            person.describe()

    def countDoctor(self):
        return sum(1 for person in self.people if isinstance(person, Doctor))

    def sortAge(self):
        self.people.sort(key=lambda person: person.yob)

    def aveTeacherYearOfBirth(self):
        teacher_yobs = [person.yob for person in self.people if isinstance(person, Teacher)]
        return sum(teacher_yobs) / len(teacher_yobs) if teacher_yobs else 0

    def removePerson(self, name):
        self.people = [person for person in self.people if person.name != name]

    def findOldestPerson(self):
        oldest_person = max(self.people, key=lambda person: person.yob, default=None)
        if oldest_person:
            oldest_person.describe()

    def findPersonBySpecialist(self, specialist):
        for person in self.people:
            if isinstance(person, Doctor) and person.specialist == specialist:
                person.describe()

    def findStudentsByGrade(self, grade):
        for person in self.people:
            if isinstance(person, Student) and person.grade == grade:
                person.describe()

    def updateTeacherSubject(self, name, new_subject):
        for person in self.people:
            if isinstance(person, Teacher) and person.name == name:
                person.subject = new_subject

    def findPersonByName(self, name):
        for person in self.people:
            if person.name == name:
                person.describe()

    def aveAgeByOccupation(self, occupation):
        current_year = 2024
        ages = []
        for person in self.people:
            if occupation == "student" and isinstance(person, Student):
                ages.append(current_year - person.yob)
            elif occupation == "teacher" and isinstance(person, Teacher):
                ages.append(current_year - person.yob)
            elif occupation == "doctor" and isinstance(person, Doctor):
                ages.append(current_year - person.yob)
        return sum(ages) / len(ages) if ages else 0

ward = Ward("A1")

ward.addPerson(Student("Alice", 2005, "10A"))
ward.addPerson(Teacher("Mr. Smith", 1980, "Math"))
ward.addPerson(Teacher("Ms. Johnson", 1975, "History"))
ward.addPerson(Doctor("Dr. Brown", 1970, "Cardiology"))
ward.addPerson(Doctor("Dr. Green", 1965, "Neurology"))

ward.describe()

print("\nSố lượng bác sĩ:", ward.countDoctor())
ward.sortAge()
print("\nDanh sách sau khi sắp xếp theo tuổi tăng dần:")
ward.describe()
print("\nTrung bình năm sinh của giáo viên:", ward.aveTeacherYearOfBirth())

print("\nDanh sách sau khi xóa Ms. Johnson:")
ward.removePerson("Ms. Johnson")
ward.describe()


