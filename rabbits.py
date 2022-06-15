def F(n,k):
    if n == 1 or n ==2:
        return 1
    else:
        return F(n-1,k)+F(n-2,k)*k

inputs = open("./rosalind_fib.txt","r").readline().split()
n = int(inputs[0])
k = int(inputs[1])

print (F(n,k))