import re

# input one of three splice donor (GTAG, GCAG, ATAC)
combination = input("Please enter one of the GTAG, GCAG, ATAC: ")
part1 = combination[:2]
part2 = combination[2:]
# consider when the user input anything out of the three combinations
while combination not in ['GTAG', 'GCAG', 'ATAC']:
    print("Your input is not in the three combinations")
    combination = input("Please enter one of the GTAG, GCAG, ATAC: ")

# open the input file and output file
infile = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
outfile_name = f"{combination}_spliced_tata_genes.fa"
outfile = open(outfile_name, 'w')

current_seq = ""
current_name = ""

# define the TATA box 
tata_pattern = re.compile('TATA[AT]A[AT]')

for line in infile:
    line = line.strip()
    if line.startswith(">"):
        # deal with the current sequence first
        if current_seq:
            tata_count = len(tata_pattern.findall(current_seq))
            # find the point to cut 
            
            splice_match = re.search(rf'{part1}.*{part2}', current_seq)
            if splice_match and tata_count > 0:
                gene_names = re.findall(r'gene:(\S+)', current_name)
                if gene_names:
                    current_gene_name = gene_names[0].replace('gene:', '')
                    # output the name of gene and the account of TATA box
                    outfile.write(f">{current_gene_name} TATA box: {tata_count}\n")
                    # write on the first line
                    outfile.write(current_seq + "\n")
        # updatet the gene name
        current_name = line
        current_seq = ""
    else:
        current_seq += line

# deal with the last line
if current_seq:
    tata_count = len(tata_pattern.findall(current_seq))
    splice_match = re.search(combination, current_seq)
    if splice_match and tata_count > 0:
        gene_names = re.findall(r'gene:(\S+)', current_name)
        if gene_names:
            current_gene_name = gene_names[0].replace('gene:', '')
            outfile.write(f">{current_gene_name}_{tata_count}\n")
            outfile.write(current_seq + "\n")

# close the file
infile.close()
outfile.close()