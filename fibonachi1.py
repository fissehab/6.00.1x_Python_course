def fibonachi(n):
    if n <=1:
        return 1
    else:
        return fibonachi(n-1)+fibonachi(n-2)

def genPrimes(n):
    p=[2]
    while n>=2:
     if n%p!=0:
         p.append(n)
         yield p
        