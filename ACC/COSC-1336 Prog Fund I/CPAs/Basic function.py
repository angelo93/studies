# Program Basic function
# Description: 
#   Calls a simple function
# Author: Michael Navarro
# Date: 10/28/2020
# Revised: 
#   <revision date> 

# list libraries used

# Declare global constants (name in ALL_CAPS)
PHRASE = "I'm not nervous"

def main():

    # Declare Variable types (EVERY variable used in this main program)

    for num in range(10):
        ten_times(PHRASE)
    #end for

# End Program

# Function ten_times()
# Description:
#   prints a simple string
# Calls:
# Parameters:
#   phrase     string
# Returns:
#   phrase

def ten_times (str_variable):

    # Declare Local Variable types (NOT parameters)
    return print(str_variable)

    # Return the return variable, if any

# End Function ten_times()
main()
