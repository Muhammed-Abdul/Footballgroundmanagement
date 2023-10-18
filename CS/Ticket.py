import csv

def ticket_book():
    def load_tickets():
        with open('tickets.csv', 'r') as file:
            reader = csv.DictReader(file)
            tickets = list(reader)
        return tickets

    def save_tickets(tickets):
        fieldnames = ['TicketID', 'SeatNumber', 'Price', 'Availability']
        with open('tickets.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(tickets)

    def display_tickets(tickets):
        print("Available Tickets:")
        print("===================")
        for ticket in tickets:
            if 'TicketID' in ticket:
                print(f"Ticket ID: {ticket['TicketID']}")
            if 'SeatNumber' in ticket:
                print(f"Seat Number: {ticket['SeatNumber']}")
            if 'Price' in ticket:
                print(f"Price: {ticket['Price']}")
            if 'Availability' in ticket:
                print(f"Availability: {ticket['Availability']}")
            print("===================")

    def buy_ticket(tickets, ticket_id):
        for ticket in tickets:
            if ticket['TicketID'] == ticket_id and ticket['Availability'] == 'Available':
                ticket['Availability'] = 'Sold'
                save_tickets(tickets)
                print("Ticket purchased successfully!")
                return
        print("Ticket not found or unavailable.")

    def cancel_ticket(tickets, ticket_id):
        for ticket in tickets:
            if ticket['TicketID'] == ticket_id and ticket['Availability'] == 'Sold':
                ticket['Availability'] = 'Available'
                save_tickets(tickets)
                print("Ticket Cancelled successfully!")
                return
        print("Ticket not found or unavailable.")

    def ticketmain():
        tickets = load_tickets()

        while True:
            print("Welcome to the Stadium Ticketing Application!")
            print("1. Display available tickets")
            print("2. Buy a ticket")
            print("3. Cancel a ticket")
            print("4. Exit")
            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                display_tickets(tickets)
            elif choice == '2':
                ticket_id = input("Enter the Ticket ID you want to buy: ")
                buy_ticket(tickets, ticket_id)
            elif choice == '4':
                print("Thank you for using the Stadium Ticketing Application!")
                break
            elif choice == '3':
                ticket_id = input("Enter the Ticket ID you want to Cancel: ")
                cancel_ticket(tickets, ticket_id)
            else:
                print("Invalid choice. Please try again.")

    p = 1
    if p == 1 :
        ticketmain()


def ground_book():
    def load_ground():
        with open('ground.csv', 'r') as file:
            reader = csv.DictReader(file)
            Book = list(reader)
        return Book

    def save_ground(Book):
        fieldnames = ['TimeNo', 'BookingTime', 'Price', 'Availability']
        with open('ground.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(Book)

    def display_ground(Book):
        print("Available Time Slots:")
        print("===================")
        for ele in Book:
            if 'TimeNo' in ele:
                print(f"Time Number: {ele['TimeNo']}")
            if 'BookingTime' in ele:
                print(f"Time Slot: {ele['BookingTime']}")
            if 'Price' in ele:
                print(f"Price: {ele['Price']}")
            if 'Availability' in ele:
                print(f"Availability: {ele['Availability']}")
            print("===================")
    def Book_ground(Book, Time_No):
        for elem in Book:
            if elem['TimeNo'] == Time_No and elem['Availability'] == 'Unbooked':
                elem['Availability'] = 'Booked'
                save_ground(Book)
                print("Ground booked successfully!")
                return
        print("Ticket not found or unavailable.")

    def groundmain():
        Book = load_ground()

        while True:
            print("Welcome to the Stadium Ground Booking Application!")
            print("1. Display available Time Slots")
            print("2. Book For A Time Slot")
            print("3. Exit")
            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                display_ground(Book)
            elif choice == '2':
                Time_No = input("Enter the Time Number you want to buy: ")
                Book_ground(Book, Time_No)
            elif choice == '3':
                print("Thank you for using the Stadium Ticketing Application!")
                break
            else:
                print("Invalid choice. Please try again.")

    if __name__ == "__main__":
        groundmain()

print("WELOME TO THE DUBAI STADIUM APPLICATION")
print("1. BOOK THE GROUND FOR A TIME SLOT")
print("2. BUY TICKETS FOR A SEAT")
print("3. Exit")
choice = input("Enter your choice (1-3):")

while True:
    if choice == '1':
        ground_book()
    if choice == '2':
        ticket_book()
    if choice == '3':
        print("THANK YOU FOR USING OUR STADIUM APPLICATION")
        break
    else:
        print("INVALID RESPONSE")