import baseballDict as bbdic


class Player:

    def __init__(self, posnum, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.position = bbdic.dic_position[posnum]
        self.posAbbrev = bbdic.dic_posAbbrev[self.position]

    def name(self):
        return self.firstname + " " + self.lastname
