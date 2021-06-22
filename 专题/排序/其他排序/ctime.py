import time

def cTime(func):
    start = time.time()
    def inner(*args, **kwargs):
        ref = func(*args, **kwargs)
        end = time.time()
        print('func {} exec {}'.format(func.__name__, end-start))
        return ref
    return inner