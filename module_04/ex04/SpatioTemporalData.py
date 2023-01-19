from FileLoader import FileLoader
import pandas as pd

class SpatioTemporalData:
    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df

    def when(self, location: str) -> pd.DataFrame:
        return self.df[self.df['City'] == location]['Year'].drop_duplicates().tolist()

    def where(self, date: int) -> pd.DataFrame:
        return self.df[self.df['Year'] == date]['City'].drop_duplicates().tolist()

if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')

    sp = SpatioTemporalData(data)
    print(sp.where(1896)) # ['Athina']
    print(sp.where(2016)) # ['Rio de Janeiro']
    print(sp.when('Athina')) # [2004, 1906, 1896]
    print(sp.when('Paris')) # [1900, 1924]