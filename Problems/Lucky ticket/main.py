# Save the input in this variable
ticket = input()

ls_ticket = list(ticket)

# Add up the digits for each half
half1 = int(ls_ticket[0]) + int(ls_ticket[1]) + int(ls_ticket[2])
half2 = int(ls_ticket[3]) + int(ls_ticket[4]) + int(ls_ticket[5])

# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")