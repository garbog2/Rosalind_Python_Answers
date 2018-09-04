import regex as re
### upgraded regex provides the overlapped = True statement, and the ',' after print prints everything on one line. For some reason, Rosalind 
### uses 1-based indexing, which the '+1' is for at the end
def find_dna_motif_re(dna, motif):
    for m in re.finditer(motif, dna, overlapped = True):
        print m.start() + 1,
