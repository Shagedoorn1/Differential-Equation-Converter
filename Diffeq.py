# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 10:19:48 2025

@author: 23066776
"""

import sympy as sp
import math
from myerrors import UnholyError
class DiffEq:
    """
    A class for differential equations. The primary purpose of the class is to
    enter a differential equation in Lagrange notation,
    the way it would be written on paper and convert it into a sympy expression.
    Note that this class only supports non-mixed ODEs.
    If a mixed ODE is necessary then you can create multiple instances of this
    class.
    """  
    def __init__(self, eq, func, var='t'):
        """
        Function to initialise the DiffEq class.
        input arguments:
            eq:
                The differential equation as a string.
                For correct converting, the entered differential equation
                should follow the following rules:
                    1. It should be entered in double quotes.
                    2. For multiplication, use an asterisk (*).
                    3. For subtraction, for example 5-3 enter 5+-3.
                    This might be changed in a later version
            func:
                The name of the function in the differential equation.
                In the example y' = 5*y, y is the name
            var:
                The variable to which the function is to be differentiated to.
                It is assumed to be t.
        
        output arguments:
            self.eq:
                This is the same as the input agrument eq but with whitespaces
                removed
            self.terms:
                This is a list that contains the terms of the equation.
                Terms are, by definition, separated by the + operator
            self.var:
                See above input argument
            self.t:
                Symbolic sympy version of the self.var variable
            self.func:
                See above input argument
            self.y:
                Mathematical sympy Function with the given name,
                dependent on the given variable, assumed to be 't'
            self.derivatives:
                This is a list that contains either an integer or 'A'.
                This variable is assigned by calling the find_derivs function,
                see documentation below for meaning of the elements.
            self.order:
                This is the order of the differential equation, the highest derivative in the equation.
            self.K:
                This is a list that contains the numerical factors of the given
                terms. With this the terms of the equation can be spliced into
                a numerical and symbolic part.
            self.function:
                This is the sympy expression of the differential equation
        """
        self.eq = eq.replace(" ", "")
        self.terms = self.sort_eq()
        self.var = var
        self.t = sp.Symbol(self.var)
        self.func = func
        self.y = sp.Function(self.func.lower())(self.t)
        self.derivatives = self.find_derivs()
        orders = [i for i in self.derivatives if isinstance(i, int)]
        self.order = max(orders, default=0)
        self.K = self.find_factors()
        self.function = sp.sympify(sum(self.make_equation())) #Sum and sympify all converted terms for the full expression
    
    def sort_eq(self):
        """
        Splits the equation into terms based on the + operator and,
        returns them as a list.
        """
        terms = self.eq.split("+")      #Split at the + operator
        return terms
    
    def find_derivs(self):
        """
        This function creates a list that contains either an integer or 'A'.
        This list has as many elements as there are terms in the equation.
        Explanation of list elements:
            non-zero integer:
                The order of the derivative
                For example y'' has order 2 and y' has order 1
            zero integer:
                This indicates that the term doesn't contain the function name'
            string 'A':
                This means the term contains the function name, but not its
                derivative.
        If a term contains a prime (') but not the function name then either
        a factor or 't' is being differentiated. This is likely a typo. In
        this scenario the UnholyError is raised.
        
        """
        prims = []
        for n in self.terms:
            m = n.count("'")
            if m != 0 and self.func in n:
                d = m
            elif m != 0 and self.func not in n:
                raise UnholyError
            elif m == 0 and self.func in n:
                d = 'A'
            elif m == 0 and self.func not in n:
                d = 0
            prims.append(d)
        return prims
    
    def find_factors(self):
        """
        Returns:
            fact:
                This is a list that contains all the factors of every term 
                of the differential equation.
            Ks:
                This is a list that contains the product of all the factors
                of every term of the differential equation.
        This function creates a list of sublists,
        where each sublist contains the numerical factors of a term.
        If a character in a term is not numerical, like y,
        it is replaced with 1 to maintain multiplication consistency.
        Except for t, which is added like a sympy symbol, otherwise this is
        ignored is it is a factor of a term in the equation.
        Finally it creates the Ks list by taking the product of all the items
        in every sublist.
        """
        fact = []
        for term in self.terms:
            i = term.split('*')
            
            sub_l = []
            for char in i:
                try:
                    f = int(char)
                    sub_l.append(f)
                except ValueError:
                    if char == self.var:
                        sub_l.append(sp.Symbol(self.var))
                    else:
                        sub_l.append(1)
            fact.append(sub_l)
            Ks = [math.prod(sub) for sub in fact]
        return Ks
    
    def make_equation(self):
        """
        This function is the primary step in converting the equation into
        the full sympy expression.
        The final step happens in the __init__ function.
        Returns:
            equ:
                This is a list that contains the sympy version of every term in
                self.terms.
        This function converts the terms to sympy expressions by iterating over
        the self.K, self.derivatives and self.terms at the same time.
        These lists have equal sizes and are ordered identically,
        ensuring each iterated value corresponds to the correct term.
        """
        equ = []
        for K, Y, T in zip(self.K, self.derivatives, self.terms):
            if Y == 'A':
                k = K
                ter = self.y
            elif int(Y) > 0:
                k = K
                ter = sp.diff(self.y, self.t, Y)
            elif Y == 0:
                k = 1
                ter = T
            equ_term = sp.sympify(k)*sp.sympify(ter)
            equ.append(equ_term)
        return equ
    
    def __str__(self):
        """
        Returns the converted differential equation as a string when
        the class instance is printed.
        """
        return f'{self.function}'
            
                
if __name__ == '__main__':
    string = "2*y'+2*2*y+-3*t+-12*y'''"
    a = DiffEq(string, 'y')
    print(a)
