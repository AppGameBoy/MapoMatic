import abc

choices = ['Nigh University Center','Max Chambers Library','Math and Computer Science']

ucoBuildings = {
    'Nigh University Center' : (35.65572618535371, -97.47124943368546),
    "Max Chambers Library" : (35.657965312633785, -97.47373031501483),
    "Math and Computer Science": (35.653997083277126, -97.47312997269954)

}

midDict = {
    "Nigh to Lib W" :(
        (35.65794235634459, -97.47360704924955),
        (35.65794128726414, -97.47331916781197),
        (35.65767540904128, -97.47332989664746),
        (35.65765797436592, -97.47120022274068),
        (35.65658347479419, -97.4712353441628),
        (35.656293440101, -97.47090501606355),
        (35.655598855156136, -97.47102941440974)
    ),
    "Nigh to math W" :( 
        (35.65563899390924, -97.47097476725821),
        (35.65430517303365, -97.47089231449681),
        (35.65439847734943, -97.47301027653971),
        (35.65397860707006, -97.47306131176967)
    ),
    "Math to Lib W" : (
        (35.65397860707006, -97.47306131176967),
        (35.65439847734943, -97.47301027653971),
        (35.65434423565961, -97.4730719261411),
        (35.654684225115155, -97.47312020590076),
        (35.65479755461205, -97.47490119259025),
        (35.658211889572975, -97.47499775926565),
        (35.658160056330466, -97.47430240425761),
        (35.657921622981654, -97.47427688664263),
        (35.65794235634459, -97.47360704924955)
    ),
    "Math to Nigh NW" : (
        (35.65425162157668, -97.47270851296994),
        (35.65436524716877, -97.4727581330868),
        (35.65438540653113, -97.47143192269081)
    ),
    "Math to Lib NW" : (
        (35.65425162157668, -97.47270851296994),
        (35.65435004355568, -97.47307999503826),
        (35.65518257921023, -97.47313363921646),
        (35.65588870214999, -97.47356279265084),
        (35.65649892680413, -97.47348769080808),
        (35.65649892680413, -97.47312827481419),
        (35.65692608130799, -97.47323019877126),
        (35.657069918527384, -97.47349841966225),
        (35.6579634469659, -97.47362716568992)
    ),
    "Lib to Nigh NW" : (
        (35.6579634469659, -97.47362716568992),
        (35.65765398215114, -97.47370226749302),
        (35.65764526481504, -97.47202856913336),
        (35.65650764428815, -97.47193200961262),
        (35.65449416993982, -97.47189018680612),
        (35.654359, -97.471431)
    )
}



print(midDict["Nigh to Lib W"])

class IRouteBuilder (metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def setStart(self, startPoint):
        pass
        
    @abc.abstractmethod
    def setMid(self, startPoint, endPoint, wheelchair):
        pass
    
    @abc.abstractmethod
    def setEnd(self, endPoint):
        pass

    @abc.abstractmethod
    def get_results(self):
        pass

class RouteBuilder (IRouteBuilder):
    def __init__(self):
        self.route = Route()
        
    def setStart(self, startPoint):
        if startPoint is choices[0]:
            self.route.startPoint = ucobuildings["Nigh University Center"]
        elif startPoint == choices[1]:
            self.route.startPoint = ucobuildings["MaxCHambers Library"]
        elif startPoint == choices[2]:
            self.route.startPoint = ucobuildings["Math and Computer Science"]

        return self
        

    def setMid(self, startPoint, endPoint, wheelchair):
        if ((startPoint == choices[0] and endPoint == choices[1]) or (startPoint == choices[1] and endPoint == choices[0])) and wheelchair == True:
            self.route.midPoint = midDict["Nigh to Lib W"]
        elif ((startPoint == choices[1] and endPoint == choices[2]) or (startPoint == choices[2] and endPoint == choices[1])) and wheelchair == True:
            self.route.midPoint = midDict["Math to Lib W"]
        elif ((startPoint == choices[0] and endPoint == choices[2]) or (startPoint == choices[2] and endPoint == choices[0])) and wheelchair == True:
            self.route.midPoint = midDict["Nigh to math W"]
        elif ((startPoint == choices[0] and endPoint == choices[1]) or (startPoint == choices[1] and endPoint == choices[0])) and wheelchair == False:
            self.route.midPoint = midDict["Nigh to Lib NW"]
        elif ((startPoint == choices[1] and endPoint == choices[2]) or (startPoint == choices[2] and endPoint == choices[1])) and wheelchair == False:
            self.route.midPoint = midDict["Math to Lib NW"]
        elif ((startPoint == choices[0] and endPoint == choices[2]) or (startPoint == choices[2] and endPoint == choices[0])) and wheelchair == False:
            self.route.midPoint = midDict["Nigh to math NW"]

        return self
    

    def setEnd(self, endPoint):
        if endPoint == choices[0]:
            self.route.endPoint = ucobuildings["Nigh University Center"]
        elif endPoint == choices[1]:
            self.route.endPoint = ucobuildings["MaxCHambers Library"]
        elif endPoint == choices[2]:
            self.route.endPoint = ucobuildings["Math and Computer Science"]

        return self

    def get_results(self):
        return self.route

class Route:
    def __init__(self):
        self.startPoint = None
        self.midPoint = None
        self.endPoint = None

    def getStartPoint(self):
        return self.startPoint

    def getMidPoint(self):
        return self.midPoint

    def getEndPoint(self):
        return self.endPoint

    def __str__(self):
        return "Start point is: {0} mid points are: {1} end point is; {3} ".format(
            self.startPoint, self.midPoint, self.endPoint
        )

class RouteDirector:
    def __init__(self, builder):
        self.builder = builder

    def generate(startPoint, endPoint, wheel):
        return RouteBuilder()\
            .setStart(startPoint)\
            .setMid(startPoint, endPoint, wheel)\
            .setEnd(endPoint)\
            .get_results()

if __name__ == "__main__":
    builder = RouteBuilder()
    RouteBuildDirector = RouteDirector(builder.setMid("Nigh University Center", "MaxCHambers Library", False))

    print(RouteBuildDirector.generate("Nigh University Center", "MaxCHambers Library", False))