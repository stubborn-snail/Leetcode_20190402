
def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if (x > (pow(2, 31) - 1)) or (x < (-1) * pow(2, 31)):
        return 0
    if x < 0:
        flag = -1
    else:
        flag = 1

    list = []

    x1 = abs(x)
    sum = 0

    while(x1 > 0):
        a = x1 % 10
        x1 = (x1 - a) // 10
        list.append(a)

    for i in range(len(list)):
        sum = 10 * sum + list[i]

    sum = sum * flag

    if (sum > (2 ** 31 - 1)) or (sum < (-1) * 2 ** 31):
        return 0
    print(sum)

x = -123
reverse(x)

