def rna_to_protein(rna):
### RNA to protein translation for up to 10 kbs. The code at the bottom is because Rosalind wants the answer as a file (copying/pasting doesn't work)
### so I wrote a new file within the program. If just looking for the protein sequence, can run without that ###
    rnacodon = {"UUU" : "F", "CUU" : "L", "AUU" : "I", "GUU" : "V", "UUC" : "F", "CUC" : "L", "AUC" : "I",
"GUC" : "V","UUA" : "L","CUA" : "L","AUA" : "I","GUA" : "V","UUG" : "L","CUG" : "L","AUG" : "M","GUG" : "V", "UCU" : "S",
"CCU" : "P", "ACU" : "T", "GCU" : "A", "UCC" : "S", "CCC" : "P", "ACC" : "T", "GCC" : "A", "UCA" : "S", "CCA" : "P", "ACA" : "T",
"GCA" : "A", "UCG" : "S", "CCG" : "P", "ACG" : "T", "GCG" : "A", "UAU" : "Y", "CAU" : "H", "AAU" : "N", "GAU" : "D", "UAC" : "Y",
"CAC" : "H", "AAC" : "N", "GAC" : "D", "UAA" : "", "CAA" : "Q", "AAA" : "K", "GAA" : "E", "UAG" : "", "CAG" : "Q", "AAG" : "K",
"GAG" : "E", "UGU" : "C", "CGU" : "R", "AGU" : "S", "GGU" : "G", "UGC" : "C", "CGC" : "R", "AGC" : "S", "GGC" : "G", "UGA" : "",
"CGA" : "R", "AGA" : "R", "GGA" : "G", "UGG" : "W", "CGG" : "R", "AGG" : "R", "GGG" : "G"}
    reading_frame_rna = [rna[i:i+3] for i in range(0, len(rna), 3)]
    protein = ''
    for codon in reading_frame_rna:
        protein += (rnacodon[codon])
    print protein
    answer = open("answer.txt", "w+")
    answer.write(protein)
    answer.close()
    
    
