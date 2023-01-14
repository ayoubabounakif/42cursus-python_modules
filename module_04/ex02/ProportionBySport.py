from FileLoader import FileLoader

def proportion_by_sport(df, year: int, sport: str, gender: str) -> float:
    # Syntax: df [ (df[‘‘column name 1' ]==’column value’ ) & (df[‘‘column name 2' ]==’column value’ )]

    # total_count = df[ (df['Year'] == year) & (df['Sex'] == gender) ].drop_duplicates().count()[0]
    # sport_count = df[ (df['Year'] == year) & (df['Sex'] == gender) & (df['Sport'] == sport) ].drop_duplicates().count()[0]
    # proportion = '{:0.1f}%'.format((sport_count / total_count * 100))

    total_count = df[ (df['Year'] == year) & (df['Sex'] == gender) ].drop_duplicates(subset='Name').count()[0]
    sport_count = df[ (df['Year'] == year) & (df['Sex'] == gender) & (df['Sport'] == sport) ].drop_duplicates(subset='Name').count()[0]
    proportion = sport_count / total_count

    return proportion

if __name__ == '__main__':
    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')
    print(proportion_by_sport(data, 2004, 'Tennis', 'F')) # 0.019302325581395347 || 0.02307...
    print(proportion_by_sport(data, 2008, 'Hockey', 'F')) # 0.04149467738431458 || 0.03284...
    print(proportion_by_sport(data, 1964, 'Biathlon', 'M')) # 0.009539842873176206|| 0.00659...