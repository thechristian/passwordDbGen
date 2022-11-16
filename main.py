from validate import validate_input
from strgPassGen import passGen


print('Hello, Welcome to Password generator db!')

# user input for password length
input_1 = validate_input('\nEnter the length of password to be generated >> ')

# user input for the quantity of passwords
input_2 = validate_input('\nEnter the quantity of passwords to be generated >> ')

passGen(input_1, input_2)