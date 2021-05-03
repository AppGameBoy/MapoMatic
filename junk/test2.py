import abc

# represents the product created by the builder.
class Car:
    def __init__(self):
        self.color = None

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def __str__(self):
        return "Car [color={0}]".format(self.color)


# the builder abstraction
class CarBuilder(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def set_color(self, color):
        pass

    @abc.abstractmethod
    def get_result(self):
        pass


class CarBuilderImpl(CarBuilder):
    def __init__(self):
        self.car = Car()

    def set_color(self, color):
        self.car.set_color(color)

    def get_result(self):
        return self.car


class CarBuildDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.set_color("Red")
        return self.builder.get_result()

if __name__ == '__main__':
    builder = CarBuilderImpl()
    carBuildDirector = CarBuildDirector(builder)
    print(carBuildDirector.construct())