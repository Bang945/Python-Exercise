trans = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}

def transcribe(c):
    if c not in trans.keys():
        raise Exception("DNA can only contain G C T A")
    return trans[c]

def to_rna(dna_strand):
    return "".join(map(transcribe, list(dna_strand)))
