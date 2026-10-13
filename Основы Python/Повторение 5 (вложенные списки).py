def pascal(n):
    if n == 0:
        return [1]
    a = [1,1]
    for i in range(n-1):
        b = [1]*(len(a)+1)
        for j in range(len(a)-1):
            b[j+1]=a[j]+a[j+1]
        a = b[:]
    return a
        
print(pascal(7))
