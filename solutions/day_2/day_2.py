import os

def _parse_input(file_path: str):
    
    with open(file_path, 'r') as file:
        data_set_raw = file.read().strip().split(',')

    data_set_cleaned = []
    for row in data_set_raw:
        curent_row = row.split('-')
        data_set_cleaned.append((int(curent_row[0]), int(curent_row[1])))

    return data_set_cleaned

def _get_numbers_in_range(start: int, end: int):
    return list(range(start, end + 1))

#used in part 2
def _is_invalid(id : int, is_debug: bool = False):
    id_str = str(id)

    l = len(id_str) // 2
    if is_debug:
        print(f"_is_invalid: Checking ID: {id_str}")
    is_matching : bool = False

    for i in range(l):
        pattern = id_str[:i+1]
        pattern_len = len(pattern)
        if is_debug:
            print(f"pattern : {pattern}")
        for j in range(0,len(id_str), pattern_len):
            comp_str = id_str[j:j+pattern_len]
            if is_debug:
                print(f"comparing to : {comp_str}")
            if pattern != comp_str:
                if is_debug:
                    print(f"_is_invalid: Mismatch found for {pattern} != {comp_str}")
                is_matching = False
                break
            else:
                is_matching = True
        
        if is_matching:
            print(f"Matching pattern found for patter: {pattern} in string: {id_str} returning True")
            return True
        
    
    if is_debug:
        print(f"No matching patterns found for ID: {id_str} returning False")
    return False

def _traverse_range_part_2(range_list : list[int], is_debug: bool = False):
     local_sum : int = 0

     for nbr in range_list:
        if is_debug:
            print(f"Traversing number: {nbr}")
        if _is_invalid(nbr, is_debug=is_debug):
            local_sum += nbr
     if is_debug:
         print (f"Local sum of invalid numbers: {local_sum}")

     return local_sum

def _handle_ranges_part_2(input_ranges, is_debug: bool = False):
    
    sum_invalid : int = 0
    for range in input_ranges:
        start, end = range
        # Further processing can be done here
        if is_debug:
            print(f"Processing range from {start} to {end}")
        exploded_range = _get_numbers_in_range(start, end)
        if is_debug:
            print(f"Exploded range: {exploded_range}")
        sum_invalid += _traverse_range_part_2(exploded_range, is_debug=is_debug)

    return sum_invalid

#used in part 1
def _is_invalid_half(id : int):
    id_str = str(id)
    left_half = id_str[:len(id_str)//2]
    right_half = id_str[len(id_str)//2:]

    print (f"_is_invalid_half: Checking ID: {id_str} : left {left_half} | right {right_half}")

    if left_half == right_half:
        print(f"_is_invalid_half: Duplicate halves found in ID: {id_str} -> {left_half} == {right_half}")
        return True

def _traverse_range_part_1(range_list : list[int]):
     local_sum : int = 0

     for nbr in range_list:
        
        if len(str(nbr)) % 2 != 0:
            continue
        print(f"Traversing number: {nbr}")
        if _is_invalid_half(nbr):
            local_sum += nbr
     print (f"Local sum of invalid numbers: {local_sum}")

     return local_sum

def _handle_ranges_part_1(input_ranges):
    
    sum_invalid : int = 0
    for range in input_ranges:
        start, end = range
        # Further processing can be done here
        print(f"Processing range from {start} to {end}")
        exploded_range = _get_numbers_in_range(start, end)
        print(f"Exploded range: {exploded_range}")
        sum_invalid += _traverse_range_part_1(exploded_range)

    return sum_invalid
        


if __name__ == "__main__":
    file_name = 'data/input.txt'
    input_file = os.path.join(os.path.dirname(__file__), file_name)

    data_input = _parse_input(input_file)

    #sum_invalid:int = _handle_ranges_part_1(data_input)
    sum_invalid_2:int = _handle_ranges_part_2(data_input, is_debug=False)

    #print (f"Total sum of invalid numbers: {sum_invalid}")
    print (f"Total sum of invalid numbers (part 2): {sum_invalid_2}")