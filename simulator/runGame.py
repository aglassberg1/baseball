import inning
import team

inning_count = 0
inning_half = 1
away_team = team.Yankees()
home_team = team.Mets()
batter = [0, 0]
runs = [0, 0]
hits = [0, 0]
errors = [0, 0]


away_team.print_lineup()
print()
home_team.print_lineup()
print()


def game_over():
    if inning_count >= 9 and inning_half == 1 and runs[0] != runs[1]:
        return True
    elif inning_count >= 9 and inning_half == 0 and runs[1] > runs[0]:
        return True
    else:
        return False


while game_over() == False:
    match inning_half:
        case 0:
            inning_half = 1
            current_inning = inning.Inning(inning_half, inning_count, home_team, away_team, runs[1], runs[0], batter[1])
            current_inning.print_inning()
        case 1:
            inning_count += 1
            inning_half = 0
            current_inning = inning.Inning(inning_half, inning_count, away_team, home_team, runs[0], runs[1], batter[0])
            current_inning.print_inning()
    current_inning.score()
    while current_inning.outs != 3:
        current_inning.sim_play()
    if inning_half == 0:
        runs[0] += current_inning.runs
        hits[0] += current_inning.hits
        errors[1] += current_inning.errors
        batter[0] = current_inning.hitter
    else:
        runs[1] += current_inning.runs
        hits[1] += current_inning.hits
        errors[0] += current_inning.errors
        batter[1] = current_inning.hitter
    current_inning.print_results()
    print()
print("Game Over")
if runs[0] > runs[1]:
    print("Final Score: " + away_team.name + " " + str(runs[0]) + " - " + home_team.name + " " + str(runs[1]))
else:
    print("Final Score: " + home_team.name + " " + str(runs[1]) + " - " + away_team.name + " " + str(runs[0]))
