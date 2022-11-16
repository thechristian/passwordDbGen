# This was written by christian otoo for your free use.
# You can modify for your use case.

import random
import string



def passGen(passLength, quantity):

    # passLength = the length of password
    # quantity = the quantity of passwords to be generated
   
    passList = []    # a list to hold each generated passwords

    # specifying password character combinations
    lowerC = string.ascii_lowercase
    upperC = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

    # creating long characters of password combinations
    allChars = lowerC + upperC + numbers + symbols


    # create password according to quantity and lenth specified
    counter = 1
    while counter <= quantity:
        temp = random.sample(allChars,passLength)
        password = "".join(temp)
        # print (password)
        passList.append(password)
        counter += 1

    # create password file name using password lenght and quantity
    fileName = str(quantity)+"of"+str(passLength)+".txt"

    # saving all generated passwords into the file
    for i in passList:
        passFile = open(fileName, "a") 
        passFile.write("{}\n".format(i))
        passFile.close()


    # Display process complete notice
    print("                                                  ")
    print("==================================================")
    print("                                                  ")
    print("All passwords generated in your working directory.")
    print("                                                  ")
    print("==================================================")