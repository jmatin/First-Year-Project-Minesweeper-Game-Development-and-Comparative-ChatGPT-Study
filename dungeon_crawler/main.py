import argparse
from renderer import GridRenderer
from box import Box
from grid import Grid
from pos2d import Pos2D
from generation import DungeonGenerator

if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description="Creation of a Donjon")
    parser.add_argument("width", help="display the width of our donjon", type=int)
    parser.add_argument('height', help="display the length of our donjon", type=int)
    parser.add_argument('--rooms', help=" number of chambers in the donjon", default=5, type=int)
    parser.add_argument("--seed ", help="seed used for the Donjon's creation ", default=None)
    parser.add_argument("--minwidth", help="minimal width of eah chamber of the donjon", type=int, default=4)
    parser.add_argument("--maxwidth", help="maximal width of eah chamber of the donjon", type=int, default=8)
    parser.add_argument("--minheight", help="minimal hieght of eah chamber of the donjon", type=int, default=4)
    parser.add_argument("--maxheight", help="maximal height of eah chamber of the donjon", type=int, default=8)
    parser.add_argument("--openings", help=" number of entries/exits of a certain chamber ", type=int,default=2)
    parser.add_argument("--hard", help="tells weither a donjon is based on a labyrinth ", type=bool)
    
    parser.add_argument("--view-radius", help="Rendering distance around the player",  type = int, default=6)
    parser.add_argument("----torch-delay", help="Number of moves between 2 torch decays (default: 7)  ", type=bool)
    parser.add_argument("----bonus-radius-radius", help="Visibility radius augmentation by bonus", type = int, default = 3)
    args = parser.parse_args()
    dungeon = DungeonGenerator(args)
    dungeon.generate()