# import necessary library to regulate the string
import re
import datetime

time1 = datetime.datetime.now()
# imput the sequence, and find the GT to AG segments
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
max_introns = re.findall(r'GT.*AG', seq)
print(max_introns) 

# identify the lenth of max_intron
max_intron = max_introns.pop(0)
max_lenth = len(max_intron)

# after pop out the intron, append it in it again
max_introns = max_introns.append(max_intron)
print(max_lenth)
time2 = datetime.datetime.now()
print(f"Running time: {time2 - time1}")