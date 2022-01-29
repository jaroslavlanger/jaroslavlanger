import ctypes
from ctypes import c_int, c_char_p, c_void_p, c_double
from datetime import datetime

clib = ctypes.cdll.LoadLibrary("./build/knapsack.so")
clib.solve.argtypes = [c_int, c_char_p, c_char_p]
clib.solve.restype = c_double

SETS = [
    (
        "../data/nr/NR{n}_inst.dat", 
        "../data/computed/nr_resu/n_n{n}_{m}_resu_test.csv"
    ),
    (
        "../data/zr/ZR{n}_inst.dat",
        "../data/computed/zr_resu/z_n{n}_{m}_resu_test.csv"
    )
]

METHODS = {0: "bf", 1: "bab", 2: "sbab"}

NUMBERS = [4, 10, 15, 20] # [4, 10, 15, 20, 22, 25, 27] # [4, 10, 15, 20, 22, 25, 27, 30, 32, 35, 37, 40]

for inst, resu in SETS:
    for m in METHODS:
        for n in NUMBERS:
            time = clib.solve(m, inst.format(n=n).encode(), resu.format(n=n, m=METHODS[m]).encode())
            print("n:", n, "current time:", datetime.now().strftime("%H:%M:%S"))
