#/usr/bin/env python
# -*- coding: UTF-8 -*-
def run0(opt):
    if opt in ['海底捞', '九毛九']: return 1 # do something and return
    else: raise Exception('输出参数错误，请检查！')

def run1(opt):
    if opt in ['上海', '深圳']: return 1 # do something and return
    else: raise Exception('输出参数错误，请检查！')

def run2(opt):
    if opt in ['火车', '飞机']: return 1 # do something and return
    else: raise Exception('输出参数错误，请检查！')

def run3(opt):
    if opt in ['好吃', '难吃']: return 1 # do something and return
    else: raise Exception('输出参数错误，请检查！')

if __name__=="__main__":
    try:
        q0 = raw_input("瓜瓜今天中午吃什么？\n")
        a0 = run0(q0)
        if a0:
            q1 = raw_input("去哪吃?\n")
            a1 = run1(q1)
            if a1:
                q2 = raw_input("怎么去？\n")
                a2 = run2(q2)
                if a2:
                    q3 = raw_input("好吃吗？\n")
                    a3 = run3(q3)

    except Exception as e:
        print(e)
