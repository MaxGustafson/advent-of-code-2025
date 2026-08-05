from data_reader import DataReader
from pathlib import Path

_PATH : Path = '/'.join(["day_7", "data", 'input_mini.txt'])


def _calculate_number_of_timelines(levels : list[str]):

        #Every other input row holds no information
        levels_curated = [level for i, level in enumerate(levels) if i%2 == 0]

        #Discard start_level row. Solution instead assumes first for with split has one and only one split
        #which is the root node
        start_level = levels_curated.pop(0)

        for level in levels_curated:

                for i,idx in [(i,idx) for i,idx in enumerate(levels) if idx == '^']:
                        ... 
                        #Build node
                        #How to keep track of child nodes being hit?

                        


def _process_levels(levels : list[str]):

        nbr_splits : int = 0
        beam_locations = [False for i in levels[0]]

        #Process start level - Initialize beam at S
        start_level : str = levels.pop(0)
        beam_locations[start_level.index("S")] = True

        #Process rest of the levels
        for level in levels:

                delta_beam_locations : list[bool] = beam_locations.copy()

                for i in [i for i,idx in enumerate(level) if idx == '^' and beam_locations[i]]:

                        if i == 0:
                                delta_beam_locations[1] = True
                                delta_beam_locations[0] = False

                        elif i == len(beam_locations):
                                delta_beam_locations[-1] = True
                                delta_beam_locations[-2] = False       

                        else:
                                delta_beam_locations[i] = False
                                delta_beam_locations[i-1] = True
                                delta_beam_locations[i+1] = True

                        nbr_splits +=1

                #Assign new beam positions
                beam_locations = delta_beam_locations

        return nbr_splits                

def main():

        data_reader : DataReader = DataReader(_PATH)

        levels : list[str] = data_reader.read_input()
        nbr_splits : int = _process_levels(levels.copy())

        print(f"Part 1: nbr_splits : {nbr_splits}")

        _calculate_number_of_timelines(levels)



if __name__ == '__main__':
        main()