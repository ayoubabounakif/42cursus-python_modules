from FileLoader import FileLoader

def youngest_fellah(df, year) -> dict:
    df = df[df['Year'] == year]
    return {
        'f': df[df['Sex'] == 'F']['Age'].min(),
        'm': df[df['Sex'] == 'M']['Age'].min(),
    }

if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load("../data/athlete_events.csv")

    print(youngest_fellah(data, 1992))
    print(youngest_fellah(data, 2004))
    print(youngest_fellah(data, 2010))
    print(youngest_fellah(data, 2003))