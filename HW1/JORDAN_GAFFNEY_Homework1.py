import math

class Location:
    #TODO: Implement the Location class according to the given UML class diagram and descriptions
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'({self.x},{self.y})'
class Car:
    #TODO: Implement the Car class according to the given UML class diagram and descriptions
    def __init__(self,name,location,cost):
        self.car_name = name
        self.location = location
        self.cost_per_mile = cost
    def __str__(self):
        return f'[{self.car_name}, {self.location}, {self.cost_per_mile}]'
    def move_to(self, new_x, new_y):
        self.location.x = new_x
        self.location.y = new_y       
class Passenger:
    #TODO: Implement the Passenger class according to the given UML class diagram and descriptions
    def __init__(self, name, location):
        self.passenger_name = name
        self.location = location
    def __str__(self):
        return f'{self.passenger_name},{self.location}'
    def move_to(self, new_x, new_y):
        self.location.x = new_x
        self.location.y = new_y
    
class RideSharingApp:
    #TODO: Implement the RideSharingApp class according to the given UML class diagram and descriptions
    def __init__(self):
        self.cars = []
        self.passengers = []
    def add_car(self,car):
        self.cars.append(car)
    def add_passenger(self, passenger):
        self.passengers.append(passenger) 
    def remove_car(self, car):
        self.cars.remove(car) 
    def remove_passenger(self, passenger):
        self.passengers.remove(passenger) 
    def find_cheapest_car(self, passenger):
        lowest = self.cars[0]
        for x in self.cars:
            if lowest.cost_per_mile > x.cost_per_mile:
                lowest = x
        print(f'Cheapest car for {passenger.passenger_name}: {lowest.car_name}, Cost per mile: {lowest.cost_per_mile}')      
    def find_nearest_car(self, passenger):
        closest = None
        min_distance = float('inf')
        lowest = self.cars[0]
        for x in self.cars:
            distance = math.sqrt((x.location.x - passenger.location.x) ** 2 + (x.location.y - passenger.location.y) ** 2)
            if distance < min_distance:           
                closest = x
            min_distance = distance
        print(f'Nearest car for {passenger.passenger_name}: {closest.car_name}, Cost per mile: {min_distance}')    
#For the remaining code (after this line), no modification is required
print('---------------------Object creation------------------')
location1 = Location(2,1)
location2 = Location(-4,1)
car1 = Car('car1', location1, 00.61)
car2 = Car('car2', location2, 0.50)
print('Car object 1 created:',car1)
print('Car object 2 created:', car2)

location3 = Location(-2,3)
location4 = Location(0,0)
passenger1 = Passenger('passenger1', location3)
passenger2 = Passenger('passenger2', location4)
print('Passenger object 1 created:', passenger1)
print('Passenger object 2 created:', passenger2)

mobileApp = RideSharingApp()
mobileApp.add_car(car1)
mobileApp.add_car(car2)
mobileApp.add_passenger(passenger1)
mobileApp.add_passenger(passenger2)

print('-----------------------Scenario 1---------------------')
mobileApp.find_cheapest_car(passenger1)
mobileApp.find_cheapest_car(passenger2)
mobileApp.find_nearest_car(passenger1)
mobileApp.find_nearest_car(passenger2)

print('-----------------------Scenario 2---------------------')
car1.move_to(0,-5)
passenger1.move_to(0,3)
print('car1\'s location has been updated:',car1)
print('passenger1\'s location has been updated:', passenger1)

mobileApp.find_cheapest_car(passenger1)
mobileApp.find_cheapest_car(passenger2)
mobileApp.find_nearest_car(passenger1)
mobileApp.find_nearest_car(passenger2)

print('-----------------------Scenario 3---------------------')
car3= Car('car3', Location(0,2), 0.3)
mobileApp.add_car(car3)
print('New car added:',car3)
mobileApp.find_cheapest_car(passenger1)
mobileApp.find_cheapest_car(passenger2)
mobileApp.find_nearest_car(passenger1)
mobileApp.find_nearest_car(passenger2)

