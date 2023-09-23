def TribFib(n):
    if n==0:
        return 0
    if n ==1:
        return 0 
    if n==2:
        return 1
    if n in res:
        return res[n]
    ans = TribFib(n-1) + TribFib(n-2) + TribFib(n-3)
    res[n] = ans
    return ans
res = {}
print(TribFib("What is the sequence"))