INPUT_DATA = 'input.txt'

depth_measurements = []

with open(INPUT_DATA, 'r') as measurements:
    for measurement in measurements:
        depth_measurements.append(measurement.strip())

comparison = zip(depth_measurements, depth_measurements[1:])
increases = list(filter(lambda x: x[1] > x[0], comparison))
print(len(increases))
## had an off by 1 error?


### part 2
depth_measurements = []

with open(INPUT_DATA, 'r') as measurements:
    for measurement in measurements:
        depth_measurements.append(int(measurement.strip()))

rolling_sums = list(map(sum, zip(depth_measurements, depth_measurements[1:], depth_measurements[2:])))
# zip(depth_measurements, depth_measurements[1:], depth_measurements[2:])
comparison = zip(rolling_sums, rolling_sums[1:])
increases = list(filter(lambda x: x[1] > x[0], comparison))
print(len(increases))
## gave the correct solution
