# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 
import math
def quadratic(a, b, c):
     # 处理 a=0 的退化情况（变成一元一次方程）
    if a == 0:
        if b == 0:
            return None  # 连 b 也是 0，无解或无数解
        return (-c / b,) # 返回单元素元组，保持“返回解”的语义
        
    # 计算判别式 delta = b^2 - 4ac
    delta = b**2 - 4 * a * c
    
    # 判别式小于0，无实数根
    if delta < 0:
        return None  # 也可以返回复数，这里按常规返回 None 表示无实根
        
    # 计算两个实根
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    
    # 通常习惯小的根在前，大的在后（可选）
    if x1 > x2:
        x1, x2 = x2, x1
        
    return x1, x2


# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')