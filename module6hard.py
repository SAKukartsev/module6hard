class Figure:
    sides_count = 0

    def __init__(self, sides=(), color=(), filled=True):
        if self.__is_valid_sides(sides):
            i = 0
            self.__sides = []
            while i < self.sides_count:
                self.__sides.append(sides[i])
                i += 1
        else:
            i = 0
            self.__sides = []
            while i < self.sides_count:
                self.__sides.append(1)
                i += 1
        if len(color) == 3:
            if self.__is_valid_color(color[0], color[1], color[2]):
                self.__color = color
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if (0 <= r <= 255
                and 0 <= g <= 255
                and 0 <= b <= 255):
            if (isinstance(r, int)
                    and isinstance(g, int)
                    and isinstance(b, int)):
                return True
            else:
                return False
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)
            return self.__color
        else:
            return False

    def __is_valid_sides(self, sides):
        if len(sides) == self.sides_count:
            for side in sides:
                if isinstance(side, int):
                    if side > 0:
                        return True
                    else:
                        return False
                else:
                    return False
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        P = 0
        for side in self.__sides:
            P += side
        return P

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            for i in range(0, self.sides_count):
                self.__sides[i] = new_sides[i]


class Circle(Figure):
    sides_count = 1

    def __init__(self, color=(), *sides):
        super().__init__(sides, color, True)
        self.__radius = self.get_sides()[0] / (2 * 3.1415)

    def get_square(self):
        return (f'Площадь круга:{3.1415 * self.__radius ** 2}'
                f'\nРадиус:{self.__radius}')


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color=(), *sides):
        super().__init__(sides, color, True)

    def get_square(self):
        p = self.__len__() / 2
        return f'Площадь треугольника:{(p * (p - self.get_sides()[0])
                                        * (p - self.get_sides()[1])
                                        * (p - self.get_sides()[2]))
                                       ** (1 / 2)}'


class Cube(Figure):
    sides_count = 12

    def __init__(self, color=(), *sides):
        super().__init__(sides, color)
        self.__len_sides_1(*sides)


    def __len_sides_1(self, *sides):
        if len(sides) == 1:
            for i in range(0, self.sides_count):
                self.get_sides()[i] = sides[0]


    def set_sides(self, *new_sides):
        super().set_sides(new_sides)
        self.__len_sides_1(*new_sides)

    def get_volume(self):
        self.filled = 5
        return f'Объём куба:{self.get_sides()[0] ** 3}'


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
Triangle1 = Triangle((200, 200, 100), 10, 6)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
# print(len(circle1))
# print(circle1.get_sides())
# print(circle1.get_square())
#
# print(Triangle1.get_color())
# print(len(Triangle1))
# print(Triangle1.get_sides())
# print(Triangle1.get_square())
#
# print(cube1.get_color())
# print(len(cube1))
#print(cube1.get_sides())
# print(cube1.get_volume())

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

