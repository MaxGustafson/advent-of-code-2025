import os

def _parse_input(file_path: str):
    
    with open(file_path, 'r') as file:
        data_set_raw = file.read().strip().split('\n')
        
    data_set_cleaned = [(row[0], int(row[1:])) for row in data_set_raw]
    return data_set_cleaned

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

    for direction, value in data_input:
        if direction == 'L':
            next_pos = (pos - value) % 100
        elif direction == 'R':
            next_pos = (pos + value) % 100

        delta = next_pos - pos

        if debug:
            print(f"From {pos} to {next_pos}. input: {direction}{value} gives delta: {delta} , total 0s: {nbr_of_0}")

        #Check for crossing 0 directon L
        if direction == 'L' and delta > 0 and pos != 0:
            nbr_of_0 += 1
            print(f"Left crossing +1")

        #Check for crossing 0 directon R
        elif direction == 'R' and delta < 0 and pos != 0:
            nbr_of_0 += 1
            print(f"Right crossing +1")

        #delta == 0 means we landed where we started. Unless we didn't move, this indicates a crossing
        elif delta == 0 and value != 0:
            nbr_of_0 += 1
            print(f"Exact crossing +1")

        #Check for landing on 0
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
    
    result_2 = _eval_rotations_2(data_input, debug = True)
    print(result_2)
    