from functools import reduce

def str2num(s):
    if '.' in s:
        return float(s) #float()可以处理小数的转换
    return int(s) #int()目仅仅支持整数的转换，不能处理小数

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()
