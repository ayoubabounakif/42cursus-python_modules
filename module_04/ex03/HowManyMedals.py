from FileLoader import FileLoader

def how_many_medals(df, participant_name):
    pass

if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load("../resources/athlete_events.csv")
    print(how_many_medals(data, 'Kjetil Andr Aamodt'))


