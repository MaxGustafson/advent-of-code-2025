import os

def _parse_input(file_path: str):
    
    with open(file_path, 'r') as file:
        data_set_raw = file.read().strip().split('\n')
        
    data_set_cleaned = [(row[0], int(row[1:])) for row in data_set_raw]
    return data_set_cleaned

def _is_sign_change(nbr_1: int, nbr_2: int) -> bool:
    if nbr_1 == 0 or nbr_2 == 0:
        return False
    elif nbr_1 / nbr_2 < 0:
        return True
    else:
        return False

def _eval_rotations_1(data_input, *, debug : bool = False):
    pos : int = 50
    nbr_of_0 : int = 0

    if debug:
        print(f"Starting at pos: {pos}")
    for direction, value in data_input:
        if direction == 'L':
            pos = (pos - value) % 100
        elif direction == 'R':
            pos = (pos + value) % 100

        if pos == 0:
            nbr_of_0 += 1

        if debug:
            print(f"New pos: {pos}, delta: {direction}{value}, total 0s: {nbr_of_0}")
    
    return nbr_of_0

def _eval_rotations_2(data_input, *, debug : bool = False):
    pos : int = 50
    nbr_of_0 : int = 0

    next_pos : int = pos
    next_pos_mod : int

    for direction, value in data_input:
        if direction == 'L':
            next_pos = (pos - value)
        elif direction == 'R':
            next_pos = (pos + value) 

        next_pos_mod = next_pos % 100

        #How many times do we pass 0?
        nbr_of_0 += abs(next_pos) // 100
        print(f"Passed 0s: +{abs(next_pos) // 100}")

        #If we change sign during movement we will pass 0
        if _is_sign_change(pos, next_pos):
            nbr_of_0 += 1
            print(f"Sign change +1") #this counts extra for tiny_input_2

        #If we end on 0 we count one more. If we start on 0, this is handled by value larger than 100
        if next_pos_mod == 0 and pos != 0 and abs(next_pos) != 100:
            nbr_of_0 += 1
            print(f"End on 0 +1")

        if debug:
            print(f"From {pos} to {next_pos_mod}. delta: {direction}{value} gives raw_pos: {next_pos}, total 0s: {nbr_of_0}")

        #update position
        pos = next_pos_mod
 
    return nbr_of_0

def _eval_rotations_2_1(data_input, *, debug : bool = False):
    pos : int = 50
    nbr_of_0 : int = 0

    next_pos : int = pos

    for direction, value in data_input:
        if direction == 'L':
            next_pos = (pos - value) % 100
        elif direction == 'R':
            next_pos = (pos + value) % 100

        delta = next_pos - pos

        if debug:
            print(f"From {pos} to {next_pos}. input: {direction}{value} gives delta: {delta} , total 0s: {nbr_of_0}")

        if direction == 'L' and delta > 0 and pos != 0:
            nbr_of_0 += 1
            print(f"Left crossing +1")

        elif direction == 'R' and delta < 0 and pos != 0:
            nbr_of_0 += 1
            print(f"Right crossing +1")

        elif delta == 0 and value != 0:
            nbr_of_0 += 1
            print(f"Exact crossing +1")

        elif next_pos == 0 and pos != 0:
            nbr_of_0 += 1
            print(f"Landing on 0 +1")

        #We need to account for crossing the 0 mutliple times
        if value >= 100:
            nbr_of_0 += abs(value - 1) // 100
            print(f"Multiple crossing +{abs(value - 1) // 100}")

        #update position
        pos = next_pos 

    return nbr_of_0

if __name__ == "__main__":
    file_name = 'data/input.txt'
    input_file = os.path.join(os.path.dirname(__file__), file_name)

    data_input = _parse_input(input_file)

    result = _eval_rotations_1(data_input, debug = True)
    print(result)
    
    result_2 = _eval_rotations_2_1(data_input, debug = True)
    print(result_2)
    