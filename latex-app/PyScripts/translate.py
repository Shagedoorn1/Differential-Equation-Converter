# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 09:46:15 2025

@author: Shagedoorn1
"""

from pysyscontrol import DiffEq
from sympy import init_printing, latex
import re
init_printing()

def equ(x: str) -> str:
    D = DiffEq(x, 'y')
    func = latex(D.function)
    return func

if __name__ == "__main__":
    import sys
    x = str(sys.argv[1])
    result = equ(x)
    
    print(result)