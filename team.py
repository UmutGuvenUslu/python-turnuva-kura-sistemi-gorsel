

class Team:

    memberCount = 0
    name = None

    def __init__(self, name):
        self.name = name

    def __init__(self, name, memberCount):
        self.name = name
        self.memberCount=memberCount



class Person(Team):
   
    @property
    def memberCount(self):
        return self.memberCount

    @memberCount.setter
    def memberCount(self, memberCount):
        self.memberCount = 1

    def __init__(self, name):
        self.name=name
    
