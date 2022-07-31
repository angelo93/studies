# Michael Navarro - Program #3

#--------------- Variables ------------------#
soccer_players = []
basketball_players = []

#--------------- Helper Functions ------------------#
def sort_players(player_list):
    '''Prints out a given player list by highest score to lowest score.'''

    while player_list:
        temp_index = 0
        high_score = 0
        best_player = []

        for player in player_list:
            if int(player["score"]) >= high_score:
                high_score = int(player["score"])
                best_player = [player["name"], player["score"]]
                best_player_index = temp_index
            temp_index += 1

        print(best_player[0].title(), "-", best_player[1])  # Reuiqrement #10
        player_list.pop(best_player_index)

def get_players(soccer = True):
    '''Creates and returns a list of dictionaries comprised of a player name and their career scores.
        If soccer is set to False, then it is assumed basketball player info will be supplied.'''

    count = 0 #counter to limit amount of entries
    players = []

    while count < 3:
        not_int = True  # Used as an except case when checking if score input is a number.

        if soccer:
            player = input('Please provide the name of a soccer player: ').lower()  # Requirement #3
            score = input(f'Please provide the number of career goals for {player.title()}: ')  # Requirement #4
        else: 
            player = input('Please provide the name of a basketball player: ').lower()  # Requirement #7
            score = input(f'Please provide the number of career points for {player.title()}: ') #Requirement #8

        # Check that input is a number
        while not_int:
            try:
                int(score)
                not_int = False
            except:
                score = input('Please provide a number: ')

        players.append({"name": player, "score": score})
        count += 1

        print("")

    return players

#--------------- Requirement 1 ------------------#
# Output a header in the console: “This is Program03 - <yournamehere>”
print('Requirement #1\n')
print('This is Program03 - Michael Navarro')

#--------------- Requirement 2 ------------------#
# Print “This program records goals for soccer players and points for basketball players.”
print('\nRequirement #2\n')
print('This program records goals for soccer players and points for basketball players.')

#--------------- Requirement 3 & 4 ------------------#
# 3. Ask user to enter three names of soccer players.
# 4. Ask user to enter the number of career goals for each of the soccer players.
print('\nRequirement #3 & #4\n')
soccer_players = get_players()

#--------------- Requirement 5 & 6 ------------------#
# 5. Use selection (decision) logic programming structures to determine the order of goals.
# 6. Output a message with the name of the soccer player and the number of goals in sorted order.
print('\nRequirement #5 & #6\n')
sort_players(soccer_players)

print("")

#--------------- Requirement 7 & 8 ------------------#
# 7. Ask user to enter three names of basketball players.
# 8. Ask user to enter career points for each of the basketball players.
print('\nRequirement #7 & #8\n')
basketball_players = get_players(False)

#--------------- Requirement 9 & 10 ------------------#
# 9. Use selection (decision) logic programming structures to determine the winner by the highest number of career points.
# 10. Output a message with the name of the basketball players and the number of career points in sorted order.
print('\nRequirement #9 & #10\n')
sort_players(basketball_players)

#--------------- Requirement 11 ------------------#
# Print a statement explaining your experiences with Program03.
print('\nRequirement #11\n')
print('''After reading the program requirements I immediately knew I would have to keep my code DRY and make most of the logic either loops or functions.
This caused me to have to think about how exactly I was going to store the information so I could manipulate it as need be.
Ultimately, I decided on a list of dictionaries. My reasoning being that I wanted to easily traverse the list of players and have direct access to the required info
for the sorting logic. I know this may not be the simplest or best solution, but it worked wonderfully for what I needed it to do.
However, perhaps the hardest part was planning out how to do the program. This is my first semester working with flowcharts and I'm not used to incorporating them into my workflow.
Normally I break down the problem and implement one feature/step at time until I finish.''')
