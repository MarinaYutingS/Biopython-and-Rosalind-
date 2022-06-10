from Bio import SeqIO
from Bio.SeqUtils import GC

max_GC_id = ""
previous_GC = 0.000000
#1. read fasta format sequences 
for seq_record in SeqIO.parse("../rosalind_gc.txt","fasta"):
   
    # 2. count GC%
    current_GC = GC(seq_record.seq)
    # 3. Compare to previous GC%
    if current_GC > previous_GC:
        max_GC_id = seq_record.id
        max_GC_pct = current_GC
    #4.move on to the next fasta sequence
    previous_GC = current_GC

# 5. output the result
# print(max_GC_id)
# print(max_GC_pct)
