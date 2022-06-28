f = open("./rosalind_iev.txt","r").readline().split()
a = int(f[0])
b = int(f[1])
c = int(f[2])
d = int(f[3])
e = int(f[4])
f =int(f[5])

p = (a * 1 + b * 1 + c * 1 + d *3/4 + e * 1/2 + f * 0) *2

print(p)
