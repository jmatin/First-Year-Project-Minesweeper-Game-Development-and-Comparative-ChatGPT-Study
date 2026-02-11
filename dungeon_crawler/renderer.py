
from box import Box
from grid import Grid
from pos2d import Pos2D
class GridRenderer :
    def __init__(self,grid):
        self.grid = grid
        self.print_liste = [["   " for largeur in range(2*grid.width+1) ]for hauteur in range(2*grid.height+1)] #on inverse la hauteur et largeur
        for i in range(len(self.print_liste))  :
            for j in range(len(self.print_liste[0])) :
                if j %2 == 0  :
                    self.print_liste[i][j] =" "
        self.print_liste[0][0] =  "┌"                       # les coins
        self.print_liste[0][-1] = "┐"
        self.print_liste[-1][0] = "└"
        self.print_liste[-1][-1] = "┘"
        for w in range(1,2*grid.width+1, 2) :
            self.print_liste[0][w] = "───"                  #les bords horizontaux
            self.print_liste[-1][w]= "───"
        for h in range(1,2*grid.height+1, 2) :
            self.print_liste[h][0] = "│"
            self.print_liste[h][-1] ="│"                    # bord verticaux
        for w in range(grid.width) :
            for h in range(grid.height) :
                node = grid.__getitem__((w,h))
                if node.left == False :                        #les murs DANS la matrice
                    self.print_liste[2*h+1][2*w] = "│"         # seulement verticaux et horizontaux
                if node.down == False:
                    self.print_liste[2*h+2][2*w+1] = "───"
        # une fois que les coins et les murs horizontaux ont été placés
        # on va juste intercaler les autres caractères en fonction de si
        # il y a un espace et de la dispositions des caractères verticaux et horizontaux
        # la main d'oeuvre apparait longue mais moins couteuse que de faire cas par cas
        # pour chaque caractère
        for h in range(len(self.print_liste)) :
            for w in range(len(self.print_liste[0])) :                                              # dans le cas ou il y a encore du vide
                if self.print_liste[h][w]==" ":
                    if 0 < h <= len(self.print_liste) - 2 and 0 < w <= len(self.print_liste[0]) - 2:                       #avant la derniere colonne
                        if self.print_liste[h][w+1] =="───" and self.print_liste[h][w-1] == "───"  and self.print_liste[h+1][w] == " " and self.print_liste[h-1][w] ==" " :
                            self.print_liste[h][w] = "─"
                        if self.print_liste[h][w+1] =="───" and self.print_liste[h][w-1] == "   "  and self.print_liste[h+1][w] == "│" and self.print_liste[h-1][w] ==" " :
                            self.print_liste[h][w] = "┌"
                        if self.print_liste[h][w+1] =="   " and self.print_liste[h][w-1] == "───"  and self.print_liste[h+1][w] == "│" and self.print_liste[h-1][w] ==" " :
                            self.print_liste[h][w] = "┐"
                        if self.print_liste[h][w+1] =="───" and self.print_liste[h][w-1] == "   "  and self.print_liste[h+1][w] == " " and self.print_liste[h-1][w] =="│" :
                            self.print_liste[h][w] = "└"
                        if self.print_liste[h][w+1] =="   " and self.print_liste[h][w-1] == "───"  and self.print_liste[h+1][w] == " " and self.print_liste[h-1][w] =="│" :
                            self.print_liste[h][w] = "┘"
                        if self.print_liste[h][w+1] =="   " and self.print_liste[h][w-1] == "   "  and self.print_liste[h+1][w] == "│" and self.print_liste[h-1][w] =="│" :
                            self.print_liste[h][w] = "│"
                        if self.print_liste[h][w+1] =="───" and self.print_liste[h][w-1] == "───"  and self.print_liste[h+1][w] == "│" and self.print_liste[h-1][w] ==" " :
                            self.print_liste[h][w] = "┬"
                        if self.print_liste[h][w+1] =="───" and self.print_liste[h][w-1] == "   "  and self.print_liste[h+1][w] == "│" and self.print_liste[h-1][w] =="│" :
                            self.print_liste[h][w] = "├"
                        if self.print_liste[h][w+1] =="───" and self.print_liste[h][w-1] == "───"  and self.print_liste[h+1][w] == "│" and self.print_liste[h-1][w] =="│" :
                            self.print_liste[h][w] = "┼"
                        if self.print_liste[h][w+1] =="   " and self.print_liste[h][w-1] == "───"  and self.print_liste[h+1][w] == "│" and self.print_liste[h-1][w] =="│" :
                            self.print_liste[h][w] = "┤"
                        if self.print_liste[h][w + 1] == "───" and self.print_liste[h][w - 1] == "───" and self.print_liste[h+ 1][w] == " " and self.print_liste[h - 1][w] == "│":
                            self.print_liste[h][w] = "┴"
                    if w == 0 and h != 0 and h != len(self.print_liste) - 1  :
                        if self.print_liste[h][w+1] == "───":
                            self.print_liste[h][w] = "├"
                        else:
                            self.print_liste[h][w] = "│"
                    if w == len(self.print_liste[0])-1 and h != 0 and h != len(self.print_liste)-1:
                        if self.print_liste[h][w-1] == "───":
                            self.print_liste[h][w] = "┤"
                        else:
                            self.print_liste[h][w] = "│"
                    if h == 0 and w != 0 and w != len(self.print_liste[0])-1  :
                        if self.print_liste[h+1][w] == "│":
                            self.print_liste[h][w] = "┬"
                        else:
                            self.print_liste[h][w] = "─"
                    if h == len(self.print_liste)-1 and w != 0 and w != len(self.print_liste[0])-1  :
                        if self.print_liste[h-1][w] == "│":
                            self.print_liste[h][w] = "┴"
                        else:
                            self.print_liste[h][w] = "─"
    def len(self):
        return len(self.print_liste)            # on se servira de cette fonction plus loin
    def len2(self):
        return len((self.print_liste[0]))       # de meme
    def show(self):                             # elle va comme indique print notre GridRenderer
         for h in range(len(self.print_liste)) :
             print("".join([self.print_liste[h][w] for w in range(len(self.print_liste[0]))]))
    def ret(self):
        return self.print_liste



"""a = Grid(10,10)
a.spanning_tree()
b =GridRenderer(a.spanning_tree()).show()
a.isolate_box(Box(Pos2D(1,1), Pos2D( 3,4)))
a.isolate_box(Box(Pos2D(4,6), Pos2D( 8,7)))
liste = a.red_zone(Box(Pos2D(1,1), Pos2D(  3,3)))
print([(elem.x,elem.y) for elem in liste])
b = GridRenderer(a).show()"""