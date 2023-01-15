from FileLoader import FileLoader

TEAM_SPORTS = ['Basketball', 'Football',  'Tug-Of-War', 'Badminton', 'Sailing', 'Handball', 'Water Polo', 'Hockey', 'Rowing', 'Bobsleigh', 'Softball', 'Volleyball', 'Synchronized Swimming', 'Baseball', 'Rugby Sevens', 'Rugby', 'Lacrosse', 'Polo']

def how_many_medals_by_country(df, country_name):

    # filtered_dfdf = df[(df['Team'] == country_name) & (~df['Sport'].isin(TEAM_SPORTS))]
    filtered_dfdf = df[(df['Team'] == country_name)]
    filtered_dfdf = filtered_dfdf.groupby('Year')['Medal'].value_counts(dropna=False).unstack().fillna(0).astype(int)

    d = {}
    for i in range(len(filtered_dfdf)):
        d[filtered_dfdf.index[i]] = {
            'G': filtered_dfdf.iloc[i]['Gold'] if 'Gold' in filtered_dfdf.columns else 0,
            'S': filtered_dfdf.iloc[i]['Silver'] if 'Silver' in filtered_dfdf.columns else 0,
            'B': filtered_dfdf.iloc[i]['Bronze'] if 'Bronze' in filtered_dfdf.columns else 0
        }
    return d

if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')

    # print(how_many_medals_by_country(data, "United States")) # {1896: {'G': 11, 'S': 7, 'B': 2}, 1900: {'G': 18, 'S': 14, 'B': 13}, 1904: {'G': 64, 'S': 67, 'B': 65}, 1906: {'G': 12, 'S': 6, 'B': 6}, 1908: {'G': 34, 'S': 16, 'B': 15}, 1912: {'G': 46, 'S': 25, 'B': 36}, 1920: {'G': 83, 'S': 40, 'B': 34}, 1924: {'G': 62, 'S': 39, 'B': 33}, 1928: {'G': 37, 'S': 20, 'B': 17}, 1932: {'G': 57, 'S': 56, 'B': 41}, 1936: {'G': 28, 'S': 29, 'B': 27}, 1948: {'G': 54, 'S': 33, 'B': 29}, 1952: {'G': 52, 'S': 38, 'B': 24}, 1956: {'G': 35, 'S': 55, 'B': 19}, 1960: {'G': 81, 'S': 27, 'B': 18}, 1964: {'G': 72, 'S': 34, 'B': 27}, 1968: {'G': 83, 'S': 35, 'B': 34}, 1972: {'G': 69, 'S': 56, 'B': 30}, 1976: {'G': 61, 'S': 41, 'B': 28}, 1980: {'G': 24, 'S': 4, 'B': 2}, 1984: {'G': 133, 'S': 64, 'B': 31}, 1988: {'G': 63, 'S': 41, 'B': 32}, 1992: {'G': 75, 'S': 38, 'B': 46}, 1994: {'G': 6, 'S': 8, 'B': 5}, 1996: {'G': 93, 'S': 38, 'B': 24}, 1998: {'G': 25, 'S': 2, 'B': 3}, 2000: {'G': 64, 'S': 29, 'B': 45}, 2002: {'G': 9, 'S': 52, 'B': 9}, 2004: {'G': 60, 'S': 64, 'B': 34}, 2006: {'G': 9, 'S': 7, 'B': 32}, 2008: {'G': 58, 'S': 55, 'B': 45}, 2010: {'G': 8, 'S': 61, 'B': 20}, 2012: {'G': 77, 'S': 43, 'B': 36}, 2014: {'G': 8, 'S': 28, 'B': 16}, 2016: {'G': 91, 'S': 51, 'B': 42}})
    # print(how_many_medals_by_country(data, "United States")) # {1896: {'G': 11, 'S': 7, 'B': 2}, 1900: {'G': 18, 'S': 14, 'B': 13}, 1904: {'G': 65, 'S': 68, 'B': 66}, 1906: {'G': 12, 'S': 6, 'B': 6}, 1908: {'G': 34, 'S': 16, 'B': 15}, 1912: {'G': 46, 'S': 25, 'B': 36}, 1920: {'G': 111, 'S': 45, 'B': 38}, 1924: {'G': 92, 'S': 44, 'B': 50}, 1928: {'G': 48, 'S': 25, 'B': 19}, 1932: {'G': 71, 'S': 57, 'B': 62}, 1936: {'G': 51, 'S': 29, 'B': 28}, 1948: {'G': 82, 'S': 34, 'B': 33}, 1952: {'G': 77, 'S': 38, 'B': 29}, 1956: {'G': 61, 'S': 61, 'B': 21}, 1960: {'G': 97, 'S': 27, 'B': 21}, 1964: {'G': 96, 'S': 37, 'B': 32}, 1968: {'G': 100, 'S': 37, 'B': 36}, 1972: {'G': 72, 'S': 77, 'B': 46}, 1976: {'G': 73, 'S': 61, 'B': 39}, 1980: {'G': 24, 'S': 4, 'B': 2}, 1984: {'G': 190, 'S': 119, 'B': 50}, 1988: {'G': 89, 'S': 67, 'B': 56}, 1992: {'G': 92, 'S': 57, 'B': 87}, 1994: {'G': 6, 'S': 8, 'B': 5}, 1996: {'G': 157, 'S': 46, 'B': 52}, 1998: {'G': 25, 'S': 2, 'B': 3}, 2000: {'G': 128, 'S': 61, 'B': 51}, 2002: {'G': 9, 'S': 52, 'B': 9}, 2004: {'G': 115, 'S': 75, 'B': 69}, 2006: {'G': 9, 'S': 7, 'B': 32}, 2008: {'G': 121, 'S': 110, 'B': 78}, 2010: {'G': 8, 'S': 61, 'B': 20}, 2012: {'G': 139, 'S': 55, 'B': 44}, 2014: {'G': 8, 'S': 28, 'B': 16}, 2016: {'G': 137, 'S': 52, 'B': 67}})
    # print(how_many_medals_by_country(data, 'Martian Federation')) # {}