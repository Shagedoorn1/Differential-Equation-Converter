# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 10:19:48 2025

@author: 23066776
"""

import sympy as sp
import math

class DiffEq:
    
    def __init__(self, eq, func, var='t'):
        self.eq = eq.replace(" ", "")
        self.terms = self.sort_eq()
        self.var = var
        self.t = sp.Symbol(self.var)
        self.func = func
        self.y = sp.Function(self.func)(self.t)
        self.derivatives = self.find_derivs()
        self.K = self.find_factors()
        self.fun = self.make_equation()
        self.function = sp.sympify(sum(self.fun))
    
    def sort_eq(self):
        tarms = self.eq.split("+" or '-')
        return tarms
    
    def find_derivs(self):
        prims = []
        for n in self.terms:
            m = n.count("'")
            if m != 0 and self.func in n:
                d = m
            elif m != 0 and self.func not in n:
                raise ValueError("Don't, please, for the love of god")
            elif m == 0 and self.func in n:
                d = 'A'
            elif m == 0 and self.func not in n:
                d = 0
            prims.append(d)
        return prims
    
    def find_factors(self):
        fact = []
        for term in self.terms:
            i = term.split('*')
            
            sub_l = []
            for char in i:
                try:
                    f = int(char)
                    sub_l.append(f)
                    #print(sub_l)
                except ValueError:
                    sub_l.append(1)
            fact.append(sub_l)
            Ks = [math.prod(sub) for sub in fact]
        return Ks
    
    def make_equation(self):
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
            
                
if __name__ == '__main__':
    string = "2*y''+2*2*y+-3*t"
    a = DiffEq(string, 'y')
    print(a.function)