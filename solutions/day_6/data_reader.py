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


