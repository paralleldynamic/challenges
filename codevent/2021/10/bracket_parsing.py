from functools import reduce

bracket_map = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

syntax_scoring_map = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

autocomplete_scoring_map = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

def check_instruction(instruction):
    bracket_map = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">"
    }
    errors = []
    closing_brackets = []
    corrupted = False
    for bracket in instruction:
        if bracket in bracket_map.keys():
            closing_brackets.append(bracket_map[bracket])
        else:
            expected_closing_bracket = closing_brackets.pop()
            if expected_closing_bracket is None or expected_closing_bracket == bracket:
                continue
            else:
                corrupted = True
                errors.append(bracket)
    if closing_brackets:
        closing_brackets.reverse()
        return corrupted, closing_brackets
    return corrupted, errors

instructions = []
corrupted_instructions = []
other_instructions = []
corruption_errors = []
incompleted = []
autocomplete_reducer = lambda x, y: x * 5 + autocomplete_scoring_map[y]
autocomplete_scores = []

with open("input.txt", "r") as input:
    for row in input:
        r = row.strip()
        instructions.append(r)

for instruction in instructions:
    corrupted, errors = check_instruction(instruction)
    if corrupted:
        corrupted_instructions.append(instruction)
        corruption_errors.extend(errors)
    else:
        completion = "".join(errors)
        autocomplete_score = reduce(autocomplete_reducer, completion, 0)
        autocomplete_scores.append(autocomplete_score)
        other_instructions.append(instruction + completion)

syntax_error_reducer = lambda x, y: x + syntax_scoring_map[y]
syntax_error_score = reduce(syntax_error_reducer, corruption_errors, 0)

middle_score = sorted(autocomplete_scores)[len(autocomplete_scores)//2]


