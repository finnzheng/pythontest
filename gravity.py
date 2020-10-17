#coding:utf-8

def w(m,g):
    return m*g

def weight(g):
    def cal_mg(m):
        return m*g
    return cal_mg

w = weight(10)
G = w(100)
print(G)

w2 = weight(9.8)
G3 = w2(100)
print(G3)

