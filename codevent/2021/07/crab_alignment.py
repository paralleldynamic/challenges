with open("input.txt", "r") as input:
    raw_input = input.readline()
    crab_positions = list(map(int, raw_input.split(",")))

fuel_use_scenarios = []
for position in crab_positions:
    diff = lambda x: abs(x - position)
    fuel_use = list(map(diff, crab_positions))
    fuel_use_scenarios.append(fuel_use)

fuel_use_scenario_sums = list(map(sum, fuel_use_scenarios))
least_fuel = min(fuel_use_scenario_sums)

triangle_progression = lambda x: (x * (x + 1))//2

traingle_progression_fuel_use_scenarios = []
for position in range(max(crab_positions) + 1):
    diff = lambda x: abs(x - position)
    fuel_use_diffs = map(diff, crab_positions)
    triangle_progression_fuel_use = list(map(triangle_progression, fuel_use_diffs))
    traingle_progression_fuel_use_scenarios.append(triangle_progression_fuel_use)


triangle_fuel_use_scenario_sums = list(map(sum, traingle_progression_fuel_use_scenarios))
least_fuel = min(triangle_fuel_use_scenario_sums)
least_fuel
