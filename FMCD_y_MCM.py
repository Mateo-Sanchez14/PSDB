# %%
import numpy as np

# %%
# Maximo comun divisor
def mcd(num1, num2):
    a = max(num1, num2)
    b = min(num1, num2)
    while b!=0:
        mcd = b
        b = a%b
        a = mcd
    return mcd

# Minimo comun multiplo
def mcm(num1, num2):
    a = max(num1, num2)
    b = min(num1, num2)
    mcm = (a / mcd(a, b)) * b
    return mcm

# %%
def mcd_3(num1, num2, num3):
    return mcd(num1,mcd(num2,num3))

# %%
mcd_3


