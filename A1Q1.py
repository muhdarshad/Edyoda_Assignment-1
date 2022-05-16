first=0
second=1
fib=0
print(second,end=" ")
while True:
    fib=first+second
    if(fib<50):
        print(fib,end=" ")
        first=second
        second=fib
    else:
        break