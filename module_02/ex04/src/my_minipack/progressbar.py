import time

SCALE = 3333
WIDTH = 60
START = time.time()

def ft_progress(listy):
    for i in listy:
        yield i

def progressbar(elem, ret):
    left = WIDTH * ret // (SCALE * 2)
    right = WIDTH - left
    tags = "=" * left 
    spaces = " " * right
    estimated_time = (time.time() - START) * (SCALE) / (elem + 1)
    percents = f"{ret / (SCALE / 100 * 2):.0f}%"
    print("\rETA: {:.2f}s ".format(estimated_time), "[", percents, "][", tags, spaces, "] ", ret // 2,'/', SCALE, " | ", "elapsed time {:.2f}".format(time.time() - START), sep="", end="", flush=True)
