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
    The parking garage has a maximum of 10 parking spaces, represented as a list. Each item in the list will represent 0 or 1,
    where 0 = empty, 1 = occupied.
    '''
    def __init__ (self, tickets=[0,0,0,0,0,0,0,0,0,0], parkingSpaces=[0,0,0,0,0,0,0,0,0,0], currentTicket={'Paid': False}):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket
        self.parked_list = []
        self.car_id = {}
    
    def takeTicket(self):
        user_car = input("Please choose a car from 1-10")
        user_parking = int(input("Where would you like to park? [1-10]"))
        index = user_parking - 1
        self.car_id[user_car] = index  # unique ID for each parked car, associated with their parked index
        self.parked_list.append(self.car_id)  # keeps track of the current key's index
        self.parked_list[].append('Unpaid')
        self.tickets[index] = 1
        self.parkingSpaces[index] = user_car
        return self.tickets, self.parkingSpaces

        parked_list['car1'].append(index)
        parked_list['car1'].append(paid)

    def payforParking(self):
        remainder = 10
        user_car = input("Please input your car number")
        while True:
            user_pay = input("Please pay for you parking ticket ($10): ")
            ticket_amount_paid = int(user_pay)
            remainder -= ticket_amount_paid
            if remainder <= 0:
                self.currentTicket['Paid'] = True
                print("You have paid the full amount. You have 15 minutes to leave the parking garage.")
                break
            else:
                self.currentTicket['Paid'] = False
                print(f'Please pay the remainder: ${remainder}')
               
    def leaveGarage(self):
        if self.currentTicket == True:
            car_number = input("Please verify your car number [1-10]")
            # if car_number == self.parkingSpaces[]
            print("Thank You, have a nice day!")
        else:
            self.payforParking()
        self.parkingSpaces[index] = 0
        self.tickets[index] = 0
        print(self.parkingSpaces)
        print(self.tickets)
        

car = ParkingGarage()
car.takeTicket()
# car.leaveGarage()