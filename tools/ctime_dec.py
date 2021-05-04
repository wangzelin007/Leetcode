import time

def ctime(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        ref = func(*args, **kwargs)
        end = time.time()
        print('func [{}] cost: {} seconds'.format(func.__name__, end-start))
        return ref
    return wrapper