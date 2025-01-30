import random

def random_multiply_and_round(numbers, multiplier_range):
    result = []
    for num in numbers:
        multiplier = random.uniform(*multiplier_range)
        new_value = round(num * multiplier, 1)
        result.append(new_value)
    return result

# 输入的数字列表
numbers = [46.4, 30, 35.3, 31.2, 34.3, 29.6, 34.4, 30.4, 32.7, 31.1, 34.5, 29.9]


multiplier_range = (1.08, 1.18)

# 计算并输出结果
result = random_multiply_and_round(numbers, multiplier_range)
print(result)
