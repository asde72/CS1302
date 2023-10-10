class OddNunmberError(Exception):
    def __init__(self, error_messsage):
        self.msg = error_messsage
num = int(input("Please enter a number:"))
if num%2 == 1:
    raise OddNunmberError('This program only accepts even numbers')

print("You have entered ", num)
