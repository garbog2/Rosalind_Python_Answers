### this function will take the input of multiple key value pairs in FASTA format, and return the key and GC percent of the highest ###

def gc_content(dict):
    highscore_percent = 0.0
    highscore_key = ''
    for key in dict:
        sequence = dict[key]
        gc_count = 0.0
        total_count = len(sequence)
        for letter in sequence:
            if letter == 'C' or letter == 'G':
                gc_count += 1
        gc_percent = gc_count / total_count * 100.0
        if gc_percent > highscore_percent:
            highscore_percent = gc_percent
            highscore_key = key
    print highscore_key
    print highscore_percent
    
