# 该文件是外部文件
print('深圳的温度，好高呀')

def sum(l):
    ret = 0
    for i in l:
        ret += i
    return ret

def square_3(x):
    ret = x*x*x
    return ret

l = [3.14,6.28,2.713]

ret = sum(l)
print('调用方法得到了求和：',ret)
    