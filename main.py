import time

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def recognizeNumber(number: str):
    # ----------------Number Normalization----------------

    number_formated = number.replace(" ", "")
    number_chars = [c for c in number_formated]

    #-----------------------------------------------------

    state = 0
    isFinal = False

    for char in number_chars:
        if state == 0:
            isFinal = False
            if findInDigits(char):
                state = 1
            elif char == '+' | char == '-':
                state = 2
            else:
                return False
            
        elif state == 1:
            isFinal = True
            if findInDigits(char):
                state = 1
            elif char == '.':
                state = 3
            elif char == 'e':
                state = 5
            else:
                return False
            
        elif state == 2:
            isFinal = False
            if findInDigits(char):
                state = 1
            else:
                return False
            
        elif state == 3:
            isFinal = False
            if findInDigits(char):
                state = 4
            else:
                return False
            
        elif state == 4:
            isFinal = True
            if findInDigits(char):
                state = 4
            elif char == 'e':
                state = 5
            else:
                return False
            
        elif state == 5:
            isFinal = False
            if findInDigits(char):
                state = 6
            elif char == '+' | char == '-':
                state = 7
            else:
                return False
            
        elif state == 6:
            isFinal = True
            if findInDigits(char):
                state = 6
            else:
                return False
            
        elif state == 7:
            isFinal = False
            if findInDigits(char):
                state = 6
            else:
                return False
            
    return isFinal

def findInDigits(char):
    for d in DIGITS:
        if char == d:
            return True
    
    return False

start = time.process_time()

print(recognizeNumber("25"))

end: float = time.process_time()
end = str(end)+"s".replace(" ", "")

print("Process Time: ", end)