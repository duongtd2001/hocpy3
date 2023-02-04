# Tạo một class hình chữ nhật chứa hai thuộc tính: chiều dài và chiều rộng
class Rectangle:
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width
# Tạo các method để tính chu vi và diện tích của hình chữ nhật

    def perimeter(self):
        return (self.lenght + self.width) * 2

    def area(self):
        return self.lenght * self.width


# Tạo đối tượng hình chữ nhật và gọi các method tương ứng
rect = Rectangle(30, 20)
per = rect.perimeter()
are = rect.area()
print('chu vi hình chữ nhật là:', per)
print('diện tích hình chữ nhật là:', are)
