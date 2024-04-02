import sympy as sym
from sympy import symbols
from sympy.parsing.sympy_parser import parse_expr



# ====== Class
class Tree:
    def __init__(self, label, *children):
        self.__label = label
        self.__children = children
    
    def label(self): #getter of label
        """Returns the label of self"""
        return f"{self.__label}"

    def children(self): #getter of children
        """Returns the label of self"""
        return self.__children

    def nb_children(self):
        """Returns number of children"""
        
        return len(self.__children)

    def child(self, i : int):
        """Return the i th child of self"""
        if i >= self.nb_children():
            raise IndexError
        return self.__children[i]

    def is_leaf(self):
        """Return True if self is a leaf"""
        return self.__children == ()

    def depth(self):
       
        if self.is_leaf():
            return 0
        return 1+ max([e.depth() for e in self.__children])

    def __str__(self):
        """ Returns the string representation of self """
        if self.is_leaf():
            return self.__label
        result = f"{self.__label}("
        for child in self.__children:
            if self.__children.index(child) == len(self.__children)-1:
                result += str(child) + ")"
            else:
                result += str(child) + ","
        return result

    def __eq__(self,Tree2):
        """ Returns True if self == Tree2, False otherwise"""
        return str(self) == str(Tree2)

    def deriv(self, var):
        """ Returns a Tree representing the derivative of self with respect to var"""
        x = { var.label() : symbols(var.label())}
        derivative_children = ()
        if self.is_leaf():
            f_x = parse_expr(self.__label,x)
            return Tree(f"{f_x.diff(symbols(var.label()))}")
        if self.__label == "+":
            for child in self.__children:
                derivative_children += (child.deriv(var),)
        if self.__label == "*":
            for child in self.__children:
                if  parse_expr(child.__label).diff(symbols(var.label())) == 0 :
                      derivative_children += (Tree(child.__label),)
                else:
                        derivative_children += (child.deriv(var),)

        return Tree(self.__label,*derivative_children)
        
    def substitute(self, t1, t2):
        """Substitute Tree t1 with Tree t2 in Self """
        if self.__label == t1.__label :
            self.__label = t2.__label
        for child in self.__children:
            child.substitute(t1,t2)
        return self










# ======= Functions

if __name__ == '__main__':
    children = (Tree("*",Tree("3"),Tree("X**2")), Tree("*",Tree("5"),Tree("a")),Tree("a"))
    f = Tree("+",*children)
    print(f"The label of f is {f.label()}")
    print(f.nb_children())
    t1 = Tree("a")
    t2 = Tree("X")
    
    
    print(str(f.deriv("X")))
    print(str(f.substitute(t1,t2)))











#======== Script
#Ex1:
# La classe Tree peut avoir comme méthodes; méthode qui retourne la représentation de l'arbre; une qui ajoute des fils ou des sous arbres;
# une qui supprime des branches ou des fils









