import player
import pandas as pd


class Team:
    def __init__(self, location, name, roster):
        self.location = location
        self.name = name
        self.lineup = []
        self.roster = roster

    def print_lineup(self):
        count = 1
        print(self.name, "Starting Lineup")
        for x in self.lineup:
            print(str(count) + ". " + x.firstname + " " + x.lastname + " " + x.posAbbrev)
            count = count + 1


class Angels(Team):
    def __init__(self):
        Team.__init__(self, ":Los Angeles", "Angels",
                      pd.read_csv("C:\\Users\\arj2o\\OneDrive\\Documents\\2022 MLB Event Files\\ANA2022.ros",
                                  header=None,
                                  names=['Player ID', 'Last Name', 'First Name', 'Bats', 'Throws', 'Team', 'Position']))


class Diamondbacks(Team):
    def __init__(self):
        Team.__init__(self, "Arizona", "Diamondbacks",
                      pd.read_csv("C:\\Users\\arj2o\\OneDrive\\Documents\\2022 MLB Event Files\\ARI2022.ros",
                                  header=None,
                                  names=['Player ID', 'Last Name', 'First Name', 'Bats', 'Throws', 'Team', 'Position']))


class Braves(Team):
    def __init__(self):
        Team.__init__(self, "Atlanta", "Braves",
                      pd.read_csv("C:\\Users\\arj2o\\OneDrive\\Documents\\2022 MLB Event Files\\ATL2022.ROS",
                                  header=None,
                                  names=['Player ID', 'Last Name', 'First Name', 'Bats', 'Throws', 'Team', 'Position']))


class Orioles(Team):
    def __init__(self):
        Team.__init__(self, "Baltimore", "Orioles",
                      pd.read_csv("C:\\Users\\arj2o\\OneDrive\\Documents\\2022 MLB Event Files\\BAL2022.ROS",
                                  header=None,
                                  names=['Player ID', 'Last Name', 'First Name', 'Bats', 'Throws', 'Team', 'Position']))


class RedSox(Team):
    def __init__(self):
        Team.__init__(self, "Boston", "Red Sox",
                      pd.read_csv("C:\\Users\\arj2o\\OneDrive\\Documents\\2022 MLB Event Files\\BOS2022.ROS",
                                  header=None,
                                  names=['Player ID', 'Last Name', 'First Name', 'Bats', 'Throws', 'Team', 'Position']))


class WhiteSox(Team):
    def __init__(self):
        Team.__init__(self, "Chicago", "White Sox",
                      pd.read_csv("C:\\Users\\arj2o\\OneDrive\\Documents\\2022 MLB Event Files\\CHA2022.ROS",
                                  header=None,
                                  names=['Player ID', 'Last Name', 'First Name', 'Bats', 'Throws', 'Team', 'Position']))


class Cubs(Team):
    def __init__(self):
        Team.__init__(self, "Chicago", "Cubs",
                      pd.read_csv("C:\\Users\\arj2o\\OneDrive\\Documents\\2022 MLB Event Files\\CHN2022.ROS",
                                  header=None,
                                  names=['Player ID', 'Last Name', 'First Name', 'Bats', 'Throws', 'Team', 'Position']))


class Reds(Team):
    def __init__(self):
        Team.__init__(self, "Cincinnati", "Reds",
                      pd.read_csv("C:\\Users\\arj2o\\OneDrive\\Documents\\2022 MLB Event Files\\CIN2022.ROS",
                                  header=None,
                                  names=['Player ID', 'Last Name', 'First Name', 'Bats', 'Throws', 'Team', 'Position']))


class Guardians(Team):
    def __init__(self):
        Team.__init__(self, "Cleveland", "Guardians",
                      pd.read_csv("C:\\Users\\arj2o\\OneDrive\\Documents\\2022 MLB Event Files\\CLE2022.ROS",
                                  header=None,
                                  names=['Player ID', 'Last Name', 'First Name', 'Bats', 'Throws', 'Team', 'Position']))


class Rockies(Team):
    def __init__(self):
        Team.__init__(self, "Colorado", "Rockies",
                      pd.read_csv("C:\\Users\\arj2o\\OneDrive\\Documents\\2022 MLB Event Files\\COL2022.ROS",
                                  header=None,
                                  names=['Player ID', 'Last Name', 'First Name', 'Bats', 'Throws', 'Team', 'Position']))


class Tigers(Team):
    def __init__(self):
        Team.__init__(self, "Detroit", "Tigers",
                      pd.read_csv("C:\\Users\\arj2o\\OneDrive\\Documents\\2022 MLB Event Files\\DET2022.ROS",
                                  header=None,
                                  names=['Player ID', 'Last Name', 'First Name', 'Bats', 'Throws', 'Team', 'Position']))


class Astros(Team):
    def __init__(self):
        Team.__init__(self, "Houston", "Astros",
                      pd.read_csv("C:\\Users\\arj2o\\OneDrive\\Documents\\2022 MLB Event Files\\HOU2022.ROS",
                                  header=None,
                                  names=['Player ID', 'Last Name', 'First Name', 'Bats', 'Throws', 'Team', 'Position']))



class Royals(Team):
    def __init__(self):
        Team.__init__(self, "Kansas City", "Royals",
                      pd.read_csv("C:\\Users\\arj2o\\OneDrive\\Documents\\2022 MLB Event Files\\KCA2022.ROS",
                                  header=None,
                                  names=['Player ID', 'Last Name', 'First Name', 'Bats', 'Throws', 'Team', 'Position']))


class Dodgers(Team):
    def __init__(self):
        Team.__init__(self, "Los Angeles", "Dodgers",
                      pd.read_csv("C:\\Users\\arj2o\\OneDrive\\Documents\\2022 MLB Event Files\\LAN2022.ROS",
                                  header=None,
                                  names=['Player ID', 'Last Name', 'First Name', 'Bats', 'Throws', 'Team', 'Position']))


class Marlins(Team):
    def __init__(self):
        Team.__init__(self, "MIami", "Marlins",
                      pd.read_csv("C:\\Users\\arj2o\\OneDrive\\Documents\\2022 MLB Event Files\\MIA2022.ROS",
                                  header=None,
                                  names=['Player ID', 'Last Name', 'First Name', 'Bats', 'Throws', 'Team', 'Position']))


class Brewers(Team):
    def __init__(self):
        Team.__init__(self, "Milwaukee", "Brewers",
                      pd.read_csv("C:\\Users\\arj2o\\OneDrive\\Documents\\2022 MLB Event Files\\MIL2022.ROS",
                                  header=None,
                                  names=['Player ID', 'Last Name', 'First Name', 'Bats', 'Throws', 'Team', 'Position']))


class Twins(Team):
    def __init__(self):
        Team.__init__(self, "Minnesota", "Twins",
                      pd.read_csv("C:\\Users\\arj2o\\OneDrive\\Documents\\2022 MLB Event Files\\MIN2022.ROS",
                                  header=None,
                                  names=['Player ID', 'Last Name', 'First Name', 'Bats', 'Throws', 'Team', 'Position']))


class Yankees(Team):
    def __init__(self):
        Team.__init__(self, "New York", "Yankees",
                      pd.read_csv("C:\\Users\\arj2o\\OneDrive\\Documents\\2022 MLB Event Files\\NYA2022.ros",
                                  header=None,
                                  names=['Player ID', 'Last Name', 'First Name', 'Bats', 'Throws', 'Team', 'Position']))
        self.pitcher = player.Player(1, "Domingo", "German")
        self.catcher = player.Player(2, "Kyle", "Higashioka")
        self.first_baseman = player.Player(3, "DJ", "LeMahieu")
        self.second_baseman = player.Player(4, "Gleyber", "Torres")
        self.third_baseman = player.Player(5, "Josh", "Donaldson")
        self.shortstop = player.Player(6, "Isiah", "Kiner-Falefa")
        self.left_fielder = player.Player(7, "Aaron", "Hicks")
        self.center_fielder = player.Player(8, "Aaron", "Judge")
        self.right_fielder = player.Player(9, "Matt", "Carpenter")
        self.designated_hitter = player.Player(0, "Anthony", "Rizzo")
        self.lineup = [self.first_baseman, self.center_fielder, self.designated_hitter, self.second_baseman,
                       self.right_fielder, self.third_baseman, self.left_fielder, self.shortstop, self.catcher]


class Mets(Team):
    def __init__(self):
        Team.__init__(self, "New York", "Mets",
                      pd.read_csv("C:\\Users\\arj2o\\OneDrive\\Documents\\2022 MLB Event Files\\NYN2022.ros",
                                  header=None,
                                  names=['Player ID', 'Last Name', 'First Name', 'Bats', 'Throws', 'Team', 'Position'])
                      )
        self.pitcher = player.Player(1, "Max", "Scherzer")
        self.catcher = player.Player(2, "Tomas", "Nido")
        self.first_baseman = player.Player(3, "Pete", "Alonso")
        self.second_baseman = player.Player(4, "Jeff", "McNeil")
        self.third_baseman = player.Player(5, "Eduardo", "Escobar")
        self.shortstop = player.Player(6, "Francisco", "Lindor")
        self.left_fielder = player.Player(7, "Mark", "Canha")
        self.center_fielder = player.Player(8, "Brandon", "Nimmo")
        self.right_fielder = player.Player(9, "Starling", "Marte")
        self.designated_hitter = player.Player(0, "Daniel", "Vogelbach")
        self.lineup = [self.center_fielder, self.right_fielder, self.shortstop, self.first_baseman,
                       self.designated_hitter, self.left_fielder, self.second_baseman, self.third_baseman, self.catcher]


class Athletics(Team):
    def __init__(self):
        Team.__init__(self, "Oakland", "Athletics",
                      pd.read_csv("C:\\Users\\arj2o\\OneDrive\\Documents\\2022 MLB Event Files\\OAK2022.ROS",
                                  header=None,
                                  names=['Player ID', 'Last Name', 'First Name', 'Bats', 'Throws', 'Team', 'Position']))


class Phillies(Team):
    def __init__(self):
        Team.__init__(self, "Philadelphia", "Phillies",
                      pd.read_csv("C:\\Users\\arj2o\\OneDrive\\Documents\\2022 MLB Event Files\\PHI2022.ROS",
                                  header=None,
                                  names=['Player ID', 'Last Name', 'First Name', 'Bats', 'Throws', 'Team', 'Position']))


class Pirates(Team):
    def __init__(self):
        Team.__init__(self, "Pittsburgh", "Pirates",
                      pd.read_csv("C:\\Users\\arj2o\\OneDrive\\Documents\\2022 MLB Event Files\\PIT2022.ROS",
                                  header=None,
                                  names=['Player ID', 'Last Name', 'First Name', 'Bats', 'Throws', 'Team', 'Position']))


class Padres(Team):
    def __init__(self):
        Team.__init__(self, "San Diego", "Padres",
                      pd.read_csv("C:\\Users\\arj2o\\OneDrive\\Documents\\2022 MLB Event Files\\SDN2022.ROS",
                                  header=None,
                                  names=['Player ID', 'Last Name', 'First Name', 'Bats', 'Throws', 'Team', 'Position']))


class Mariners(Team):
    def __init__(self):
        Team.__init__(self, "Seattle", "Mariners",
                      pd.read_csv("C:\\Users\\arj2o\\OneDrive\\Documents\\2022 MLB Event Files\\SEA2022.ROS",
                                  header=None,
                                  names=['Player ID', 'Last Name', 'First Name', 'Bats', 'Throws', 'Team', 'Position']))


class Giants(Team):
    def __init__(self):
        Team.__init__(self, "San Francisco", "Giants",
                      pd.read_csv("C:\\Users\\arj2o\\OneDrive\\Documents\\2022 MLB Event Files\\SFN2022.ROS",
                                  header=None,
                                  names=['Player ID', 'Last Name', 'First Name', 'Bats', 'Throws', 'Team', 'Position']))


class Cardinals(Team):
    def __init__(self):
        Team.__init__(self, "St. Louis", "Cardinals",
                      pd.read_csv("C:\\Users\\arj2o\\OneDrive\\Documents\\2022 MLB Event Files\\SLN2022.ROS",
                                  header=None,
                                  names=['Player ID', 'Last Name', 'First Name', 'Bats', 'Throws', 'Team', 'Position']))


class Rays(Team):
    def __init__(self):
        Team.__init__(self, "Tampa Bay", "Rays",
                      pd.read_csv("C:\\Users\\arj2o\\OneDrive\\Documents\\2022 MLB Event Files\\NYA2022.ros",
                                  header=None,
                                  names=['Player ID', 'Last Name', 'First Name', 'Bats', 'Throws', 'Team', 'Position']))


class Rangers(Team):
    def __init__(self):
        Team.__init__(self, "Texas", "Rangers",
                      pd.read_csv("C:\\Users\\arj2o\\OneDrive\\Documents\\2022 MLB Event Files\\TEX2022.ROS",
                                  header=None,
                                  names=['Player ID', 'Last Name', 'First Name', 'Bats', 'Throws', 'Team', 'Position']))


class BlueJays(Team):
    def __init__(self):
        Team.__init__(self, "Toronto", "Blue Jays",
                      pd.read_csv("C:\\Users\\arj2o\\OneDrive\\Documents\\2022 MLB Event Files\\TOR2022.ROS",
                                  header=None,
                                  names=['Player ID', 'Last Name', 'First Name', 'Bats', 'Throws', 'Team', 'Position']))


class Nationals(Team):
    def __init__(self):
        Team.__init__(self, "Washington", "Nationals",
                      pd.read_csv("C:\\Users\\arj2o\\OneDrive\\Documents\\2022 MLB Event Files\\WAS2022.ROS",
                                  header=None,
                                  names=['Player ID', 'Last Name', 'First Name', 'Bats', 'Throws', 'Team', 'Position']))
