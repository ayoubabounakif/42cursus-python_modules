import pandas as pd

class FileLoader:
    def __init__(self) -> None:
        pass

    def load(self, path: str) -> pd.DataFrame:
        dataset = pd.read_csv(path)
        print(f"Loading dataset of dimensions {dataset.shape[0]} x {dataset.shape[1]}")
        return dataset

    def display(self, df: pd.DataFrame, n: int) -> None:
        if not isinstance(n, int): return None
        print(df.head(n) if n > 0 else df.tail(-n))
