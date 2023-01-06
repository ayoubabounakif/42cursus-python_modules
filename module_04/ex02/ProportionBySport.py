from FileLoader import FileLoader

#"What was the percentage of
#female tennis players among all the female participants of the 2016 Olympics?"
def proportion_by_sport(df, year, sport, gender) -> float:
    filtered_df = df[df['Year'] == year]
    filtered_df = df[df['Sex'] == gender]
    # filtered_df = filtered_df.drop_duplicates(subset='Sport')
    total_count = len(filtered_df) # total number of female **participants** in year

    filtered_df = filtered_df[filtered_df['Sport'] == sport]
    filtered_df = filtered_df.drop_duplicates(subset='Sport') # remove duplicates
    sport_count = len(filtered_df) # number of gender **sport** players in year

    proportion = sport_count / total_count * 100
    return proportion

if __name__ == '__main__':
    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')
    print(proportion_by_sport(data, 2004, 'Tennis', 'F'))
    pass