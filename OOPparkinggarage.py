#Your assignment for today is to create a parking garage class 
# to get more familiar with Object Oriented Programming(OOP). 

# Your parking garage class should have the following methods:

# - takeTicket
# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parkingSpaces available by 1
# - 
# - payForParking
# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) -> 
#  display a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "currentTicket" dictionary key "paid" to True

# -leaveGarage
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

    def __init__ (self, tickets, parkingSpaces, currentTicket):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket

    def takeTicket(self):
        self.ticketDispensed = self.tickets.pop()
        self.assignedSpace = self.parkingSpaces.pop()
        print(f'Here is ticket {self.ticketDispensed} for space {self.assignedSpace}.')


    def payForParking(self):
        self.charges = input('\nPlease enter your payment amount to check out: ')
        if self.charges != '':
            print('\nThank you! Your ticket is paid and you have 15 minutes to leave.')
            self.currentTicket ['paid'] = True


    def leaveGarage(self):
        if self.currentTicket['paid'] == False:
            self.payForParking()
        elif self.currentTicket['paid'] == True:
            print('Thank You, have a nice day')
            self.tickets.append(self.ticketDispensed)
            self.parkingSpaces.append(self.assignedSpace)


nightOut = ParkingGarage([1, 2, 3], [1, 2, 3], {'paid': False})

print(f'Tickets available before take ticket method used {nightOut.tickets}')  #proof this works
print(f'Spaces available before take ticket method used {nightOut.parkingSpaces}\n')

nightOut.takeTicket()

print(f'\nTickets remaining {nightOut.tickets}')  #proof this works
print(f'Spaces remaining {nightOut.parkingSpaces}')

nightOut.payForParking()
nightOut.leaveGarage()

print(f'\nTickets after leaving {nightOut.tickets}')   #proof this works
print(f'Spaces after leaving {nightOut.parkingSpaces}')
