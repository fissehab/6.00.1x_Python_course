def genFib():
    fibn_1=1 #fib(n-1)
    fibn_2=0 #fib(n-2)
    while True:
      next=fibn_1+fibn_2
      yield next
      fibn_2=fibn_1
      fibn_1=next
    