# Program Exam2
# Description: 
#   Simulates a Soccer game
# Author: Michael Navarro 
# Date: 10/26/2020
# Revised: 
#   <revision date> 

# list libraries used

# Declare constants (name in ALL_CAPS)
MULTIPLIER = 29
INCREMENT = 7
LIMIT = 243803
SCORE_PROBABILITY = .005

# Declare Variable types (EVERY variable used)
home_team_score = int()
away_team_score = int()
game_minute = int()
chance_of_score = int()
seed_value = int()

possibilty_of_score = float()

goal_scored = bool()

# The Setup
possibilty_of_score = ( LIMIT * SCORE_PROBABILITY )
home_team_score = 0
away_team_score = 0

goal_scored = False

seed_value = int(input('Please enter an integer to use as the seed value: '))
chance_of_score = seed_value

# Minute by Minute (The Game)
game_minute = 1
while ( game_minute <= 90 ):

    # Check if home team scored.
    chance_of_score = ( ( ( chance_of_score * MULTIPLIER ) + INCREMENT ) % LIMIT )
    if ( chance_of_score < possibilty_of_score ):
        home_team_score += 1
        goal_scored = True
    else:
        pass
    # end if

    # Check if away team scored.
    chance_of_score = ( ( ( chance_of_score * MULTIPLIER ) + INCREMENT ) % LIMIT )
    if ( chance_of_score < possibilty_of_score ):
        away_team_score += 1
        goal_scored = True
    else:
        pass
    #end if

    if ( goal_scored == True ):
        print('\nGooooaaaaaalllll!!!!!')
        print(f'Current game time is... {game_minute}')
        print(f'Home team score: {home_team_score}')
        print(f'Away team score: {away_team_score}')
    else:
        pass
    # end if

    # Prep variables for next game minute
    goal_scored = False
    game_minute += 1
# end while

# Final Tally
print('\nTime! Final scores are...')
print(f'Home team score: {home_team_score}')
print(f'Away team score: {away_team_score}')

# End Program
