def f(s1: list[int], s2: list[int]):
    i: int = 0
    a: int = 0
    b: int = 0
    while i < len(s1):
        a = s1[i]
        if i >= len(s2):
            b = 0
        else:
            b = s2[i]
        s1[i] = a + b
        if i < len(s2):
            if a - b > 0:
                s2[i] = b - a
            else:
                s2[i] = a - b
        i = i + 1

s1 = [0,0,0]
s2 = [0,0,0]
       
f(s1, s2)

print(s1)
print(s2)