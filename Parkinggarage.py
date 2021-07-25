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
    
    def __init__ (self, tickets=[1], parkingSpaces=[1], currentTicket={'Paid': False}):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket

    
    def takeTicket(self):
        del self.tickets[0]
        del self.parkingSpaces[0]
        return self.tickets, self.parkingSpaces
    
    def payforParking(self):
        remainder = 10
        while True:
            user_input = input("Please pay for you parking ticket($10): ")
            ticket_amount_paid = int(user_input)
            remainder -= ticket_amount_paid
            if remainder <= 0:
                self.currentTicket['Paid'] = True
                print("You have paid the full amount")
                break
            else:
                self.currentTicket['Paid'] = False
                print(f'Please pay the remainder: ${remainder}')
               

     
        
    


car1 = ParkingGarage([1,2],[1,2],{})
# print(car1.takeTicket())
car1.payforParking()
