import time

def exeTime(func):
    def wrapper(x):
        start=time.clock()
        func(x)
        end=time.clock()
        print(func.__name__,"time",end-start)
        return func
    return wrapper

@exeTime
def _cocktail_sort(the_list):
    the_len = len(the_list)
    if the_len <2:#0和1
        print "无需排序"
        return the_list
    else:
        m = 0
        while 1:
            flag = False
            for i in range(m,the_len-1-m):
                if the_list[i] > the_list[i+1]:
                    the_list[i], the_list[i+1] = the_list[i+1], the_list[i]
                    flag = True
                print the_list,m
            j = the_len-2-m
            while j > 0:
                if the_list[j-1] > the_list[j] and j>m:
                    the_list[j], the_list[j-1] = the_list[j-1], the_list[j]
                    flag = True
                j -= 1
                print the_list,m,j
            m += 1
            if flag == False:
                return the_list
                break

if __name__ == '__main__':
    the_list = [6, 4, 5, 1, 8, 7, 2, 3]
    print "原始的列表是:" + str(the_list)
    print "鸡尾酒排序之后的列表是:" + str(_cocktail_sort(the_list))
