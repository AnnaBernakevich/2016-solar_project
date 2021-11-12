# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet
import matplotlib.pyplot as plt


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":
                planet = Planet()
                parse_star_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return objects


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """
    star.R, star.color = float(line.split()[1]), line.split()[2]
    star.m, star.x, star.y, star.Vx, star.Vy = [float(x) for x in line.split()[3:]]
    return

def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    planet.R, planet.color = line.split()[1], line.split()[2]
    planet.m, planet.x, planet.y, planet.Vx, planet.Vy = [float(x) for x in line.split()[3:]]
    return


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            s = str(type(obj).__name__) + " " + str(obj.R) + " " + str(obj.color) + " " + str(obj.m) + " " \
                                              + str(obj.x) + " " + str(obj.y) + " " + str(obj.Vx) + " " + str(obj.Vy) + "\n"
            print(s)
            out_file.write(s)
    return

def save_statisctic_to_file(filename, obj, star, physical_time):
    """Сохраняет данные о космическом объекте в файл.
    Строки должны иметь следующий формат:
    <t> <x> <y> <Vx> <Vy> <X> <Y>
    t - время
    x, y, Vx, Vy - координаты и проекции скорости объекта
    X, Y - координаты звезды, относительно которой вычисляется статистика

    Параметры:

    **filename** — имя входного файла
    **obj** — объект, данные о котором сохраняются
    **star** - звезда, относительно которой вычисляется статистика
    **physical_time** - время
    """
    with open(filename, 'a') as out_file:
        s = str(physical_time) + " " + str(obj.x) + " " + str(obj.y) + " " + str(obj.Vx) + " " + str(obj.Vy) + " " + str(star.x) + " " + str(star.y) + "\n"
        out_file.write(s)
    return

def read_statistics_from_file(filename):
    """
    Считывает статистические данные из файла

    **filename** - файл, содержащий статистические данные о планете
    """
    time = []
    velocity = []
    distance = []
    with open(filename) as input_file:
        for line in input_file:
            time.append(float(line.split()[0]))
            x, y, Vx, Vy, X, Y = [float(x) for x in line.split()[1:]]
            V = (Vx**2 + Vy**2)**(0.5)
            velocity.append(V)
            d = ((x - X)**2 + (y - Y)**2)**(0.5)
            distance.append(d)
    return time, velocity, distance

def visualize_statistics(time, velocity, distance):
    """
    Выводит графики зависимости:
    - модуля скорости планеты от времени
    - расстояния от спутника до звезды от времени
    - модуля скорости от расстояния до звезды

    **time** - массив с значениями времени
    **velocity** - массив с значениями модуля скорости планеты
    """
    plt.subplot(131)
    plt.plot(time, velocity)
    plt.title(r'$V(t)$')

    plt.subplot(132)
    plt.plot(time, distance)
    plt.title(r'$d(t)$')

    plt.subplot(133)
    plt.plot(velocity, distance)
    plt.title(r'$V(d)$')

    plt.show()

if __name__ == "__main__":
    print("This module is not for direct call!")
