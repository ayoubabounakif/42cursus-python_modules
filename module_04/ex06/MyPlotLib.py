import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import date, datetime
from scipy.stats import skew
from math import sqrt
import seaborn as sns

class MyPlotLib:
    def histogram(self, data, features):
        for i in range(len(features)):
            plt.hist(data[features[i]])
            plt.xlabel(features[i])
            plt.title(f'{features[i]}')
            plt.grid(True)
            plt.show()

    def density(self, data, features):
        data[features].plot.kde()
        plt.show()
                
    def pair_plot(self, data, features):
        # g = sns.PairGrid(data, y_vars=features, x_vars=features, height=4)
        # sns.pairplot(data[features])
        # g = sns.PairGrid(data, y_vars=features, x_vars=features, height=4   )
        # sns.pairplot(data[features], diag_kind='hist', kind='reg', fit_reg=False)
        # g.map_diag(sns.kdeplot)
        # g.map_offdiag(sns.kdeplot)

        g = sns.PairGrid(data, vars=features)
        g.map_diag(sns.histplot, binwidth=10, edgecolor=None)
        g.map_offdiag(sns.regplot, fit_reg=False)
        plt.show()

    def box_plot(self, data, features):
        fig = plt.figure()
        fig.add_subplot()
        data.boxplot(column=features, grid=False)
        plt.show()

def main():
    # fig = plt.figure()
    # ax = fig.add_subplot(111)

    # x = np.linspace(0, 4*np.pi, 200)
    # y1 = np.sin(x)
    # y2 = 1.5*np.sin(x)
    # y3 = 2*np.sin(x)

    # ax.plot(x, y1, label='A = 1')
    # ax.plot(x, y2, label='A = 1.5')
    # ax.plot(x, y3, label='A = 2')

    # ax.legend()



    # fig = plt.figure()
    # ax = fig.add_subplot()
 
    data = pd.DataFrame({'date':
    ['01-01-2017',
    '04-12-2008',
    '23-06-1988',
    '25-08-1999',
    '20-02-1993',
    ]})
    data['date'] = pd.to_datetime(data.date, format="%d-%m-%Y")
    data['year'] = data['date'].dt.year
    data['month'] = data['date'].dt.month
    data['day_name'] = data['date'].dt.day_name()
    data['weekday'] = data['date'].dt.weekday
    # print(data.head())

    # ax.plot(data['year'], data['month'])
    # ax2 = ax.twinx()
    # ax2.plot(data['year'], data['weekday'], color='green')
    # ax3 = ax.twinx()
    # ax3.plot(data['year'], data['day_name'], color='red')
    # ax3.spines['right'].set_position(('axes', 1.2))

    # ax.set_ylabel('Month', color="blue")
    # ax2.set_ylabel('Week Day', color="green")
    # ax3.set_ylabel('Day Name', color="red")

    # ax.tick_params(axis='y', colors="blue")
    # ax2.tick_params(axis='y', colors="green")
    # ax3.tick_params(axis='y', colors="red")

    # ax2.spines['right'].set_color('green')
    # ax3.spines['right'].set_color('red')
    # ax3.spines['left'].set_color('blue')

    # fig.tight_layout()




    # np.random.seed(420)
    # d = np.random.randn(20000, 1)
    x = [1, 1, 2, 3, 3, 5, 7, 8, 9, 10,
     10, 11, 11, 13, 13, 15, 16, 17, 18, 18,
     18, 19, 20, 21, 21, 23, 24, 24, 25, 25,
     25, 25, 26, 26, 26, 27, 27, 27, 27, 27,
     29, 30, 30, 31, 33, 34, 34, 34, 35, 36,
     36, 37, 37, 38, 38, 39, 40, 41, 41, 42,
     43, 44, 45, 45, 46, 47, 48, 48, 49, 50,
     51, 52, 53, 54, 55, 55, 56, 57, 58, 60,
     61, 63, 64, 65, 66, 68, 70, 71, 72, 74,
     75, 77, 81, 83, 84, 87, 89, 90, 90, 91
     ]
    
    # n = len(x)
    # range = max(x) - min(x)
    # number_of_intervals = sqrt(n)

    # plt.style.use('ggplot')
    # plt.hist(x, bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 99], edgecolor='black')

    # plt.grid(axis='y', alpha=0.75)
    # plt.xlabel('Value')
    # plt.ylabel('Frequency')

    data = pd.read_csv('../data/athlete_events.csv')

    plot = MyPlotLib()
    plot.histogram(data, ['Height', 'Weight'])
    plot.density(data, ['Weight', 'Height'])
    plot.pair_plot(data, ['Weight', 'Height'])
    plot.box_plot(data, ['Weight', 'Height'])

    # plt.show()

if __name__ == "__main__":
    main()