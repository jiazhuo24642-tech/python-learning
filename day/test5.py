# 位置参数    默认参数    可变参数    关键字参数 
# 命名关键字参数  需要一个特殊的分隔符 * , * 后的参数被视为命名关键字参数
# 默认参数必须指向不可变对象
# def f1(a, b, c=0, *args, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

# def f2(a, b, c=0, *, d, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

# # 调用示例
# f1(1, 2, 3, 'a', 'b', 'c', x=10, y=20)
# f2(1, 2, 3, d=4, x=5, y=6)
def mul(*arg):
    result = 1 ; 
    for n in arg:
        result *= n
    return result

# 测试
print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('mul(5)测试失败!')
elif mul(5, 6) != 30:
    print('mul(5, 6)测试失败!')
elif mul(5, 6, 7) != 210:
    print('mul(5, 6, 7)测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('mul(5, 6, 7, 9)测试失败!')
else:
    try:
        mul()
        print('mul()测试失败!')
    except TypeError:
        print('测试成功!')