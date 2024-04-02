import math as m
import sympy as sym
from sympy.abc import x
#******** Class

class Fraction:
    def __init__(self,n,d):
        """Initialize the fraction object with numerator and denominator"""
        self.denum= d
        self.num= n
    
    def __str__(self):
        """returns beautifully the fraction"""       
        return (f"{self.num}/{self.denum}")
    
    def __add__(self, frac2):
        """ Returns fraction which is the sum of self and frac2 """
        return Fraction(frac2.denum*self.num+self.denum*frac2.num , frac2.denum*self.denum)

    def simplify(self):
        """ Returns simplified fraction of self"""
        pgcd=m.gcd(self.denum,self.num)
        num= int(self.num/pgcd)
        denum= int(self.denum/pgcd)
        return Fraction(num,denum)

    def isEqual(self,frac2):
        """ Return True if self=frac2 False otherwise"""
        s=self.simplify()
        f2= frac2.simplify()
        return ( s.denum==f2.denum and s.num==f2.num)

    def mult(self,frac2):
        """ Returns product of self and frac2"""
        r= Fraction (self.num*frac2.num , self.denum*frac2.denum)
        return r.simplify()

class polynome:
    def __init__(self,coeff_list):
        self.expr=coeff_list[0]
        for i in range(1,len(coeff_list)):
            self.expr += coeff_list[i]*x**i
        
    def __str__(self):
        """return the expression of self"""
        return f"{self.expr}"

    def __add__(self,p2):
        """return the of sum self and p2""" 
        return self.expr + p2.expr

    def deriv(self):
        """return the derivative of self"""
        return self.expr.diff(x)

    def integrate(self,C):
        """ return the integral of self"""
        return sym.integrate(self.expr,x)+C


#===== Fonctions

def H_n(n):
    
    """Return H(n) (harmonic series)"""
    if n<=1:
        return 1
    r=Fraction(1,1)
    for i in range(2,n+1):
        r= r+Fraction(1,i)
        r=r.simplify()
    return r.simplify()

def leibniz(n):
    """Return L(n)"""
    if n==0:
        return 1
    r=Fraction(1,1)
    for i in range(1,n+1):
        r=r+Fraction((-1)**i,2*i+1)
        r=r.simplify()
    return r.simplify()
    
#...... Script



if __name__=='__main__':
    frac_1=Fraction(2,4)
    frac_2=Fraction(3,8)
    frac_3=frac_1+frac_2
    print(str(frac_3.simplify()))
    print(frac_1.isEqual(frac_2))
    print(frac_1.mult(frac_2))

    print(H_n(10000))
    print(leibniz(10000))
  
    p=polynome([1,2,3])
    p2=polynome([0,0,1])
    print(str(p+p2))
    print(str(p.deriv()))
    print(str(p2.integrate(17)))