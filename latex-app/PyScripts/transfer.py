import pysyscontrol as psc
from sympy import latex
def trans(string1: str, string2: str) -> str:
    Trans = psc.TransferFunction(string1, string2)
    result = Trans.transfer_func
    return latex(result)

if __name__ == "__main__":
    import sys
    string1 = str(sys.argv[1])
    string2 = str(sys.argv[2])
    result = trans(string1, string2)
    print(result)