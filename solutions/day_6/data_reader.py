from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataReader():
        input_path: Path
        
        def read_input(self) -> list[str]:
                rows : list[str] = self._read_file()
                return self._structure_input(rows)


        def _read_file(self) -> list[str]:
                with open(self.input_path, 'r') as file:
                        return [r.strip() for r in file.read().strip().split('\n')]

        def _structure_input(self, input_rows: list[str]):
                return [r.split() for r in input_rows]


        def read_input_cephalopod(self):

                #Cephalopod_numbers in machine readable format
                #Structure: [groups[numbers]]
                cephalopod_numbers : list[int] = list()

                #Operators
                operators : list[str] = []

                with open(self.input_path, 'r') as file:
                        rows = file.read().split('\n')
                        operators = rows.pop(-1).split()
                        
                        for row in rows:
                                if not cephalopod_numbers:
                                        cephalopod_numbers = [0 for i in row]

                                for i in range(len(row)):
                                        char = row[i]

                                        if char.isnumeric():
                                                #increase significance of existing numbers
                                                cephalopod_numbers[i] =  cephalopod_numbers[i] * 10 + int(char)

                #Group numbers into respective problem
                cephalopod_numbers_grouped = list()
                nbr_group = list()

                #Only numbers which equals 0 have been produced by a column of blank spaces. Exactly what indicates a new group.
                cephalopod_numbers.append(0) #Ensure last group is closed according to rule
                for nbr in cephalopod_numbers:
                        
                        if nbr == 0:
                                cephalopod_numbers_grouped.append(nbr_group)
                                nbr_group = list() #Reset the group
                        else:
                                nbr_group.append(nbr)

                #Sanity check
                assert len(cephalopod_numbers_grouped) == len(operators)

                return cephalopod_numbers_grouped, operators


                                        

