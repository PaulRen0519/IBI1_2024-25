# import necessary library
import re

# creat a funciton to report all the cut sites
def Cut_sites(DNA_seq, DNA_cut):
    temp = True
    
    valid_seq = {"A", "G", "C", "T"}
    # check whether the sequence match AGCT
    if not set(DNA_seq).issubset(valid_seq):
        temp = False

    # find the cut sequence in order
    matches = re.finditer(DNA_cut, DNA_seq)

    start_positions = []
    for match in matches:
        start_position = match.start()
        start_positions.append(start_position + 1)
    
    if temp:
        return start_positions
    else:
        print("Error. Your inputs don't match to DNA sequence.")

# example
DNA_seq = "ACGCGCTATAGCTCGATCAATT"
DNA_cut = "CG"
positions = Cut_sites(DNA_seq, DNA_cut)
print(positions)

# for input DNA
DNA_seq = input("Enter the DNA sequence to be identified (AGCT): ")
DNA_cut = input("Enter the sequence recognised by the restriction enzyme (AGCT): ")

print(Cut_sites(DNA_seq, DNA_cut))