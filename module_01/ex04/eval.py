class Evaluator:

    @staticmethod
    def zip_evaluate(coefs, words):
        if not len(coefs) == len(words): return -1
        return sum(float(len(x) * float(y)) for x, y in zip(words, coefs))

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if not len(coefs) == len(words): return -1
        return sum(float(len(x[1]) * coefs[x[0]]) for x in list(enumerate(words)))

if __name__ == '__main__':
    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    print(Evaluator.zip_evaluate(coefs, words)) # 32.0

    words = ["Le", "Lorem", "Ipsum", "n", "est", "pas", "simple"]
    coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
    print(Evaluator.enumerate_evaluate(coefs, words)) # -1