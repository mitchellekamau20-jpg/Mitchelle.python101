#bottle blueprint
class Bottle:
    #attributes
    shape ="hourglass"
    #method
    # def bottleDetails():
    #     print(f"")


class Monitor:
#     #attributes
# #   shape ="rectangular"
# #   resoluton ="1000"
# #   size ="large"
# #   yom =2020


#an initialize provoked the monitor
    def __init__(self,shape,resolution,size,yom,color):
        self.shape =shape
        self.resolution = resolution
        self.size = size
        self.yom = yom
        self.color = color

#methods(functions that result in a class)
    def switchOnMonitor(self):
        print("turning on monitor")

    def displayInterface(self):
        print("display OS")
#OBJECTS instaces of classes(a real world thing)
hpMonitor = Monitor("rectangular",1000,21,2000,"gray")
delMonitor = Monitor(shape="oval",resolution=1200,size=34,yom=2000,color="gray")



hpMonitor.switchOnMonitor()
delMonitor.switchOnMonitor()

print(f"===>{hpMonitor.shape}")
print(f"===>{delMonitor.shape}")

"""
-encapsulation
-inheritance
-polymorphism
"""
class vehicle:
    def __init__(self,model,color,isElectric)
        self.model =  model
        self.color = color
        self.isElectric = isElectric
    #method
    def carFeatures(self):
        print(f"this vehicle is of model(self.model)in")

    def startCar(self):
        print(f"starting your (self model) car!")

tesla = vehicle("tesla","space-gray"True)
toyota = vehicle("Toyota","White",False)

class Tuktuk(vehicle):#inhertance
    #attributes
    def __init__(self,model,color,isElectric,numberOfWheels)
        super().__init__(model,color,isElectric)
        self.numberOfWheels = numberOfWheels



