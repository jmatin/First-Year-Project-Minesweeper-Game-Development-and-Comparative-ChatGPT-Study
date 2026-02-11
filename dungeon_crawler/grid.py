
import random
import copy
from pos2d import Pos2D
from box import Box
from random import shuffle
"─, ┌, ┐, ┬, └, │, ├, ┘, ┴, ┤, ┼"
class Node:
    def __init__(self, up: bool, left: bool, down: bool, right: bool):  # La classe Node est simplement définie
        self.up = up                                                    # par les positions possible vers lequelles
        self.left = left                                                # un noeud peut aller
        self.down = down
        self.right = right
class Grid:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.grid = []
        for w in range(width):                  # on va initialiser notre grille avec des Nodes initialisés à TRUE
            inner = []
            for h in range(height):
                inner.append(Node(up=True, left=True, down=True, right=True))
            self.grid.append(inner)
        for w in range(self.width):
            for h in range(self.height):
                if w == 0 and h == 0:                                   # mat[0][0]     i.e. 1er elem
                    self.grid[w][h] = Node(up=False, left=False, down=True, right=True)
                elif w == 0 and 0 < h <= self.height - 2:               # i.e 1ere colonne sauf dernier elem
                    self.grid[w][h] = Node(up=True, left=False, down=True, right=True)
                elif w == 0 and h == self.height - 1:                   # i.e dernier elem
                    self.grid[w][h] = Node(up=True, left=False, down=False, right=True)
                elif 0 < w <= self.width - 2 and h == 0:                # i.e 1ere ligne sauf dernier elem
                    self.grid[w][h] = Node(up=False, left=True, down=True, right=True)
                elif w == self.width - 1 and h == 0:                    # mat[i-1][0]    i.e dernier elem
                    self.grid[w][h] = Node(up=False, left=True, down=True, right=False)
                elif 0 < w <= self.width - 2 and h == self.height - 1:  # mat[i-2][w-1]  i.e derniere ligne sauf dernier elem
                    self.grid[w][h] = Node(up=True, left=True, down=False, right=True)
                elif w == self.width - 1 and 0 < h <= self.height - 2:  # mat[i-1][j-2]  i.e derniere colonne sauf dernier elem
                    self.grid[w][h] = Node(up=True, left=True, down=True, right=False)
                elif w == self.width - 1 and h == self.height - 1:  # mat[i-1][j-1]      i.e derniere ligne et derniere colonne
                    self.grid[w][h] = Node(up=True, left=True, down=False, right=False)
    def __getitem__(self, pos):
        w, h = pos                          # on va se servor plus loin dans le code get item pour getter les nodes de la grille
        return self.grid[w][h]
    def add_wall(self, pos1: Pos2D, pos2: Pos2D) -> None:
        if pos1.x < pos2.x:                                 # points sur la même ligne
            self.grid[pos1.x][pos1.y].right = False
            self.grid[pos2.x][pos2.y].left = False
        elif pos1.x > pos2.x:
            self.grid[pos1.x][pos1.y].left = False
            self.grid[pos2.x][pos2.y].right = False
        if pos1.y < pos2.y:                                # points sur la même colonne
            self.grid[pos1.x][pos1.y].down = False
            self.grid[pos2.x][pos2.y].up = False
        elif pos1.y > pos2.y:
            self.grid[pos1.x][pos1.y].up = False
            self.grid[pos2.x][pos2.y].down = False
    def remove_wall(self, pos1, pos2) -> None:
        if pos1.x < pos2.x:                                 # points sur la même ligne
            self.grid[pos1.x][pos1.y].right = True
            self.grid[pos2.x][pos2.y].left = True
        elif pos1.x > pos2.x:
            self.grid[pos1.x][pos1.y].left = True
            self.grid[pos2.x][pos2.y].right = True
        if pos1.y < pos2.y:                                   # points sur la même colonne
            self.grid[pos1.x][pos1.y].down = True
            self.grid[pos2.x][pos2.y].up = True
        elif pos1.y > pos2.y:
            self.grid[pos1.x][pos1.y].up = True
            self.grid[pos2.x][pos2.y].down = True
    def isolate_box(self, box ) -> None:
        print(type(box))
        #exemple de rectangle = [[pos2, pos4], [pos3, pos1]] comme explicité dans la classe Box
        rectangle = box.relier(box.pos1,box.pos2)
        for pos in range(rectangle[0][0].x, rectangle[0][1].x+1):                       # mur horizontale sup droit
            self.add_wall(Pos2D(pos,rectangle[0][0].y-1),Pos2D(pos,rectangle[0][0].y ))
        for pos in range(rectangle[0][0].x, rectangle[0][1].x+1) :                      # mur horizontale  inf
            self.add_wall(Pos2D(pos, rectangle[1][0].y), Pos2D(pos,rectangle[1][0].y+1))
        for pos in range(rectangle[0][0].y, rectangle[1][0].y+1) :                      # mur vertical droit
            self.add_wall(Pos2D( rectangle[0][0].x,pos),Pos2D(rectangle[0][0].x-1,pos))
        for pos in range(rectangle[0][1].y, rectangle[1][0].y+1):                       # mur vertical gauche
            self.add_wall(Pos2D(rectangle[0][1].x, pos), Pos2D(rectangle[0][1].x+1, pos))
    def inside_box(self,box):
        """cette fonction rassemble les positions des élément au sein d'une box/piece"""
        piece = []                                  # les positions des elements dans la pièce
        rectangle = box.relier(box.pos1,box.pos2)
        for posy in range(rectangle[0][0].y, rectangle[1][0].y+1):
            for posx in range(rectangle[0][0].x, rectangle[0][1].x+1):
                piece.append(Pos2D(posx, posy))
        return piece
    def red_zone(self,box):
        """cette fonction (bien que malgré que les boxes se trouvent à une distance moins de 2 quand même) a pour but
        de rassembler l'ensemble des positions sur lesquelles on ne peut pas créer une boxe i.e autant celles
        à l'intérieur de la boxe que à une distance de 2 sur les cotés adjcents et une distance de 1
        sur les cotés en diagonale"""

        red_zone = []              # les zones autour de la piece ou l'on ne veut pas creer une autre piece
                                                            # Les éléments dans la box
        rectangle = self.inside_box(box)
                                                            # Les éléments à une distance 2 de la boxe horizontalement:
        for elem in rectangle  :
            red_zone.append(elem)
            if Pos2D(elem.x+3,elem.y) not in red_zone :
                red_zone.append(Pos2D(elem.x+3,elem.y))
            if  Pos2D(elem.x-3,elem.y) not in red_zone :
                red_zone.append(Pos2D(elem.x-3,elem.y))
                                                            # Les éléments à une distance 2 de la boxe verticalement:
        for elem in rectangle :
            if Pos2D(elem.x, elem.y +3) not in red_zone :
                red_zone.append(Pos2D(elem.x , elem.y+ 3))
            if Pos2D(elem.x, elem.y - 3) not in red_zone:
                red_zone.append(Pos2D(elem.x , elem.y- 3))
                                                            # le carré de coté 1 autour de la piece
        for elem in rectangle :
            if Pos2D(elem.x+2,elem.y+2) not in red_zone :
                red_zone.append(Pos2D(elem.x+2,elem.y+2))
            if Pos2D(elem.x-2,elem.y-2) not in red_zone :
                red_zone.append(Pos2D(elem.x-2,elem.y-2))
            if Pos2D(elem.x-2,elem.y+2) not in red_zone  :
                red_zone.append(Pos2D(elem.x-2,elem.y+2))
            if Pos2D(elem.x+2,elem.y-2) not in red_zone :
                red_zone.append(Pos2D(elem.x-2,elem.y-2))
                                                            #enfin on va ajouter les positions en adhérence avec le bord
        for h in range(self.height)  :
                red_zone.append(Pos2D(0,h))
                red_zone.append(Pos2D(self.width-1,h))
        for w in range(self.height):
            red_zone.append(Pos2D(w,0))
            red_zone.append(Pos2D(w,self.height-1))
        return red_zone
    def accessible_neighbours(self, pos: Pos2D):
        adjacent_cases = []
        if self.grid[pos.x][pos.y].up == True:
            adjacent_cases.append(Pos2D(pos.x, (pos.y) - 1))
        if self.grid[pos.x][pos.y].left == True:
            adjacent_cases.append(Pos2D((pos.x) - 1, pos.y))
        if self.grid[pos.x][pos.y].right == True:
            adjacent_cases.append(Pos2D((pos.x) + 1, pos.y))
        if self.grid[pos.x][pos.y].down == True:
            adjacent_cases.append(Pos2D(pos.x, (pos.y) + 1))
        return adjacent_cases
    def recur(self, pos, profondeur,  neighbour_liste):
        """la partie récursive que spanning va appeler"""
        for neighbour in neighbour_liste :
            if neighbour in profondeur :
                self.add_wall(pos,neighbour)     # le mur doit etre ajouter si un voisin est deja dans la liste des sommet adjacents
            else :
                profondeur.append(neighbour)
                neighbour_liste = self.accessible_neighbours(neighbour)
                neighbour_liste.remove(pos)
                random.shuffle(neighbour_liste)
                self.recur(neighbour,profondeur,neighbour_liste)
    def spanning_tree(self):
         graphe = copy.deepcopy(self)
         pos = Pos2D(0,0)
         neighbour_liste = graphe.accessible_neighbours(pos)
         random.shuffle(neighbour_liste)
         profondeur =[]
         profondeur.append(pos)
         graphe.recur(pos,profondeur,neighbour_liste)
         return graphe


