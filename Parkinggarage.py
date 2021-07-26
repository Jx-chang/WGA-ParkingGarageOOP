# Your parking gargage class should have the following methods:
# - takeTicket
# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parkingSpaces available by 1
# - payForParking
# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "currentTicket" dictionary key "paid" to True. The key is 'paid' and the value is 'true or false'
# - leaveGarage 
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)


# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary

class ParkingGarage():
    '''
    The ParkingGarage class creates a parking garage with a maximum of 10 parking spaces, represented in the parkingSpaces list.
    Each parked car will appear in the designated location. The tickets list will correspond to the parked car's paid or unpaid ticket.
    '''
    def __init__ (self, tickets=[0,0,0,0,0,0,0,0,0,0], parkingSpaces=[0,0,0,0,0,0,0,0,0,0], currentTicket={'Paid': False}):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket
        self.car_id = {}
    
    def takeTicket(self):
        '''
        Asks user what car they want to park [car1-car10] and where they want to park [1-10]. The dictionary car_id keeps track of
        all parked cars in the garage along with their unique index location for parkingSpaces and paid/unpaid status. Updates the tickets and
        parkingSpaces list.
        '''
        user_car = input("To park and take a ticket, please choose a car: car1, car2,..., car10. \n").title()
        user_parking = int(input("Where would you like to park? [1-10] \n"))
        index = user_parking - 1
        self.car_id[user_car] = [index, 'Unpaid']  # keeps track of all cars in the garage and their parked location (in index) and paid tickets
        self.tickets[index] = 'Unpaid'
        self.parkingSpaces[index] = user_car
        return self.tickets, self.parkingSpaces, self.car_id

    def payforParking(self):
        '''
        Asks user to identify their car, then asks the amount they would like to pay for that car. If the user pays the full amount, then
        update the car_id dictionary to Paid status. If not, ask the user to pay more.
        '''
        remainder = 10
        user_car = input("To pay for parking, please input your car number (car1, car2,..., car10) \n").title()
        while True:
            user_pay = input('Please pay for you parking ticket ($10) [exclude "$"]: \n')
            ticket_amount_paid = int(user_pay)
            remainder -= ticket_amount_paid
            if remainder <= 0:
                self.currentTicket['Paid'] = True
                self.car_id[user_car][1] = 'Paid'
                index = self.car_id[user_car][0]
                self.tickets[index] = 'Paid'
                print(f"You have paid the full amount for {user_car}. You have 15 minutes to leave the parking garage.")
                break
            else:
                self.currentTicket['Paid'] = False
                print(f'Please pay the remainder: ${remainder}')
        print(f'The current parking status is: {self.parkingSpaces}')
        print(f'The current ticket stauts is: {self.tickets}')
               
    def leaveGarage(self):
        '''
        Asks user to identify their car, then checks if the user's car ticket is paid or unpaid. If paid, they can leave. If not,
        run the payforParking method to have the user pay. Show the updated parking garage and ticket status at the end.
        '''
        user_car = input("To leave the garage, please input your car number (car1, car2,..., car10) \n").title()
        if self.car_id[user_car][1] == 'Paid':
            index = self.car_id[user_car][0]
            self.parkingSpaces[index] = 0
            self.tickets[index] = 0
            del self.car_id[user_car]
            print(f"Thank You {user_car}, have a nice day!")
            print(f'The current parking status is: {self.parkingSpaces}')
            print(f'The current ticket stauts is: {self.tickets}')
        else:
            print("You have an unpaid ticket. Please pay for your ticket to proceed.")
            self.payforParking()

        

car = ParkingGarage()
car.takeTicket()
car.takeTicket()
car.takeTicket()
car.payforParking()
car.leaveGarage()