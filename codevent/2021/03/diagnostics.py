from collections import Counter

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


diagnostic_readings = []

with open(INPUT_DATA, "r") as input:
    for reading in input:
        diagnostic_readings.append(reading.strip())

reading_digits = map(list, diagnostic_readings)
inverted = zip(*reading_digits)
digit_counts = map(lambda x: Counter(x), inverted)
digit_frequencies = map(extract_element_frequencies, digit_counts)
binary_value_elements = zip(*digit_frequencies)
gamma_rating, epsilon_rating = map(convert_rate, binary_value_elements)

power_consumption_rate = gamma_rating * epsilon_rating

# part 2
swap_element = lambda x: 0 if int(x) == 1 else 1

reading_digits = list(map(list, diagnostic_readings))
inverted = list(zip(*reading_digits))
digit_counts = list(map(lambda x: Counter(x), inverted))
digit_frequencies = list(map(extract_element_frequencies, digit_counts))
binary_value_elements = list(zip(*digit_frequencies))

oxygen_generator_bit_criteria, co2_scrubber_bit_criteria = binary_value_elements

oxygen_generator_rating = convert_rate(find_life_support_rating_component(diagnostic_readings, oxygen_generator_bit_criteria))
c02_scrubber_rating = convert_rate(find_life_support_rating_component(diagnostic_readings, oxygen_generator_bit_criteria))

life_support_rating = oxygen_generator_rating * c02_scrubber_rating
