from data_reader import DataReader
from pathlib import Path
import sys

_INPUT_FILE_PATH : Path = "/".join(['day_5','data','input.txt'])



def _process_input(input_list : list[str]):

        allow_listed_ranges : set[tuple[int,int]] = set()
        values_to_check : list[int] = list()

        for row in input_list:
                #When row represents a range
                if '-' in row:

                        limit_values : list[int]=  [int(x) for x in row.split('-')]
                        allow_listed_ranges.add((limit_values[0],limit_values[1]))


                #When row should be checked
                elif row != '':
                        values_to_check.append(int(row))

        return values_to_check, allow_listed_ranges,

def _optimize_ranges(allow_listed_ranges : set[tuple[int,int]]) -> set[tuple[int,int]]:
        """Takes an input of unsorted, overlapping ranges and creates an ordered deduplicated representation.
        
        Algorithm inspired by this reddit post: https://www.reddit.com/r/adventofcode/comments/1pep1z7/2025_day_5_part_2_algorithm_visualization/
        Implementation is fully mine."""

        #-1 indicates a range start, 1 indicates a range stop
        #Important to also sort such that -1 (start) happens before 1 (end) to extend a range instead of creating a new one when 
        #stop and start of different ranges are at the same location
        sorted_ranges : list[tuple[int,int]]  = sorted([pt for r in allow_listed_ranges for pt in ((r[0],-1), (r[1],1))])

        #Iterate over the sorted ranges.
        #If the counter ever reaches 0 that means the current min and max boundry represents ONE range made up of 1 or more sub ranges
        #from sorted_ranges.
        optimized_ranges : set[tuple[int,int]] = set()
        counter : int = 0

        min : int = None
        max : int = -sys.maxsize

        for range in sorted_ranges:
                counter += range[1]

                #Represents the beginning of a range.
                #Due to sorting - this can never become smaller once set
                if range[1] == -1 and not min:
                        min = range[0]

                #Represents the end of a range
                #Update max boundary
                if range[1] == 1 and range[0] > max:
                        max = range[0]

                #When counter ends on 0
                if counter == 0:
                        optimized_ranges.add((min,max))
                        min : int = None
                        max : int = -sys.maxsize

        return optimized_ranges

def _check_values_in_ranges(values_to_check : list[int], allow_listed_ranges : set[tuple[int,int]]):
        """Final step part 1."""

        nbr_allowed_input : int = 0
        for trg in values_to_check:
                for min,max in allow_listed_ranges:
                        if min <= trg <= max:
                                nbr_allowed_input+= 1
                                break

        print(f"Nbr of fresh ingredients : {nbr_allowed_input}")

def _check_nbr_values_in_ranges(allow_listed_ranges: set[tuple[int,int]]):
        """Final step part 2."""

        nbr_values : int = 0
        for min,max in allow_listed_ranges:
                print(f"Adding {max} - {min} + {1} (boundary)= {max-min + 1}")
                nbr_values+= max - min + 1 #Plus one to include boundary
                        
        print(f"Total Number of unique values: {nbr_values}")


def main():

        #Get input
        data_reader = DataReader(_INPUT_FILE_PATH)
        input_list = data_reader.read_input()

        #Process input
        values_to_check, allow_listed_ranges = _process_input(input_list=input_list)

        #Optimize ranges
        optimized_ranges = _optimize_ranges(allow_listed_ranges)

        #Part 1 final step
        _check_values_in_ranges(values_to_check, optimized_ranges)

        #Part 2 final step
        _check_nbr_values_in_ranges(optimized_ranges)


if __name__ == "__main__":
        main()