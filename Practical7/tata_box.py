# import necessary library
import re

# open the sourse file and creat the output file
infile = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
outfile = open('tata_genes.fa', 'w')

# identify the TATAWAW sequence in the sequence
current_seq = ""
first_line = infile.readline()
current_name_list = re.findall(r'gene:(\S*)', first_line)
current_name = current_name_list.pop(0)

for line in infile:
    if line.startswith(">"):
        if current_seq and re.search('TATA[AT]A[AT]', current_seq):
            outfile.write(f">{current_name}\n")
            outfile.write(current_seq + '\n')
            current_name_list = re.findall(r'gene:(\S*)', line)
            current_name = current_name_list.pop(0)
            current_seq = ""
    else:
        current_seq += line.strip()

if current_seq and re.search('TATA[AT][AT]A', current_seq):
        outfile.write(f">{current_name}\n")
        outfile.write(current_seq + "\n")