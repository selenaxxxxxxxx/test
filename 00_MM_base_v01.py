#check yes and no
def yes_no(question):
    while True:
        response = input(question).lower()
        if response =="yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes or no")

def not_blank(question):
    while True:
        response = input (question)
        if response =="":
            print("Sorry this can't be blank. Please try again")
        else:
            return response

def num_check(question):
    while True:
        try:
            response=int(input(question))
            return response

        except ValueError:
            print("Plz enter an integer")

MAX_TICKETS =3
tickets_sold=0
#ask user if they want to see the instructions
want_instructions = yes_no("Do you want to read the instructions?")

if want_instructions == "yes":
    print("Instructions go here")


#loop to sell tickets
while tickets_sold<MAX_TICKETS:
    name = not_blank("Enter your name (or 'xxx' to quit)")
    if name=='xxx':
        break
    else:
        age = num_check("Age:")
        if 12 <= age <= 120:
            pass
        elif age < 12:
            print("Sorry you are too young for this movie")
            continue
        else:
            print("Typo, try again")
            continue
        tickets_sold +=1
#comment
if tickets_sold==MAX_TICKETS:
    print("Congrats. You have sold all the tickets")
else:
    print("you have sold "+str(tickets_sold)+" tickets. There is "+str(MAX_TICKETS-tickets_sold)+" remaining.")
    print("You have sold {} ticket/s. There is {} ticket/s remaining".format(tickets_sold, MAX_TICKETS-tickets_sold))