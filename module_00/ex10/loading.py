import time
import sys
# from tqdm import tqdm

SCALE = 1000

def ft_progress(listy):
    for i in listy:
        yield i

def main():
    global SCALE
    listy = range(SCALE)
    ret = 0
    width = 40
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        left = width * ret // (SCALE * 2)
        right = width - left
        tags = "=" * left 
        spaces = " " * right
        percents = f"{ret / (SCALE / 100 * 2):.0f}%"
        print("\r[", tags, spaces, "]", percents, sep="", end="", flush=True)
        time.sleep(0.01)

if __name__ == '__main__':
    main()
    # print(ret)
    # print()

# def progress(percent=0, width=40):
#     left = width * percent
#     right = width - left
    
#     tags = "#" * left
#     spaces = " " * right
#     percents = f"{percent:.0f}%"
    
#     print("\r[", tags, spaces, "]", percents, sep="", end="", flush=True)
# # Example run
# for i in range(500):
#     progress(i)
#     time.sleep(0.05)
