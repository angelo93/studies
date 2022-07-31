# Program examples
# Description: 
#   trying things out
# Author: Michael Navarro
# Date: <11/01/20>
# Revised: 
#   <revision date> 

# list libraries used

# Declare global constants (name in ALL_CAPS)

def main():

    # Declare Variable types (EVERY variable used in this main program)

    # call the function, passing 12 as an argument
    times_ten(12)

# End Program

# Function times_ten()
# Description:
#   displays the product of the parameter times 10
# Calls:
#   none
# Parameters:
#   quantity    Integer
# Returns:
#   none

# write the function definition line here
def times_ten(base):
    # Declare Local Variable types (NOT parameters)

    # write the statements that do what the description says this function does
    print(f'The product of {base} and 10 is: {base * 10}')
    # Return the return variable, if any
    
# End Function times_ten()

main()