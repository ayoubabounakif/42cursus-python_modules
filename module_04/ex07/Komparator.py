import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

class Komparator:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def compare_box_plots(self, categorical_var: str, numerical_var: str):
        for category in self.df[categorical_var].unique():
            sub_df = self.df[self.df[categorical_var] == category]
            sub_df[numerical_var].plot(kind='box')
            plt.title(f'{numerical_var} for {categorical_var} = {category}')
            plt.show()

    def density(self, categorical_var: str, numerical_var: str):
        for category in self.df[categorical_var].unique():
            sub_df = self.df[self.df[categorical_var] == category]
            sub_df[numerical_var].plot(kind='density')
            plt.title(f'{numerical_var} density for {categorical_var} = {category}')
            plt.show()

    def compare_histograms(self, categorical_var: str, numerical_var: str):
        for category in self.df[categorical_var].unique():
            sub_df = self.df[self.df[categorical_var] == category]
            sub_df[numerical_var].plot(kind='hist')
            plt.title(f'{numerical_var} histogram for {categorical_var} = {category}')
            plt.show()



def main():
    data = pd.read_csv('../data/athlete_events.csv')
    komparator = Komparator(data)
    komparator.compare_box_plots('Sex', ['Weight', 'Height'])
    komparator.density('Sex', ['Weight', 'Height'])
    komparator.compare_histograms('Sex', ['Weight', 'Height'])

if __name__ == "__main__":
    main()

    # https://www.youtube.com/watch?v=KCYTR3wReXc
