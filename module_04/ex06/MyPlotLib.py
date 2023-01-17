import matplotlib.pyplot as plt
import numpy as np

class MyPlotLib:

    def __init__(self):
        pass

    def histogram(self, data, features):
        pass

    def density(self, data, features):
        pass

    def pair_plot(self, data, features):
        pass

    def box_plot(self, data, features):
        pass

def main():
    fig = plt.figure()
    ax = fig.add_subplot(111)

    # Create some data
    x = np.linspace(0, 4*np.pi, 200)
    y1 = np.sin(x)
    y2 = 1.5*np.sin(x)
    y3 = 2*np.sin(x)

    ax.plot(x, y1, label='A = 1')
    ax.plot(x, y2, label='A = 1.5')
    ax.plot(x, y3, label='A = 2')

    ax.legend()

    plt.show()
    pass

if __name__ == "__main__":
    main()