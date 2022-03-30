def hamming_distance(p,q):
    c=0
    for i in range(len(p)):
        if p[i]!=q[i]:
            c+=1
    return c

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



dna="TTACCTTAAC GATATCTGTC ACGGCGTTCG CCCTAAAGAG CGTCAGAGGT"
pattern='AAA'

print(distancepatternstrings(pattern,dna))