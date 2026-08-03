from data_reader import DataReader
from pathlib import Path

_INPUT_FILE_PATH : Path = "/".join(['day_5','data','input.txt'])



def _process_input(input_list : list[str]) -> int:

        allow_listed_ranges : set[tuple[int,int]] = set()
        nbr_allowed_input : int = 0

        for row in input_list:
                #When row represents a range
                if '-' in row:

                        limit_values : list[int]=  [int(x) for x in row.split('-')]
                        allow_listed_ranges.add((limit_values[0],limit_values[1]))


                #When row should be checked
                elif row != '':

                        trg : int = int(row)
                        for min,max in allow_listed_ranges:
                                if min <= trg <= max:
                                        nbr_allowed_input+= 1
                                        break
        return nbr_allowed_input

def main():

        data_reader = DataReader(_INPUT_FILE_PATH)
        input_list = data_reader.read_input()

        nbr_allowed_of_input : int = _process_input(input_list=input_list)

        print(f"Nbr of fresh ingredients : {nbr_allowed_of_input}")


if __name__ == "__main__":
        main()