"""For the given ‘Location’ class (on the next slide), write the following overloaded methods:
Less than or equal to (__le__ )
      - This method should return True if x and y values of the first object are less than or equal to 
         the x and y values of the second object respectively.
      - Otherwise, it should return False
Greater than or equal to (__ge__)
      - This method should return True if x and y values of the first object are greater than or equal to 
         the x and y values of the second object respectively.
      - Otherwise, it should return False
Equal to (__eq__)
	      - This method should return True if x and y values of the first object are equal to 
                 the x and y values of the second object respectively.
      	      - Otherwise, it should return False
"""
class Location():
    def __init__(self,x = 0,y=0,):
        self.x = x
        self.y = y
    def __le__(self,other):
        return (self.x and self.y) <= (other.x and other.y)
    def __ge__(self,other):
        return (self.x and self.y) >= (other.x and other.y)
    def __eq__(self,other):
        return (self.x and self.y) == (other.x and other.y)
Position = Location(3,4)
Other_Position = Location(5,8)
print(Position == Other_Position)
print(Position <= Other_Position)
print(Position >= Other_Position)