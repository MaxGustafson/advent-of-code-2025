from dataclasses import dataclass
from pathlib import Path

_INPUT_FILE_PATH : Path = "/".join(['day_4','data','input.txt'])

@dataclass
class MapNode():
        id : tuple[int,int]
        is_paper_roll : bool
        nbr_paper_neighbours : int = 0
        movable_threshold : int = 4

        @property
        def is_movable(self) -> bool:
                return self.is_paper_roll and self.nbr_paper_neighbours < self.movable_threshold

@dataclass
class DataReader():
        input_path: Path
        
        def read_input(self) -> list[str]:
                with open(self.input_path, 'r') as file:
                        return file.read().strip().lower().split('\n')



def _compare_nodes(src_node : MapNode, trg_node : MapNode):
        if src_node.is_paper_roll:
                trg_node.nbr_paper_neighbours += 1

        if trg_node.is_paper_roll:
                src_node.nbr_paper_neighbours += 1

def _check_neighbours(row : int, col : int, l_row : int, l_col : int, map_node_matrix : list[list[MapNode]]):
        """Check if the Node has neighbours and update accordingly
        
        row : row location of node
        col : col location of node
        l_row : max length of row
        l_col : max length of col
        map_node_matrix : complete matrix of all nodes"""

        #As we are building the table dynamically and updating both nodes, we only need to check for neighbours which have been previously created
        _DIRECTIONS = [ (-1,-1), (-1,0), (-1,1), ( 0,-1)]

        src_map_node = map_node_matrix[row][col]

        for dr, dc in _DIRECTIONS:
                nr, nc = row + dr, col + dc

                if  0 <= nr < l_row and 0 <= nc < l_col and map_node_matrix[nr][nc]:
                        _compare_nodes(src_map_node, map_node_matrix[nr][nc])

def _evaluate_cell(row : int, col : int, cell : str, map_node_matrix : list[list[MapNode]]):
        map_node_matrix[row][col] = MapNode(id = (row,col), is_paper_roll= (cell == '@'))

def process_input(parsed_input : list[str]):
        """Build map_node_matrix and update4 number of neighbours as you go. Every row should only be processed once!"""

        l_col : int = len(parsed_input)
        l_row : int = len(parsed_input[0]) # assumes all rows are sime sized

        #Final matrix which will be populated with nodes
        map_node_matrix = [[None for j in range(l_row)] for i in range(l_col)]

        for row in range(l_col):

                input_row = parsed_input[row]
                l_row : int = len(input_row)

                for col in range(l_row):

                        #Evaluate cell and add to map_node_matrix
                        cell : str = input_row[col]
                        _evaluate_cell(row, col, cell, map_node_matrix)

                        #Check neighbours
                        _check_neighbours(row,col,l_row,l_col,map_node_matrix)
                        

        return map_node_matrix


def _count_movable_nodes(map_node_matrix : list[list[MapNode]]) -> int:
        return sum(node.is_movable for row in map_node_matrix for node in row)

def _print_movables(map_node_matrix : list[list[MapNode]]) -> None:
        
        print() #empty line
        for row in map_node_matrix:
                row_str = "".join('x' if col.is_movable else '@' if col.is_paper_roll else '.' for col in row)
                print(row_str)

        print()

def main() -> None:

        #Read Input
        data_reader = DataReader(input_path = _INPUT_FILE_PATH)
        parsed_input : list[str] = data_reader.read_input()

        #Process Input
        map_node_matrix = process_input(parsed_input)

        #Examine Output
        _print_movables(map_node_matrix)
        print(_count_movable_nodes(map_node_matrix))


if __name__ == '__main__':
        main()
