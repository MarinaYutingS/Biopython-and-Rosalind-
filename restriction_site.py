from Bio import SeqIO
from datetime import datetime
start=datetime.now()

for seq_record in SeqIO.parse("./rosalind_gc.txt","fasta"):
    string = seq_record.seq
    for length in range(4,13):
        for i in range(len(string)-length+1):
            substring = string[i:i+length]
            if substring.reverse_complement() == substring:
                print(str(i+1)+" "+str(length),end=" ")

print (datetime.now()-start)