from data_reader import DataReader
from pathlib import Path
import math 

_PATH : Path = "/".join(['day_6','data','input.txt'])

def _structure_cephalopod_math_problems_part_1(input_rows: list[list[str]]):

        #Get array of operations
        operations : list [str] = input_rows[-1]
        numbers : list[list[int]] = []

        #Create matrix to group problems
        numbers = [[] for i in range(len(operations))]

        #Populate matrix
        for i in range(len(input_rows) - 1): #Operations already handled
                row = input_rows[i]

                for j in range(len(row)):
                    numbers[j].append(int(row[j]))

        return numbers, operations

def _solve_cephalopod_math_problems(number_groups : list[list[int]], operators : list[str]):

        #Solve problems
        ttl_sum : int = 0

        for i in range(len(operators)):
            if operators[i] == '+':
                ttl_sum += sum(number_groups[i])

            elif operators[i] == '*':
                ttl_sum+= math.prod(number_groups[i])

            else:
                raise(ValueError, "Unhandled operator!")

        return ttl_sum
                    

def main():
        data_reader : DataReader = DataReader(_PATH)

        input_rows : list[list[str]] = data_reader.read_input()

        numbers, operators = _structure_cephalopod_math_problems_part_1(input_rows=input_rows)
        total_sum: int = _solve_cephalopod_math_problems(numbers, operators)
        print(f"The total sum of the maths problems with part 1 structure is : {total_sum}")

        number_groups, operators = data_reader.read_input_cephalopod()

        total_sum: int = _solve_cephalopod_math_problems(number_groups, operators)
        print(f"The total sum of the maths problems with Cephalopod structure is : {total_sum}")


if __name__ == "__main__":
        main()