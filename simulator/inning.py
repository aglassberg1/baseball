import random
import baseballDict as bbdic


class Inning:
    def __init__(self, half, number, hitting_team, pitching_team, hitting_score, pitching_score, hitter):
        self.half = half
        self.half_name = bbdic.dic_inning[half]
        self.number = number
        self.hitting_team = hitting_team
        self.pitching_team = pitching_team
        self.hitting_score = hitting_score
        self.pitching_score = pitching_score
        self.hitter = hitter
        self.outs = 0
        self.first_base = False
        self.first_baserunner = None
        self.second_base = False
        self.second_baserunner = None
        self.third_base = False
        self.third_baserunner = None
        self.runs = 0
        self.hits = 0
        self.errors = 0


    def ordinal(self, n: int):
        if 11 <= (n % 100) <= 13:
            suffix = 'th'
        else:
            suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
        return str(n) + suffix

    def print_inning(self):
        print(self.half_name + " " + self.ordinal(self.number))

    def is_over(self):
        if self.outs == 3:
            return True
        else:
            return False

    def score(self):
        if self.pitching_score > self.hitting_score:
            print(self.pitching_team.name + " " + str(self.pitching_score) + " - " + self.hitting_team.name + " "
                  +str(self.hitting_score))
        else:
            print(self.hitting_team.name + " " + str(self.hitting_score) + " - " + self.pitching_team.name + " "
                  + str(self.pitching_score))

    def onebase(self, option):
        runs = 0
        runners_scored = []
        self.hits += 1
        if self.third_base == True:
            self.third_base = False
            runners_scored.append(self.third_baserunner.name())
            self.third_baserunner = None
            runs += 1
        if self.second_base == True:
            self.second_base = False
            self.third_base = True
            self.third_baserunner = self.second_baserunner
            self.second_baserunner = None
        if self.first_base == True:
            self.first_base = False
            self.second_base = True
            self.second_baserunner = self.first_baserunner
            self.first_baserunner = None
        self.first_base = True
        self.first_baserunner = self.hitting_team.lineup[self.hitter]
        if option == 0:
            if runs != 0:
                self.runs += runs
                self.hitting_score += runs
                print(self.hitting_team.lineup[self.hitter].name() + " singled, " + runners_scored[0] + " scores. Still " +
                    str(self.outs) + " out(s).")
                self.score()
            else:
                print(self.hitting_team.lineup[self.hitter].name() + " singled. Still " + str(self.outs) + " out(s).")
        else:
            if runs != 0:
                self.runs += runs
                self.hitting_score += runs
                print(self.hitting_team.lineup[self.hitter].name() + " reached on an error, " + runners_scored[0] +
                      " scores. Still " + str(self.outs) + " out(s).")
                self.score()
            else:
                print(self.hitting_team.lineup[self.hitter].name() + " reached on an error. Still " +
                      str(self.outs) + " out(s).")

    def twobase(self, option):
        runs = 0
        runners_scored = []
        self.hits += 1
        if self.third_base == True:
            self.third_base = False
            runners_scored.append(self.third_baserunner.name())
            self.third_baserunner = None
            runs += 1
        if self.second_base == True:
            self.second_base = False
            runners_scored.append(self.second_baserunner.name())
            self.second_baserunner = None
            runs += 1
        if self.first_base == True:
            self.first_base = False
            self.third_base = True
            self.third_baserunner = self.first_baserunner
            self.first_baserunner = None
        self.second_base = True
        self.second_baserunner = self.hitting_team.lineup[self.hitter]
        if option == 0:
            if runs != 0:
                self.runs += runs
                self.hitting_score += runs
                print(self.hitting_team.lineup[self.hitter].name() + " doubled, " + ", ".join(runners_scored) + " score(s). Still " +
                    str(self.outs) + " out(s).")
                self.score()
            else:
                print(self.hitting_team.lineup[self.hitter].name() + " doubled. Still " + str(self.outs) + " out(s).")
        else:
            if runs != 0:
                self.runs += runs
                self.hitting_score += runs
                print(self.hitting_team.lineup[self.hitter].name() + " reached on an error, " + ", ".join(runners_scored) +
                      " score(s). Still " + str(self.outs) + " out(s).")
                self.score()
            else:
                print(self.hitting_team.lineup[self.hitter].name() + " reached on an error. Still " +
                      str(self.outs) + " out(s).")

    def threebase(self, option):
        runs = 0
        runners_scored = []
        self.hits += 1
        if self.third_base == True:
            self.third_base = False
            runners_scored.append(self.third_baserunner.name())
            self.third_baserunner = None
            runs += 1
        if self.second_base == True:
            self.second_base = False
            runners_scored.append(self.second_baserunner.name())
            self.second_baserunner = None
            runs += 1
        if self.first_base == True:
            self.first_base = False
            runners_scored.append(self.first_baserunner.name())
            self.first_baserunner = None
            runs += 1
        self.third_base = True
        self.third_baserunner = self.hitting_team.lineup[self.hitter]
        if option == 0:
            if runs != 0:
                self.runs += runs
                self.hitting_score += runs
                print(self.hitting_team.lineup[self.hitter].name() + " tripled, " + ", ".join(runners_scored) +
                      " score(s). Still " + str(self.outs) + " out(s).")
                self.score()
            else:
                print(self.hitting_team.lineup[self.hitter].name() + " tripled. Still " + str(self.outs) + " out(s).")
        else:
            if runs != 0:
                self.runs += runs
                self.hitting_score += runs
                print(self.hitting_team.lineup[self.hitter].name() + " reached on an error, " +
                      ", ".join(runners_scored) + " score(s). Still " + str(self.outs) + " out(s).")
                self.score()
            else:
                print(self.hitting_team.lineup[self.hitter].name() + " reached on an error. Still " +
                      str(self.outs) + " out(s).")

    def homerun(self):
        runs = 0
        runners_scored = []
        self.hits += 1
        if self.third_base == True:
            self.third_base = False
            runners_scored.append(self.third_baserunner.name())
            self.third_baserunner = None
            runs += 1
        if self.second_base == True:
            self.second_base = False
            runners_scored.append(self.second_baserunner.name())
            self.second_baserunner = None
            runs += 1
        if self.first_base == True:
            self.first_base = False
            runners_scored.append(self.first_baserunner.name())
            self.first_baserunner = None
            runs += 1
        runs += 1
        self.runs += runs
        self.hitting_score += runs
        print(self.hitting_team.lineup[self.hitter].name() + " homered, " + ", ".join(runners_scored) +
              " score(s). Still " + str(self.outs) + " out(s).")
        self.score()

    def freebase(self, option):
        runs = 0
        runners_scored = []
        if self.first_base == True:
            if self.second_base == True:
                if self.third_base == True:
                    self.third_base = False
                    runners_scored.append(self.third_baserunner.name())
                    self.third_baserunner = None
                    runs += 1
                self.second_base = False
                self.third_base = True
                self.third_baserunner = self.second_baserunner
                self.second_baserunner = None
            self.first_base = False
            self.second_base = True
            self.second_baserunner = self.first_baserunner
            self.first_baserunner = None
        self.first_base = True
        self.first_baserunner = self.hitting_team.lineup[self.hitter]
        if option == 0:
            if runs != 0:
                self.runs += runs
                self.hitting_score += runs
                print(self.hitting_team.lineup[self.hitter].name() + " walked, " + runners_scored[0] + " scores. Still " +
                    str(self.outs) + " out(s).")
                self.score()
            else:
                print(self.hitting_team.lineup[self.hitter].name() + " walked. Still " + str(self.outs) + " out(s).")
        else:
            if runs != 0:
                self.runs += runs
                self.hitting_score += runs
                print(self.hitting_team.lineup[self.hitter].name() + " got hit by a pitch, " + runners_scored[0] +
                      " scores. Still " + str(self.outs) + " out(s).")
                self.score()
            else:
                print(self.hitting_team.lineup[self.hitter].name() + " got hit by a pitch. Still " +
                      str(self.outs) + " out(s).")

    def reachonerror(self, bases):
        if .3991 < bases < .4082:
            self.onebase(1)
        elif .4082 <= bases < .411:
            self.twobase(1)
        else:
            self.threebase(1)
        self.errors += 1

    def out(self, option):
        self.outs += 1
        match option:
            case 0:
                print(self.hitting_team.lineup[self.hitter].name() + " struck out. " + str(self.outs) + " outs(s).")
            case 1:
                print(self.hitting_team.lineup[self.hitter].name() + " grounded out. " + str(self.outs) + " outs(s).")
            case 2:
                print(self.hitting_team.lineup[self.hitter].name() + " flied out. " + str(self.outs) + " outs(s).")

    def sim_play(self):
        outcome = random.random()
        if outcome < .1831:
            self.onebase(0)
        elif .1831 <= outcome < .2391:
            self.twobase(0)
        elif .2391 <= outcome <= .245:
            self.threebase(0)
        elif .245 < outcome < .2797:
            self.homerun()
        elif .2797 <= outcome < .3883:
            self.freebase(0)
        elif .3883 <= outcome <= .3991:
            self.freebase(1)
        elif .3991 < outcome < .4113:
            self.reachonerror(outcome)
        elif .4113 <= outcome <= .6119:
            self.out(0)
        elif .6119 < outcome < .806:
            self.out(1)
        else:
            self.out(2)
        if self.hitter == 8:
            self.hitter = 0
        else:
            self.hitter += 1

    def print_results(self):
        print(str(self.runs) + " run(s), " + str(self.hits) + " hit(s), " + str(self.errors) + " error(s).")
