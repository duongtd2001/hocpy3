'''

'''
# class


class Student:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def show_info(self):
        print(f'''STUDENT INFO
Name: {self.name}  
Age: {self.age}
Address: {self.address}''')

    def __str__(self):
        return f'<(Student(name={self.name}, age={self.age}))>'

    def __gt__(self, other):
        return self.age > other.age


student_one = Student('Bob', 23, 'New York')
Student.show_info(student_one)
# print(student_one.name)
# print(student_one.age)
# print(student_one)


class People:
    def __init__(self, birth_year):
        self.birth_year = birth_year

    @property  # sử dụng khi chỉ truyền vào self, nếu truyền thêm vào sẽ không được
    def get_age(self):
        return 2023 - self.birth_year


people1 = People(2001)
age = people1.get_age
print(age)


# kế thừa
# __init__: được gọi khi

class Human:
    def __init__(self, name):
        self.name = name


class Clhuman(Human):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
