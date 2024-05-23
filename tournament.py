from team import Team
from match import Match
import random

class Tournament:

    teams = []

    def __init__(self, team):

        if team is None:
            return

        if isinstance(team, Team):
            self.teams.append(team)

        elif isinstance(team, list):
            for t in team:
                self.teams.append(t)
    
    def AddTeam(self,team):
        self.teams.append(team)

    def MatchTeams(self):
 
        random.shuffle(self.teams)

        matches = []

        for i in range(int(len(self.teams) / 2)):

            firstTeam = self.teams[i * 2]
            secondTeam = self.teams[i * 2 + 1]

            match = Match(firstTeam, secondTeam)
            
            matches.append(match)
            
        return matches
                        

      