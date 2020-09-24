def guest_list(guests):
	for guest in guests:
		  print('{} is {} years old and works as {}.'.format(guest[0],guest[1],guest[2]))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

# format methodology combined with tuple functionailty
