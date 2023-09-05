class Seat:
    def __init__(self, seat_num):
        self.seat_num = seat_num
        self.name = ''
        self.paid = 0.0
    def reserve(self, customer_name, amount):
        self.name = customer_name
        self.paid = amount
        print('Reservation successful')
    def cancel_reservation(self):
        self.name = ''
        self.paid = 0.0
        print('Cancellation successful')
    def is_available(self):
        return self.name == ''
    def print_info(self):
        print(f'[Seat {self.seat_num}] Name: {self.name} Paid:{self.paid}')
total_seats = 5
seats = []
for i in range(total_seats):
    seats.append(Seat(i))
option = input('''Enter option
(print/reserve/cancel/exit):''')
while option != 'exit':
    if option == 'print':
        for i in range(total_seats):
            Seat(i).print_info()
    elif option=='reserve':
        seat_num = int(input('''Enter seat
number:'''))

        if seat_num < 0 or seat_num >= total_seats:
            print('Invalid Seat Number!')
            option = input('''Enter option
(print/reserve/cancel/exit):''')
            break
        if Seat(seat_num).is_available:
            name = input('Enter customer name:')
            amount = input('Enter amount paid:')

            Seat(seat_num).reserve(name, amount)
        else:
                print('''The requested seat is not
available. Please try another seat.''')
    elif option == 'cancel':
            seat_num = int(input('Enter seat number'))
            if seat_num < 0 or seat_num >= total_seats:
                print("Invalid Seat Number!")
                Seat(seat_num).cancel_reservation()
            else:
                print('Invalid Input')
option = input('''Enter option
(print/reserve/cancel/exit):''')