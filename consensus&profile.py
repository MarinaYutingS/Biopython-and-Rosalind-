from Bio import SeqIO
from Bio.Seq import Seq

a = []
c = []
g = []
t = []
position_a = []
position_c = []
position_g = []
position_t = []
occurance_a = []
occurance_c = []
occurance_g = []
occurance_t = []

'''
Read from fasta
Count occurence of each character seperately
Append the count into each character list
'''
for seq_record in SeqIO.parse("./rosalind_gc.txt","fasta"):
    columns = len(seq_record)
    rows = int(seq_record.id[-1])
    strings = Seq(seq_record.seq)
    for s in strings:
        a.append(s.count("A"))
        c.append(s.count("C"))
        g.append(s.count("G"))
        t.append(s.count("T"))


'''
Slice each character list with the string length
Appened to the position list of each character accordingly
'''
for i in range(columns):
    position_a.append(a[i::columns])
    position_c.append(c[i::columns])
    position_g.append(g[i::columns])
    position_t.append(t[i::columns])

'''
Calculate the sum of character 'A' occured in each position of the given strings
'''
for item in position_a:
    occurance_a.append(sum(item))

'''
Calculate the sum of character 'C' occured in each position of the given strings
'''
for item in position_c:
    occurance_c.append(sum(item))

'''
Calculate the sum of character 'G' occured in each position of the given strings
'''
for item in position_g:
    occurance_g.append(sum(item))

'''
Calculate the sum of character 'T' occured in each position of the given strings
'''
for item in position_t:
    occurance_t.append(sum(item))

'''
Construct 2d array
Row number: 4 (A,C,G,T)
Column number: len(strings)
'''
profile = [[0]*columns]*4

'''
Add the occurence of each character on each position to the profile
'''
profile[0] = occurance_a
profile[1] = occurance_c
profile[2] = occurance_g
profile[3] = occurance_t

'''
Define an out put function
'''
def output():
    if position == 0:
        print("A", end="")
    elif position == 1:
        print("C", end="")
    elif position == 2:
        print("G", end="")
    elif position == 3:
        print("T", end="")

'''
Find the consensus string
Output the consensus string
'''
previous = 0
for j in range(len(profile[0])):
    for i in range(len(profile)):
        x = profile[i][j]
        if x>previous:
            position = i
            previous = x
    previous = 0
    output()

'''
Output the profile
'''
for i in range(len(profile)):
    for j in range(len(profile[0])):
        print(profile[i][j],end=" ")
    print()




