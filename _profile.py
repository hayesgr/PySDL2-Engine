import cProfile
import pstats
from pstats import SortKey
#micro-seconds mod
def f8(x):
    ret = "%8.3f" % x
    if ret != '   0.000':
        return ret
    return "%6dus" % (x * 10000000)

pstats.f8 = f8


def profile():
    cProfile.run('main()',"output.dat")

    with open("output_time.txt","w") as f:
        p = pstats.Stats("output.dat",stream=f)
        p.sort_stats("time").print_stats()
    with open("output_calls.txt","w") as f:
        p = pstats.Stats("output.dat",stream=f)
        p.sort_stats("calls").print_stats()