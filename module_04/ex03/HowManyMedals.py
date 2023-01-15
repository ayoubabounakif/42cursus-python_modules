from FileLoader import FileLoader

def how_many_medals(df, participant_name):
    filtered_dfdf = df[df['Name'] == participant_name]
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
    data = loader.load("../data/athlete_events.csv")
 
    print(how_many_medals(data, 'Kjetil Andr Aamodt'))
    {1992: {'G': 1, 'S': 0, 'B': 1}, 1994: {'G': 0, 'S': 2, 'B': 1}, 2002: {'G': 2, 'S': 0, 'B': 0}, 2006: {'G': 1, 'S': 0, 'B': 0}}

    # print(how_many_medals(data, 'Gary Abraham'))
    # {1976: {'G': 0, 'S': 0, 'B': 0}, 1980: {'G': 0, 'S': 0, 'B': 1}}

    # print(how_many_medals(data, 'Yekaterina Konstantinovna Abramova'))
    # {2006: {'G': 0, 'S': 0, 'B': 1}, 2010: {'G': 0, 'S': 0, 'B': 0}}

    # print(how_many_medals(data, 'Kristin Otto'))
    # {1988: {'G': 6, 'S': 0, 'B': 0}}


