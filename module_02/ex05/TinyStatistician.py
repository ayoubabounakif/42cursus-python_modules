from math import sqrt

class TinyStatistician:

    def __init__(self):
        pass

    # µ = Σx / m
    def mean(self, x):
        if not len(x) != 0: return None
        return sum(x) / len(x)

    def median(self, x):
        if not len(x) != 0: return None
        x = [float(i) for i in x]
        x = sorted(x)
        if len(x) % 2 == 0:
            return (x[int(len(x) / 2)] + x[int(len(x) / 2) - 1]) / 2
        else:
            return x[int(len(x) / 2)]

    # Q1 = Σx / 4
    # Q3 = Σx / 4 * 3
    def quartiles(self, x):
        if not len(x) != 0: return None
        x = [float(i) for i in x]
        x = sorted(x)
        if len(x) % 2 == 0:
            q1 = (x[int(len(x) / 4)] + x[int(len(x) / 4) - 1]) / 2
            q3 = (x[int(len(x) / 4 * 3)] + x[int(len(x) / 4 * 3) - 1]) / 2
        else:
            q1 = x[int(len(x) / 4)]
            q3 = x[int(len(x) / 4 * 3)]
        return [q1, q3]
        
        

    # σ² = Σ(x - µ)² / m
    def var(self, x):
        if not len(x) != 0: return None
        x = [float(i) for i in x]
        return sum([(i - self.mean(x)) ** 2 for i in x]) / len(x)
    
    # σ = √σ²
    def std(self, x):
        if not len(x) != 0: return None
        x = [float(i) for i in x]
        return sqrt(self.var(x))
    


if __name__ == '__main__':
    tstat = TinyStatistician()
    dataset = [1, 42, 300, 10, 59]

    print('------Data-----', dataset)
    print(tstat.mean(dataset)) # 82.4
    print(tstat.median(dataset)) # 42.0
    print(tstat.quartiles(dataset)) # [10.0, 59.0]
    print(tstat.var(dataset)) # 12279.439999999999
    print(tstat.std(dataset)) # 110.81263465868862

    dataset = []
    print('------Data-----', dataset)
    print(tstat.mean(dataset)) # None
    print(tstat.median(dataset)) # None
    print(tstat.quartiles(dataset)) # None
    print(tstat.var(dataset)) # None
    print(tstat.std(dataset)) # None