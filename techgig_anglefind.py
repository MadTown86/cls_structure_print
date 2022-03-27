def fibo(arg):
    res = [0, 1, 2]
    while (res[len(res)-2] + res[len(res)-1]) < arg:
        res.append((res[len(res)-2] + res[len(res)-1]))
    return res

str = " bob"
str.lstrip

def anglefind(len1, len2):
    import math
    if 1 <= int(len1) <= 200:
        ab = int(len1)

    if 1 <= int(len2) <= 200:
        bc = int(len2)

    return round(90 - math.degrees(math.atan(ab/bc)))

def powint():
    line = input()
    linel = line.split(" ")
    print(linel)

    import math
    power = math.pow(int(linel[0]), int(linel[1]))
    mod = power % int(linel[2])
    print(int(mod), end="")



str1 = " bobs"
str2 = str1.lstrip()
print(str2[:1])





