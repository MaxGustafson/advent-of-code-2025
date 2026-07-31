from dataclasses import dataclass

from pydantic import BaseModel
from pathlib import Path

_INPUT_FILE_PATH : Path = "/".join(['day_3','data','input.txt'])

@dataclass
class JoltageBank:
        digits : str
        powered_digits : list[int] = None

        @property
        def length(self) -> int:
                return len(self.digits)

        @property
        def max_joltage(self) -> int:
                kept_digits : str = "".join(
                        self.digits[i] for i in range(self.length) if self.powered_digits[i] == 1
                )

                return int(kept_digits)
     
        def calculate_powered_digits(self, nbr_digits : int) -> None:
                """Poweres nbr_digits digits such that when evaluationg digits in digits at positions in powered_digits, the number is maximized"""

                if self.length < nbr_digits :
                        raise ValueError(f"{self.digits} is too short, need atleast {nbr_digits} digits")

                nbr_not_powered : int = self.length - nbr_digits
                print(f"nbr_not_powered = {nbr_not_powered}")
                print(f"nbr_digits = {nbr_digits}")
                print(f"length = {self.length}")
                
                "Initial guess is that all rightmost digits are chosen"
                self.powered_digits = [1 if i >= nbr_not_powered else 0 for i in range(self.length)]
                print(list(self.digits))
                print(list(str(i) for i in self.powered_digits))

                #Every digit we check only needs to verify what is left in the list. As we check digits right in the list, each gets an additional digit to the left to compare against.
                iter : int = 0

                #Consider the placement of every cell only once
                for i in range(nbr_not_powered , self.length, 1):

                        current_value : int = int(self.digits[i])
                        current_index : int = i

                        print("")
                        print(f"************* Checking digit with initial index {current_index} and inital value = {current_value} ******************")

                        #Compare the cell to eligeble unpowered cells. Can we get stronger power?
                        for j in reversed(range(nbr_not_powered + iter)):
                                
                                print(f"Evaluating (index,value) -> src = ({current_index}, {current_value}) and trg = ({j}, {self.digits[j]})")
                                
                                
                                #We cannot jump over another digit
                                if self.powered_digits[j] == 1:
                                        print(f"Digit at {j} already powered. We cannot hope for a better result. Breaking iteration!")
                                        print(self.powered_digits)
                                        break

                                #If we have the same value we need to update to allow another digit to take improve
                                if int(self.digits[j]) >= current_value:
                                        print(f"{self.digits[j]} > {current_value} : updating list")
                                        self.powered_digits[j] = 1
                                        self.powered_digits[current_index] = 0
                                        current_value = int(self.digits[j])
                                        current_index = j 
                                        print(self.powered_digits)
                        iter += 1

class DataReader(BaseModel):
        input_path: Path
        
        #Decorator cause it's fun to lab!
        def count_output(func):
                def wrapper(self, *args, **kwargs) -> tuple[list[str], int]:
                        result = func(self, *args,**kwargs)
                        return result, len(result)
                return wrapper
        
        @count_output
        def read_input(self) -> list[str]:
                with open(self.input_path, 'r') as file:
                        return file.read().strip().split('\n')
                
        
def parse_input() -> tuple[list[str], int]:
       args = {
                "input_path":_INPUT_FILE_PATH
        }
       data_reader = DataReader(**args)
       print(data_reader.model_dump())
       return data_reader.read_input()
       #input_2, metadata_2 = DataReader.read_input(data_reader) Equivalent function call



def process_input(row : str, nbr_digits : int) -> JoltageBank:
        """Initialize JoltageBank and calculate optimal powered digits"""

        if len(row) < nbr_digits :
                raise ValueError(f"{row} is too short, need atleast {nbr_digits} digits")

        joltage_bank = JoltageBank(digits = row)
        joltage_bank.calculate_powered_digits(nbr_digits)

        return joltage_bank

        
    

def main():

        nbr_active_digits : int = 12

        #Read input
        input, row_count = parse_input()
        print(f"Read {row_count} rows from input_file {_INPUT_FILE_PATH}")

        #Process each row/joltage bank
        joltage_banks : list[JoltageBank] = []
        for row in input:
                print(f"Input row: {row}")
                joltage_banks.append(process_input(row, nbr_active_digits))


        print(sum(joltage_bank.max_joltage for joltage_bank in joltage_banks))



if __name__ == "__main__":
        main()
