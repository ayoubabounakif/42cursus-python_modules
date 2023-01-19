import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from MyPlotLib import MyPlotLib

class Komparator:
    def __init__(self) -> None:
        pass

    def compare_box_plots(self, categorical_var, numerical_var):
        pass

    def density(self, categorical_var, numerical_var):
        pass

    def compare_histograms(self, categorical_var, numerical_var):
        pass



def main():
    data = pd.read_csv('../data/athlete_events.csv')
    print(data.head())

if __name__ == "__main__":
    main()
