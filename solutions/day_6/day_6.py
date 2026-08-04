from data_reader import DataReader
from pathlib import Path
import math 

_PATH : Path = "/".join(['day_6','data','input.txt'])

def _solve_cephalopod_math_problems(input_rows: list[list[str]]):

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

        #Solve problems
        ttl_sum : int = 0

        for i in range(len(operations)):
            if operations[i] == '+':
                ttl_sum += sum(numbers[i])

            elif operations[i] == '*':
                ttl_sum+= math.prod(numbers[i])

            else:
                raise(ValueError, "Unhandled operator!")

        return ttl_sum
                    

def main():
        data_reader : DataReader = DataReader(_PATH)

        input_rows : list[list[str]] = data_reader.read_input()

        total_sum: int = _solve_cephalopod_math_problems(input_rows=input_rows)
        print(f"The total sum of the maths problems are : {total_sum}")


if __name__ == "__main__":
        main()