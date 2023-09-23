class Vehicle:
    def __init__(self,make ="", model = "", year = 0):
        self.make = make
        self.model = model
        self.year = year
    def get_info(self):
        print(self.make, self.model, self.year)
    def __lt__(self, other):
        if self.year <  other.year:
            return True
        else:
            return False
class Car(Vehicle):
    def __init__(self,make = "", model = "", year = 0, num_doors = 0):
        Vehicle.__init__(self,make , model , year)
        self.num_doors = num_doors
    def honk(self):
        print("Honk! Honk! From Car")
    def get_info(self):
        print(self.make, self.model, self.year,self.num_doors)
class Motorcycle(Vehicle):
    def __init__(self,make , model  , year, type  ) :
        Vehicle.__init__(self,make , model  , year)
        self.type = type
    def honk(self):
        print("Honk! Honk! From Motorcycle")
    def get_info(self):
        print(self.make, self.model, self.year,self.type)
class Truck(Vehicle):
    def __init__(self,make , model , year,capacity) :
        Vehicle.__init__(self,make, model , year)
        self.capacity = capacity
    def honk(self):
        print("Honk! Honk! From Truck")
    def get_info(self):
        print(self.make, self.model, self.year,self.capacity)
    def __lt__(self, other):
        if self.capacity < other.capacity:
            return True
        else:
            return False
class PickupTruck(Car,Truck):
    def __init__(self,make,model,year, num_doors,capacity,has_cover = False,):
        Car.__init__(self, num_doors,make,model,year)
        Truck.__init__(self, capacity,make,model,year)
        self.has_cover = has_cover
        self.num_doors = num_doors
        self.capacity = capacity
    def honk(self):
        print("Honk! Honk! From Pickup Truck")
       
    def get_info(self):
        print(self.make, self.model, self.year,self.has_cover,self.capacity,self.num_doors)

Cars = Car("Toyota", "Camry", 2020, 4)
Motorcycles = Motorcycle ("Honda", "CBR1000RR", 2021,"Sport")
Trucks = Truck ("Ford", "F-150", 2019,10)
PickupTrucks= PickupTruck("Chevrolet", "Silverado", 2022, 4, 12, True)

Cars.honk()
Motorcycles.honk()
Trucks.honk()
PickupTrucks.honk()

print(Cars.get_info())
print(Motorcycles.get_info())
print(Trucks.get_info())
print(PickupTrucks.get_info())

if Trucks < PickupTrucks:
    print("The PickupTruck has a greater capacity than the Truck.")
else:
    print("The Truck has a greater or equal capacity to the PickupTruck.")