import os
import logging
import time


def delete_file(filename, max_retry=3):
    while True:
        try:
            os.remove(filename)
            return
        except Exception as e:
            max_retry -= 1
            time.sleep(0.1)
            logging.error("Delete file exception: {}".format(e))
            if max_retry == 0:
                raise e

def test():
    filename = 'test.txt'
    delete_file(filename)

if __name__ == '__main__':
    test()

# sed 某几行
# 正则表达式