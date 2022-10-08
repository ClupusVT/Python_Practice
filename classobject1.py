class vehicle:
  def __init__(self, max_speed, mileage,name):
    self.max_speed = max_speed
    self.name = name
    self.mileage  = mileage
  def printname(self):
    print(self.name,self.max_speed,self.mileage)




class Bus(vehicle):
  pass

nissan = Bus(50,3600,"Nissan")
nissan.printname()
