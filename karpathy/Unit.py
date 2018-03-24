class Unit:
    count = 0

    def __init__(self, v, d):
        self.value = v
        self.derivative = d
        Unit.count = Unit.count + 1
        self.printll()

    def printll(self):
        print("value=", self.value, "derivative=", self.derivative, "count=", Unit.count)


class AddUnit(Unit):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = self.x + self.y
        self.derivates_wrt_x = 1
        self.derivates_wrt_y = 1


if __name__ == '__main__':
    unit = Unit(1, 2)
    unit2 = Unit(2, 3)
    unit = Unit(2, 3)
    unit = Unit(2, 3)
    unit = Unit(2, 3)
    unit = Unit(2, 3)
