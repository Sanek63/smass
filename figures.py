import math


class Rectangle:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        if x1 < x2:
            self.x1 = x1
            self.x2 = x2
        else:
            self.x1 = x2
            self.x2 = x1

        if y1 < y2:
            self.y1 = y1
            self.y2 = y2
        else:
            self.y1 = y2
            self.y2 = y1

    def in_area(self, x_coordination, y_coordination):
        if self.x1 <= x_coordination <= self.x2 and self.y1 <= y_coordination <= self.y2:

            return True
        else:

            return False


class Circle:
    def __init__(self, x_circle=0, y_circle=0, r_circle=0):
        self.x_circle = x_circle
        self.y_circle = y_circle
        self.r_circle = r_circle

    def in_area(self, x_point, y_point):
        x_pow = math.pow(x_point - self.x_circle, 2)
        y_pow = math.pow(y_point - self.y_circle, 2)
        r_pow = math.pow(self.r_circle, 2)

        if x_pow + y_pow <= r_pow:

            return True
        else:

            return False
