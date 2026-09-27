booked_seats = []

TOTAL_SEATS = 10
TICKET_PRICE = 500

print("------ BUS TICKET BOOKING SYSTEM ------")

while True:
    print("\n1.Book Ticket")
    print("2.View Seat Availability")
    print("3.Cancel Ticket")
    print("4.Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        if len(booked_seats) == TOTAL_SEATS:
            print("Bookings Full,try another...")
            continue

        name = input("\nEnter Passenger Name: ")
        age = int(input("Enter Passenger Age: "))

        print("\nAvailable Seats:")

        for seat in range(1, TOTAL_SEATS + 1):
            if seat not in booked_seats:
                print(seat, end=" ")

        print("\n")

        seat_no = int(input("\nEnter Seat Number: "))

        if seat_no >= 1 and seat_no <= TOTAL_SEATS:
            if seat_no not in booked_seats:
                price = TICKET_PRICE
                if age < 12:
                    print("Child Discount Applied")
                    price -= 200
                elif age > 60:
                    print("Senior Citizen Discount Applied")
                    price -= 150
                else:
                    print("No Discount")

                booked_seats.append(seat_no)

                print("\nTicket Booked Successfully")
                print("Passenger Name :", name)
                print("Seat Number    :", seat_no)
                print("Final Ticket Price :", price)

            else:
                print("Seat already booked.")
        else:
            print("Invalid Seat Number.")


    elif choice == 2:
        print("\nAvailable Seats:")

        available = False

        for seat in range(1, TOTAL_SEATS + 1):
            if seat not in booked_seats:
                print(seat, end=" ")
                available = True
        if not available:
            print("No seats available.")

    elif choice == 3:
        cancel_seat = int(input("Enter Seat Number to Cancel: "))
        for seat in booked_seats:
            if seat == cancel_seat:
                booked_seats.remove(cancel_seat)
                print("Ticket Cancelled Successfully.")
                break
        else:
            print("Seat not found.")

    elif choice == 4:
        print("\n Thank You for Using Bus Ticket Booking System. \n")
        break

    else:
        print("Invalid Menu Choice.")
        continue