class vehical:
    def __init__(self,name,mspeed,milage):
        self.name=name
        self.mspeed=mspeed
        self.milage=milage
class bus(vehical):
    pass
ob=bus("school volvo",400,3)
print(ob.name,ob.mspeed,ob.milage)