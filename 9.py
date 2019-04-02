def ispalindrome(x):
    if x < 0:
        return "false"
    list = []
    while(x > 0):
        a = x % 10
        x = (x - a) // 10
        list.append(a)
    if len(list) % 2 == 0:
        for i in range(len(list) // 2):
            if list[i] != list[len(list)-1-i]:
                return "false"
        if i == (len(list)//2 - 1):
            return "true"

    if len(list) % 2 == 1:
        for i in range((len(list)-1) // 2):
            if list[i] != list[len(list)-1-i]:
                return "false"
        if i == ((len(list)-1)//2-1):
            return "true"


x = -121
print(ispalindrome(x))
