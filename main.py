DIGITS = [
    '0',
    '1', 
    '2', 
    '3', 
    '4', 
    '5', 
    '6', 
    '7', 
    '8', 
    '9'
]

ALPHABET = [
    '0',
    '1', 
    '2', 
    '3', 
    '4', 
    '5', 
    '6', 
    '7', 
    '8', 
    '9',
    "+",
    "-",
    ".",
    "e"
]

STATES = [
    'e0',
    'e1',
    'e2',
    'e3',
    'e4',
    'e5',
    'e6',
    'e7'
]

FINAL_STATES = [
    STATES[1],
    STATES[4],
    STATES[6],
]

transitions = {
    (STATES[0], '+'): STATES[2],
    (STATES[0], '-'): STATES[2],
    (STATES[1], 'e'): STATES[5],
    (STATES[1], '.'): STATES[3],
    (STATES[4], 'e'): STATES[5],
    (STATES[5], '+'): STATES[7],
    (STATES[5], '-'): STATES[7],
}
for d in DIGITS:
    transitions[STATES[0], d] = STATES[1]
    transitions[STATES[1], d] = STATES[1]
    transitions[STATES[2], d] = STATES[1]
    transitions[STATES[3], d] = STATES[4]
    transitions[STATES[4], d] = STATES[4]
    transitions[STATES[5], d] = STATES[6]
    transitions[STATES[6], d] = STATES[6]
    transitions[STATES[7], d] = STATES[6]

def recognizeNumber(number: str):
    number_chars = [c for c in number]

    current_state = STATES[0]

    for char in number_chars:
        if not findInAlpha(char):
            return False

        current_state = transitions[current_state, char]

    for state in FINAL_STATES:
        if current_state == state:
            return True
    return False

def findInAlpha(char):
    for c in ALPHABET:
        if char == c:
            return True
    return False

print(recognizeNumber('2.123e445'))