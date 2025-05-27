# import necessary library
import re
import os

# open the sourse file and creat the output file
os.chdir("Practical7")
infile = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
outfile = open('tata_genes.fa', 'w')

# identify the TATAWAW sequence in the sequence
current_seq = ""
current_name = ""

# set a loop to read and rewrite every line
for line in infile:
        line = line.strip()
        if line.startswith(">"):
            
            # first deal with current sequence
            if current_seq and re.search('TATA[AT]A[AT]', current_seq):

                gene_names = re.findall(r'gene:(\S+)', current_name)
                if gene_names:
                    current_gene_name = gene_names[0].replace('gene:', '')
                    outfile.write(f">{current_gene_name}\n")
                    for i in range(0, len(current_seq), 60):
                        outfile.write(current_seq[i: i + 60] + "\n")
            # update the name of gene
            current_name = line
            current_seq = ""
        else:
            current_seq += line

# deal with the last sequence
if current_seq and re.search('TATA[AT]A[AT]', current_seq):
        
        gene_names = re.findall(r'gene:(\S+)', current_name)
        if gene_names:
            current_gene_name = gene_names[0].replace('gene:', '')
            outfile.write(f">{current_gene_name}\n")
            for i in range(0, len(current_seq), 60):
                    outfile.write(current_seq[i: i + 60] + "\n")

infile.close()
outfile.close()