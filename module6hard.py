class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        if len(sides) != self.sides_count:
            self.__sides = [6   ] * self.sides_count
        else:
            self.__sides = list(sides)
        self.__color = color
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(value, int) and 0 <= value <= 255 for value in [r, g, b])

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, *new_sides):
        return all(isinstance(side, int) and side > 0 for side in new_sides) and len(new_sides) == self.sides_count

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * 3.141592653589793)

    def get_square(self):
        return 3.141592653589793 * (self.__radius ** 2)

    def set_sides(self, *new_sides):
        super().set_sides(*new_sides)
        self.__radius = self.get_sides()[0] / (2 * 3.141592653589793)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__height = self.calculate_height()

    def calculate_height(self):
        # Реализуйте метод для вычисления высоты треугольника
        # Этот метод требует дополнительной информации, такой как тип треугольника и его стороны
        return None

    def get_square(self):
        s = sum(self.get_sides()) / 2
        a, b, c = self.get_sides()
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

    def set_sides(self, *new_sides):
        super().set_sides(*new_sides)
        self.__height = self.calculate_height()


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(self.get_sides()) != self.sides_count:
            self.set_sides(*([1] * self.sides_count))

    def get_volume(self):
        side_length = self.get_sides()[0]
        return side_length ** 3

    def set_sides(self, *new_sides):
        if len(new_sides) == 1:
            new_sides = new_sides * self.sides_count
        super().set_sides(*new_sides)


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())