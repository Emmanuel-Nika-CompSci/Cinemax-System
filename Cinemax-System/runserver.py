from models.store import SeatAssignment

print("\n\nWelcome! To Cinema Booking System\n")
restart = "Y"

while True:
	sell_seat = SeatAssignment()
	print("Number of seats available: " + str(sell_seat.count()))
	print("Total sales: shs. ")
	print("\nChoose your preference...\n")
	print("1. Seat Assignment.")
	print("2. Payments (for reserved seat).")
	print("3. Reset Seating Plan.")
	print("4. Exit.")
	option = int(input("\n--> "))

	if option == 1:
		print("\nChoose your preference...\n")
		print("1. Sell a ticket.")
		print("2. Reserve a ticket.")
		print("3. Display seating plan.")
		opt = int(input("\n--> "))

		if opt == 1:
			num_of_seats = int(input("Enter number of seats required: "))
			seat_cat = str(input("Desired seat category: "))

			print("Available seats: ")
			sell_seat.category(seat_cat)

			seat_select = str(input("\n\nChoose seat: "))
			sell_seat.select(seat_select, num_of_seats, seat_cat)
			print("\n")

		elif opt == 2:
			num_of_seats = int(input("Enter number of seats required: "))
			seat_cat = str(input("Desired seat category: "))

			print("Available seats: ")
			sell_seat.category(seat_cat)

			seat_select = str(input("\n\nChoose seat: "))
			sell_seat.reserve_seat(seat_select, num_of_seats, seat_cat)
			print("\n")
			

		elif opt == 3:
			sell_seat.printTable()

		else:
			print("\nIncorrect value entered!\n")
		
	elif option == 2:
		pass

	elif option == 3:
		pass

	elif option == 4:
		pass

	else:
		restart = "Y"
		print("\nIncorrect value entered!\n")