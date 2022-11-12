import sys

print(' '.join(sys.argv[1:])[::-1].swapcase() if len(sys.argv) -1 >= 1 else 'Arguments expected\nusage: python3 exec.py [args]')