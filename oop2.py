'''
Question:
Complete the method "getPlayers" in the class "Team" to return a list of players' names in the team sorted by their ranks.
When the program is run, it should print out the following: ['Mike', 'Mary', 'Peter', 'John']
'''

class Team:
    def __init__(self, name, players):
        '''
        This method is the constructor of the class Team
        '''
        self.name = name
        self.players = players


    def addPlayer(self, player):
        '''
        This method adds a player to the team
        '''
        self.players.append(player)


    def getPlayers(self):
        '''
        This method returns a list of players' names sorted by increasing order of their ranks
        '''
        players_names  = []

        # todo: implement your logic here
        
        return players_names


class Player:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank



## Testing

# 0. Create a team
team = Team("Team 1", [])

# 2. creating player objects
player1 = Player("John", 30)
player2 = Player("Mary", 7)
player3 = Player("Mike", 4)
player4 = Player("Peter", 7)

# 3. add players to the team
team.addPlayer(player1)
team.addPlayer(player2)
team.addPlayer(player3)
team.addPlayer(player4)

# 4. get players
print(team.getPlayers())  # should print: ['Mike', 'Mary', 'Peter', 'John']
