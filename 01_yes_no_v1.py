#functions go here
def yes_no(question):
    while True:
        response = input(question).lower()
        if response =="yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes or no")




#main routine goes here
while True:
    
    want_instructions= yes_no("Do you want to read the instructions")

    if want_instructions == "yes":
        print("instructions go here")
    elif want_instructions == "no":
        pass
    else:
        print("please answer yes/no")



