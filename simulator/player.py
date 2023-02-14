import baseballDict as bbdic


class Player:

    def __init__(self, posnum, firstname, lastname):            #defines Player object
        self.firstname = firstname
        self.lastname = lastname
        self.position = bbdic.dic_position[posnum]              #sets player position
        self.posAbbrev = bbdic.dic_posAbbrev[self.position]     #sets position abbreviation

    def name(self):                                             #returns name of the player
        return self.firstname + " " + self.lastname             
