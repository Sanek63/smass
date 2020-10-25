from figures import Rectangle, Circle
from actions import parse_string


if __name__ == '__main__':
    data = parse_string('bd_data.txt')

    circle = Circle(6, 4, 2)
    rectangle = Rectangle(3, 3, 11, 8)

    circle_value = 0
    rectangle_value = 0

    for item in data['data']:
        x_data = item['x']
        y_data = item['y']
        value = item['value']

        if circle.in_area(x_data, y_data):
            circle_value += value

        if rectangle.in_area(x_data, y_data):
            rectangle_value += value

    print('Circle value = {}'.format(circle_value))
    print('Rectangle value = {}'.format(rectangle_value))
