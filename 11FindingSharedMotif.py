from Bio import SeqIO
from Bio.Seq import Seq
import timeit

start = timeit.default_timer()

# read from file and put strings into a list
strings = [Seq(seq_record.seq) for seq_record in SeqIO.parse("./rosalind_lcsm.txt","fasta") ]
# sort the list based on the length of the elements present within
strings.sort(key=len)


'''
Build a longest common string for s1 and s2
matrix: len(s1) * len(s2) matrix with alignment values 
s1: string s1, shorter or equal to s2
p: store the location of the largest value in s1
'''
def consensus_string(matrix,s1,p):
    # iterate through the matrix from the [:-1] to the begining, tracking down the largest value of each row which is consistant with [i-1][j-1] 
    longest = max(map(max,matrix))
    common_string = [x for x in s1[p-longest+1:p+1]]
    return("".join(common_string))

# comparing the first two elements in the list to find the longest common substring
def alignment_score(s1,s2):
    # build a rows * column matrix and update the numbers if two characters matches 
    rows = len(s1)
    columns = len(s2)
    matrix = [[0]*(columns) for i in range(rows)]
    counter = 0
    longerest = 0
    # consensus = [""]*rows
    for i in range(rows):
        for j in range(columns):
            if s1[i] == s2[j]:
                matrix[i][j] = 1
                if matrix[i-1][j-1] != 0:
                    matrix[i][j] = matrix[i-1][j-1]+1
                    counter += 1
                    # store the longest string as matrix proceeds
                    if counter > longerest:
                        # consensus.append(s1[i-counter+1:i+1])
                        p = i
                        longerest = counter
                    else:
                        p = i
    common_string = consensus_string(matrix,s1,p)
    return common_string
    # print(matrix)

common_strings = []
# compare the consensus string with s3, s4, s5 ...
for i in range(len(strings)-1):
    # store the single alignment common strings into a list
    common_strings.append(alignment_score(strings[i],strings[i+1]))
print(common_strings[-1])

stop = timeit.default_timer()

print('Time: ', stop - start) 



  



