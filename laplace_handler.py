# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 18:58:04 2025

@author: 23066776
"""
import sympy as sp
from Diffeq import DiffEq
from numpy import zeros

class LaplaceHandler():
    """
    A class for correctly computing the laplace transform of a differentail equation.
    """
    def __init__(self, equation, name, var='t'):
        """
        Initialise the Laplace Handler.
        Input arguments:
            equation:
                The equation which should be transformed
            name:
                The name of the function in the equation, commonly 'y'
            var:
                The variable of the function, commonly 't'
        Output arguments:
            self.t:
                The variable of the function before transforming
            self.s:
                The complex-valued laplace variable
            self.name:
                The name of the function which is to be transformed
            self.lap_name:
                The name of the laplace transformed function, the capitalised
                version of the function name
            self.function:
                The input string transformed to a sympy expression, see
                Diffeq.py for details
            self.equation:
                The sympy expression.
            self.initial_conds:
                The initial conditions of the differential equations.
                In control theory, these are assumed to be all 0, which means
                that, the system is at rest before the input signal is turned
                on. The transfer from the input signal alone is called the
                forced transfer, as opposed to the natural transfer, arising
                from the oposite case. The complete transfer would be the
                sum of the two.
            self.laplace_transform:
                The laplace transformed version of the input equation
        """
        self.t = sp.Symbol(var.lower())
        self.s = sp.Symbol('s')
        
        self.name = sp.Function(name.lower())
        self.lap_name = sp.Function(name.upper())
        self.function = DiffEq(equation, name, var)
        self.equation = self.function.function
        
        if self.function.order == 0:
            self.initial_conds = [0]
        else:
            self.initial_conds = zeros(self.function.order)
        self.laplace_transform = self.transform()
    
    def transform(self):
        """
        Function that transforms the given equation. The laplace correspondence
        is used because sympy can't correctly handle transforming an function.
        """
        transformed = sp.laplace_transform(self.equation, self.t, self.s, noconds=True)
        transformed = sp.laplace_correspondence(transformed, {self.name: self.lap_name})
        transformed = sp.laplace_initial_conds(transformed, self.t, {self.name: self.initial_conds})
        return transformed
    
    def __str__(self):
        """
        Returns the laplace transformed equation when an instance of the class
        is printed.
        """
        return f"{self.laplace_transform}"
if __name__ == '__main__':
    string = "y'''+y''+y'+y+sin(t)"
    a = LaplaceHandler(string, 'y')