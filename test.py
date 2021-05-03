import abc

# represents the product created by the builder.
class building:
    def __init__(self):
        self.buildingName = None
        self.coordinates= None

    def get_buildingName(self):
        return self.buildingName

    def get_coordinates(self):
        return self.coordinates
    
    def set_coordinates(self, coordinates):
        self.coordinates = coordinates

    def set_buildingName(self, buildingName):
        self.buildingName = buildingName

    # def __str__(self):
    #     return '1',2
    def strings(self):
        return self.coordinates,self.buildingName
    
  


# the builder abstraction
class buildingBuilder(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def set_buildingName(self, buildingName):
        pass
    @abc.abstractmethod
    def set_coordinates(self, buildingName):
        pass

    @abc.abstractmethod
    def get_result(self):
        pass
    @abc.abstractmethod
    def get_coordinates(self):
        pass


class buildingBuilderImpl(buildingBuilder):
    def __init__(self):
        self.building = building()

    def set_buildingName(self, buildingName):
        self.building.set_buildingName(buildingName)


    def set_coordinates(self, coordinates):
        self.building.set_coordinates(coordinates)

    def get_result(self):
        return self.building

    def get_coordinates(self):
            return self.building.coordinates()
    

    


class buildingBuildDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.set_buildingName("Red")
        self.builder.set_coordinates('sdfasdfasdf')
        
        return self.builder.get_coordinates()

if __name__ == '__main__':
    builder = buildingBuilderImpl()
    buildingBuildDirector = buildingBuildDirector(builder)
    print(buildingBuildDirector.construct())
    