from collections import Counter
from os import stat

INPUT_DATA = "input.txt"


def extract_element_frequencies(count:Counter):
    c = count.most_common()
    most, least = c[0], c[-1]
    return most[0], least[0]


def convert_rate(binary_elements):
    binary_string = ''.join(binary_elements)
    binary_value = int(binary_string, 2)
    return binary_value


def find_life_support_rating_component(readings, bit_criteria):
    filtered_readings = readings
    for i in range(len(bit_criteria)):
        f = lambda reading: reading[i] == bit_criteria[i]
        filtered_readings = list(filter(f, filtered_readings))
        if len(filtered_readings) == 1:
            return filtered_readings[0]


class DiagnosticsReader():
    def __init__(self, input_data):
        self.diagnostic_readings = self.read_input_data(input_data)
        # find gamma & epsilon ratings
        initial_binary_element_counts = self.find_binary_element_counts(self.diagnostic_readings)
        self.gamma_rating, self.epsilon_rating = map(convert_rate, initial_binary_element_counts)
        self.power_consumption_rate = self.gamma_rating * self.epsilon_rating

        # find life support
        for i in range(len(initial_binary_element_counts)):
            filtered_readings = self.diagnostic_readings

            if len(filtered_readings) == 0:
                pass
        self.oxygen_generator_rating = 0
        self.c02_scrubber_rating = 0
        self.life_support_rating = self.oxygen_generator_rating * self.life_support_rating

    @staticmethod
    def read_input_data(input_data):
        read_data = []

        with open(input_data, "r") as input:
            for reading in input:
                read_data.append(reading.strip())

    def find_binary_element_counts(readings):
        reading_digits = map(list, readings)
        inverted = zip(*reading_digits)
        digit_counts = map(lambda x: Counter(x), inverted)
        digit_frequencies = map(extract_element_frequencies, digit_counts)
        binary_value_elements = zip(*digit_frequencies)
        return binary_value_elements

    def find_life_support_ratings(initial_readings, )







#### original attempt
# diagnostic_readings = []

# with open(INPUT_DATA, "r") as input:
#     for reading in input:
#         diagnostic_readings.append(reading.strip())

# reading_digits = map(list, diagnostic_readings)
# inverted = zip(*reading_digits)
# digit_counts = map(lambda x: Counter(x), inverted)
# digit_frequencies = map(extract_element_frequencies, digit_counts)
# binary_value_elements = zip(*digit_frequencies)
# gamma_rating, epsilon_rating = map(convert_rate, binary_value_elements)

# power_consumption_rate = gamma_rating * epsilon_rating

# # part 2
# swap_element = lambda x: 0 if int(x) == 1 else 1

# reading_digits = list(map(list, diagnostic_readings))
# inverted = list(zip(*reading_digits))
# digit_counts = list(map(lambda x: Counter(x), inverted))
# digit_frequencies = list(map(extract_element_frequencies, digit_counts))
# binary_value_elements = list(zip(*digit_frequencies))

# oxygen_generator_bit_criteria, co2_scrubber_bit_criteria = binary_value_elements

# oxygen_generator_rating = convert_rate(find_life_support_rating_component(diagnostic_readings, oxygen_generator_bit_criteria))
# c02_scrubber_rating = convert_rate(find_life_support_rating_component(diagnostic_readings, oxygen_generator_bit_criteria))

# life_support_rating = oxygen_generator_rating * c02_scrubber_rating


## part 2
def my_function(readings, position, highest_value, tiebreaker):
    filtered = map(lambda x: x[position], readings)
    counts = Counter(filtered).most_common()
    most_common = counts[0]
    least_common = counts[-1]
    if most_common[1] == least_common[1]:
        filter_value = tiebreaker
    elif highest_value:
        filter_value = most_common[0]
    else:
        filter_value = least_common[0]
    return list(filter(lambda x: x[position] == filter_value, readings))

initial_readings = []

with open(INPUT_DATA, "r") as input:
    for reading in input:
        initial_readings.append(reading.strip())

reading_length = len(initial_readings[0])
filtered_readings = initial_readings
for i in range(reading_length):
    filtered_readings = my_function(filtered_readings, i, True, '1')
    if len(filtered_readings) == 1:
        oxygen_generator_rating = int(filtered_readings[0], 2)
        break

oxygen_generator_rating

filtered_readings = initial_readings

for i in range(reading_length):
    filtered_readings = my_function(filtered_readings, i, False, '0')
    if len(filtered_readings) == 1:
        c02_scrubber_rating = int(filtered_readings[0], 2)
        break

life_support_rating = oxygen_generator_rating * c02_scrubber_rating
life_support_rating
