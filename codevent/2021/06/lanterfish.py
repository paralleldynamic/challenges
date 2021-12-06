

def time_passes(f, days):
    fish = f
    counts_on_days = {}
    # fish_on_days = {}
    for i in range(days):
        fish_not_spawning = filter(lambda x: x != 0, fish)
        fish_aged = list(map(lambda x: x - 1, fish_not_spawning))
        new_fish = len(fish) - len(fish_aged)
        fish_aged.extend([6] * new_fish)
        fish_aged.extend([8] * new_fish)
        fish = fish_aged
        # fish_on_days[i] = fish
        counts_on_days[i] = len(fish)
    return counts_on_days

with open("input.txt", "r") as input:
    initial_state = list(map(int, input.readline().split(",")))

schools = {0: 0, 1: 0, 2: 0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
total = len(initial_state)
days = 256
for fish in initial_state:
    schools[fish] += 1
for i in range(days):
    placeholder = schools[0]
    schools[0] = schools[1]
    schools[1] = schools[2]
    schools[2] = schools[3]
    schools[3] = schools[4]
    schools[4] = schools[5]
    schools[5] = schools[6]
    schools[6] = schools[7]
    schools[7] = schools[8]
    schools[6] += placeholder
    schools[8] = placeholder
    total +=  placeholder
