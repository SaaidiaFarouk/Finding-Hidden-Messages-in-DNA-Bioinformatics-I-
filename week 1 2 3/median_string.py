def suffix (pattern):
    patternn =pattern[1:len(pattern)]
    return patternn

def hamming_distance(p,q):
    c=0
    for i in range(len(p)):
        if p[i]!=q[i]:
            c+=1
    return c

def Neighbors(Pattern, d):
    if d==0:
        return Pattern
    if len(Pattern)==1 :
        return ['A','C','T','G']
    Neighborhood=list()
    SuffixNeighbors=Neighbors(suffix(Pattern), d)
    for text in SuffixNeighbors:
        if hamming_distance(suffix(Pattern), text) < d:
            for x in ['A','C','T','G']:
                Neighborhood.append(x+text)
        else:
            Neighborhood.append(Pattern[0]+text)
    return Neighborhood

def distancepatternstrings(pattern,dna):
    k=len(pattern)
    distance=0
    strings=dna.split( )
    for string in strings:
        dist=9999
        for i in range(len(string)-k+1):
            patternn=string[i:i+k]
            if dist > hamming_distance(pattern,patternn):
                dist=hamming_distance(pattern,patternn)
        distance=distance+dist 
    return distance

def medianstring(dna,k): 
    distance=999
    pitern=''
    for i in range(k):
        pitern=pitern+'A'
    allstrings=Neighbors(pitern,k)
    patterns=allstrings
    for i in range(len(patterns)):
        pattern=patterns[i]
        if distance > distancepatternstrings(pattern,dna):
            distance=distancepatternstrings(pattern,dna)
            Median=pattern
    return Median



dna="""TAGGGCCTGTATCCTAACCAGCGCACCTAAACCCTGGGAACT
TTCCACAAGTTAAAGTGTCTGTAAGCGAGACTTCTAGCCAGC
CTTGGCTGTTCTGCCCGCCTGTAACAGTAGAATCCCTGGTTT
GCGTTCTATAATGTAGATCTGTATCAGTGTGGCACTTCTTGT
GACTTTCCAGATTTAACACTAGAGATCACTCTGTATTAAGCT
CCTTAACTGTATGCTGTGGTACCTTAGGATTCGTGCTTAGGT
GGCGGTGGACGGTAGTCCCATCGTATACGGCCGCCTCTGTAC
GACAGAGGCCATAGGTGGCTGTACGCAGCCGTTAGTTTGAGG
CCTAAACCCGAGGTTGACCGTATATCTAAACCAATTCTGTAC
TAAGTCCTGTATATCACCACCTACGTGCACGGTTCAATGATT
"""
k=6

print(medianstring(dna,k))

