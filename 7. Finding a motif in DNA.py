import regex as re
### upgraded regex provides the overlapped = True statement, and the ',' after print prints everything on one line ###
def find_dna_motif_re(dna, motif):
    for m in re.finditer(motif, dna, overlapped = True):
        print m.start() + 1,
