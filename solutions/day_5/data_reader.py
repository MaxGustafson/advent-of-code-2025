from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataReader():
        input_path: Path
        
        def read_input(self) -> list[str]:
                with open(self.input_path, 'r') as file:
                        return file.read().strip().split('\n')
