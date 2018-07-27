class Ticket:
    pnr_starting = 1734619274
    pnr = [1734619272, 1734619273, 1734619271]
    no_of_tickets = 3

    file = open('Tickets.txt', 'a')

    def __init__(self, fname, lname, age, gender):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender

    def generate_ticket(self):
        if self.no_of_tickets > 0:
            Ticket.no_of_tickets -= 1
            pnr_no = Ticket.pnr_starting + 1

            self.file.write('Name :' + self.fname + self.lname +
                            '\n Age :' + str(self.age) +
                            '\n Gender:' + self.gender +
                            '\n Pnr no:' + str(pnr_no) + '\n')

            print("Ticket Generated Succefully")

            self.pnr.append(pnr_no)
        else:
            print('No Ticket Available')

    def cancel_ticket(self):
        enter_pnr = int(input('Enter your Pnr Number to Cancel the Ticket'))
        if enter_pnr in self.pnr:

            print('Ticket Cancelled Succesfully')
            Ticket.no_of_tickets += 1

        else:
            print('Invlaid PNR or no such pnr')


'''
t1 = Ticket('Vidit','Shah',21,'M')
print(t1.generate_ticket())
print(Ticket.no_of_tickets)
print(t1.cancel_ticket())
print(Ticket.no_of_tickets)
'''

IRCTC = {'Vidit': 'qwerty', 'Rahul': 'asdfgh'}

username = input("Enter user name")
password = input("enter Password")
if username in IRCTC and password == IRCTC[username]:
    print('Welcome Username: ', username, '\n')
    book_tickets = int(input('How Many Tickets would you like to Book'))

    if book_tickets > Ticket.no_of_tickets:
        print("Only {} Tickets Available".format(Ticket.no_of_tickets))

    else:
        choice = int(input("Enter 1 to book the Ticket \n Enter 2 to Cancel the ticket"))

        if choice == 1:
            for ticket in range(book_tickets):
                fname = input("Enter your Name")
                lname = input("Enter last name")
                gender = input('Enter Gender')
                age = input('Enter age')
                passenger = Ticket(fname, lname, age, gender)
                passenger.generate_ticket()
        if choice == 2:
            Ticket.cancel_ticket()
else:
    print('Invalid Details')








