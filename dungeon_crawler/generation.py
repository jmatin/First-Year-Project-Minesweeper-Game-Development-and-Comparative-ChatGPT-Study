import argparse
from renderer import GridRenderer
from box import Box
from grid import Grid
from pos2d import Pos2D
from random import choice


class DungeonGenerator:
    def __init__(self, params: argparse.Namespace) -> None:
        self.params = params
        self.grille = Grid(params.width, params.height)

    def generer_piece(self, n, liste_globale):

        # les arguments
        minwidth_var = self.params.minwidth
        maxwidth_var = self.params.maxwidth
        minheight_var = self.params.minheight
        maxheight_var = self.params.maxheight
        i = 0
        # on veut activer la fonction ssi il y a au moins 1 piece à faire
        if n >= 1:
            while i < n:                    # tant qu'on a pas toute les piece
                bolean = True
                while bolean:               # le bolean va permettre d'arreter la boucle si
                                            # une piece ne correspond pas aux attentes

                    # notre position initiale sur base de la laquelle
                    # on va esayer une construire l'autre coin d'une boxe
                    pos1 = Pos2D(choice([i for i in range(1, self.params.width - 1)]),
                                 choice([i for i in range(1, self.params.height - 1)]))

                    # les autres coin possibles
                    posx_range_minimum_gauche = pos1.x - minwidth_var + 1  # x min
                    posx_range_minimum_droit = pos1.x + minwidth_var - 1
                    posx_range_maximum_gauche = pos1.x - maxwidth_var + 1  # x max
                    posx_range_maximum_droit = pos1.x + maxwidth_var - 1
                    posy_range_minimum_haut = pos1.y - minheight_var + 1  # y min
                    posy_range_minimum_bas = pos1.y + minheight_var - 1
                    posy_range_maximum_haut = pos1.y - maxheight_var + 1  # y max
                    posy_range_maximum_bas = pos1.y + maxwidth_var - 1

                    # la liste des coins respectant les conditions

                    liste_range_adequat_width = [i for i in range(posx_range_maximum_gauche, posx_range_minimum_gauche) if
                                                 1 <= i <= self.params.width - 1 ] + \
                                                [i for i in range(posx_range_minimum_droit, posx_range_maximum_droit) if
                                                1 <= i <= self.params.width - 1]
                    liste_range_adequat_height = [i for i in range(posy_range_maximum_haut, posy_range_minimum_haut) if
                                                1 <= i <= self.params.height - 1] + \
                                                 [i for i in range(posy_range_minimum_bas, posy_range_maximum_bas) if
                                                1 <= i <= self.params.height - 1]
                    # si la liste est vide on peut pas fairede choice
                    if len(liste_range_adequat_width) > 0 and len(liste_range_adequat_height) > 0:
                        pos2 = Pos2D(choice(liste_range_adequat_width), choice(liste_range_adequat_height))
                        bolean = True
                        a = self.grille.inside_box(Box(pos1, pos2))
                        for pos in a:
                            if pos in liste_globale:
                                bolean = False  # si on trouve une position interdite
                            elif pos == a[-1] and bolean:       # si on a traversé toute la liste des
                                # positions interdites et que ok
                                self.grille.isolate_box(Box(pos1, pos2))        # on construit enfin la grille
                                red_zone = self.grille.red_zone(Box(pos1, pos2)) # on ajoute dans la liste de spos
                                #interdites

                                for pos in red_zone:
                                    liste_globale.append(pos)
                                i += 1
                    else:
                        bolean = False

    def generate(self):
        """pas eu le temps de commenter"""
        n = self.params.rooms

        self.generer_piece(n, liste_globale=[])
        A = GridRenderer(self.grille.spanning_tree())
        B = GridRenderer(self.grille.spanning_tree())
        a = A.ret()
        b = B.ret()
        C = GridRenderer(self.grille)
        c = C.print_liste
        dico = dict()
        if not self.params.hard:
            for h in range(A.len()):
                for w in range(A.len2()):
                    if a[h][w] == b[h][w]:
                        c[h][w] = a[h][w]
                    else:
                        c[h][w] = "   "
            dico["grid"] = C.grid
            A.show()
            B.show()
            C.show()
            return dico
        elif self.params.hard:
            dico["grid"] = self.grille.spanning_tree()
            A.show()
            B.show()
            C.show()
            return dico


def fonction_taille_helper(liste, minwidth, posx):

    gauche = posx - minwidth
    droit = posx + minwidth - 3
    if gauche and droit not in liste:  # si il n'y pas la largeur minimal requise
        return False
    elif gauche not in liste and droit in liste:
        liste = liste[droit]
    elif gauche in liste and droit not in liste:
        liste = liste[0]
    return liste


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Creation of a Donjon")
    parser.add_argument("width", help="display the width of our donjon", type=int)
    parser.add_argument('height', help="display the length of our donjon", type=int)
    parser.add_argument('--rooms ', help=" number of chambers in the donjon", default=5, type=int)
    parser.add_argument("--seed ", help="seed used for the Donjon's creation ", default=None)
    parser.add_argument("--minwidth ", help="minimal width of eah chamber of the donjon", type=int, default=4)
    parser.add_argument("--maxwidth  ", help="maximal width of eah chamber of the donjon", type=int, default=8)
    parser.add_argument("--minheight ", help="minimal hieght of eah chamber of the donjon", type=int, default=4)
    parser.add_argument("--maxheight ", help="maximal height of eah chamber of the donjon", type=int, default=8)
    parser.add_argument("--openings ", help=" number of entries/exits of a certain chamber ", type=int, default=2)
    parser.add_argument("--hard", help="tells weither a donjon is based on a labyrinth ", type=bool)
    args = parser.parse_args()
    dungeon = DungeonGenerator(args)
    dungeon.generate()
