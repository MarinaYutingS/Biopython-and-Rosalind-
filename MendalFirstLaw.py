f = open("./rosalind_iprb.txt","r").readline()
k = float(f.split()[0])
m = float(f.split()[1])
n = float(f.split()[2])

sum = k+m+n

p = k/sum * (k-1)/(sum-1) + k/sum *m/(sum-1) + k/sum * n/(sum-1) + m/sum *(m-1)/(sum-1)*3/4 + m/sum*k/(sum-1) + m/sum*n/(sum-1)*1/2 + 0 + n/sum*k/(sum-1) + n/sum*m/(sum-1)*1/2


p = round(p, 5)

print(p)