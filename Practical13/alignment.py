from Bio import SeqIO
import blosum as bl
import os

os.chdir("Practical13")

# read FASTA sequence
def read_seq(filename):
    with open(filename) as f:
        sequence = ""
        for line in f:
            if not line.startswith(">"):
                sequence += line.strip()
    return sequence

human_seq = read_seq("P04179.fasta")
mouse_seq = read_seq("P09671.fasta")
random_seq = read_seq("Random.fasta")

# check the length
if len(human_seq) != len(mouse_seq):
    print("Error: Sequences are not the same length.")
    exit()

# input BLOSUM62 matrix
blosum62 = bl.BLOSUM(62)

def calculate_score(seq1, seq2):
    identity = 0
    scores = 0
    
    # compare each amino acid
    for a1, a2 in zip(seq1, seq2):
        score = blosum62[a1][a2]
        scores += score
        if a1 == a2:
            identity += 1

    # calculate identity percentage
    identity_percent = (identity / len(human_seq)) * 100
    return scores, identity_percent

# print the scores and identity
scores1, identity1 = calculate_score(human_seq, mouse_seq)
scores2, identity2 = calculate_score(human_seq, random_seq)
scores3, identity3 = calculate_score(random_seq, mouse_seq)
print("Scores between human and mouse:", scores1)
print("Scores between human and random:", scores2)
print("Scores between mouse and random:", scores3)
print("Identity between human and mouse:", identity1)
print("Identity between human and random:", identity2)
print("Identity between random and mouse:", identity3)