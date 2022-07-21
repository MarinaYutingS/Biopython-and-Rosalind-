from Bio import SeqIO
from Bio.Seq import Seq
import re

strings = [str(seq_record.seq) for seq_record in SeqIO.parse("./rosalind_splc.txt","fasta") ]


intron_location = []
m_rna = []

'''
Function which uses re.findall method to convert string to list character wise
'''
def Convert(string):
	return re.findall('[a-zA-Z]', string)

'''
Function find_intron_location
locate introns (strings[1] ~ strings[n]) in the template string(strings[0])
return the starting location and the length of each intron
start from base 0
'''
def find_intron_location(strings):
    for n in range(1, len(strings)):
        for i in range(len(strings[0])-len(strings[n])):
            if strings[0][i:i+len(strings[n])] in strings[n]:
                intron_location.append(i)
                intron_location.append(len(strings[n]))
    return intron_location


'''
Function which reorder the (location, lengths) of introns in ascending order
'''
def reorder_intron_location(intron_loca_list):
    bi_set = {''}
    # 1. TURN LIST INTO TUPLE
    unsorted_tp = tuple(intron_loca_list)
    # 2. ADD TUPLES INTO A SET
    for i in range(0, len(unsorted_tp),2):
        tp1 = (unsorted_tp[i],unsorted_tp[i+1])
        bi_set.add(tp1)
    bi_set.remove('')
    # 3. TURN THE SET INTO A LIST and SORT THE LIST
    return sorted(bi_set,key=lambda loca: loca[0])

# print(reorder_intron_location(find_intron_location(strings)))
    
'''
Function which loops through list intron_location to slice out the introns
'''
def remove_intron(template, intron_location):
    len_accu = 0
    template[intron_location[0][0]:intron_location[0][0]+intron_location[0][1]] = ''
    
    for i in range(1, len(intron_location)):
        len_accu += intron_location[i-1][1]
        slice_start = intron_location[i][0] - len_accu
        slice_end = slice_start + intron_location[i][1]
        template[slice_start:slice_end] = ''
    return template
            
    
m_rna = remove_intron(Convert(strings[0]),reorder_intron_location(find_intron_location(strings)))

m_rna = Seq("".join(m_rna))
print(m_rna.translate())


