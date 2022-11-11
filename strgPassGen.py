# This was written by christian otoo for your free use.

import random
import string

print('Hello, Welcome to Password generator db!')

# user input for password length
passLength = int(input('\nEnter the length of password >> '))

# user input for the quantity of passwords
quantity = int(input('\nEnter the quantity of passwords to be generated >> '))

# a list to hold each generated passwords
passList = []

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
fileName = str(passLength)+"of"+str(quantity)+".txt"

# saving all generated passwords into the file
for i in passList:
    passFile = open(fileName, "a") 
    passFile.write("{}\n".format(i))
    passFile.close()


# Display process complete notice
print("=============================")

print("All passwords generated in your working directory.")