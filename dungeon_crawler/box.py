
from pos2d import Pos2D
class Box:
    def __init__(self, pos1, pos2):
        self.pos1 = pos1
        self.pos2 = pos2
        self.rectangle = []                                     # on va représenter grâce à cette liste les 4 sommets définis par un rectangle

    def relier(self, pos1, pos2):
        if pos1.x <= pos2.x and pos1.y <= pos2.y :              # On conditionne les 4 cas de figures des inégalités
            pos3 = Pos2D(pos1.x,pos2.y)                         # des coodonnées x et y
            pos4 = Pos2D(pos2.x,pos1.y)
            self.rectangle = [[pos1,pos4],[pos3,pos2]]
        elif pos1.x <= pos2.x and pos1.y >= pos2.y :
            pos3 = Pos2D(pos1.x,pos2.y)
            pos4 = Pos2D(pos2.x, pos1.y)
            self.rectangle = [[pos3,pos2],[pos1,pos4]]
        elif pos1.x >= pos2.x and pos1.y <= pos2.y :
            pos3 = Pos2D(pos2.x,pos1.y)
            pos4 = Pos2D(pos1.x,pos2.y)
            self.rectangle = [[pos3, pos1], [pos2, pos4]]
        elif pos1.x >= pos2.x and pos1.y >= pos2.y :
            pos3 = Pos2D(pos2.x,pos1.y)
            pos4 = Pos2D(pos1.x,pos2.y)
            self.rectangle = [[pos2, pos4], [pos3, pos1]]
        return self.rectangle

    def __getitem__(self, pos):                             # on définit get item pour getter plus tard dans le code
        w, h = pos                                          # les positions des 4 points sommets définis par le rectangle
        return self.rectangle[w][h]

    def __get_first(self, pos):
        return self.rectangle[pos]                           # ce getter va uniquement getter le premier element de rectangle
                                                             # qui en général sera une liste


