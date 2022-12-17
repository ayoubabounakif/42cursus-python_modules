import time
import os

def log(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        with open("machine.log", "a") as f:
            exec_time = "{:.4f}".format(end - start)
            unit = 's' if float(exec_time) > 1 else 'ms'
            spaces = ' ' * (20 - len(func.__name__) - len(exec_time))
            f.write(f"({os.environ['USER']})Running: {func.__name__.replace('_', ' ').title()} {spaces} [ exec-time = {exec_time} {unit} ]\n")
        return result
    return wrapper
