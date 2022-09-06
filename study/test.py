import sys

while True:
    n = str(sys.stdin.readline().split()[0])
    dic = {}
    if n == str(0):
        break
    
    result,f = 0,1
    
    if len(n) in dic:
        f = dic[len(n)]
    else:
        for i in range(len(n)):
            f *= (i+1)
            dic[len(n)] = f
    for i,a in enumerate(n):
        if i > 0:
            f /= (len(n)+1-i)
        result += int(a)*f
    print(int(result))