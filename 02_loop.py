from tkinter.font import names

MAX_TICKETS =3

#loop to sell tickets
tickets_sold=0
while tickets_sold<MAX_TICKETS:
    name = input("Please enter your name or 'xxx' to quit")
    if name=='xxx':
        break
    else:
        tickets_sold +=1


if tickets_sold==MAX_TICKETS:
    print("Congrats. You have sold all the tickets")
else:
    print("you have sold "+str(tickets_sold)+" tickets. There is "+str(MAX_TICKETS-tickets_sold)+" remaining.")
    print("You have sold {} ticket/s. There is {} ticket/s remaining".format(tickets_sold, MAX_TICKETS-tickets_sold))