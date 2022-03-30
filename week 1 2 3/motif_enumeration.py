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
    Neighborhood=list()
    if d==0:
        Neighborhood.append(Pattern)
        return Neighborhood
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


def MotifEnumeration(Dna, k, d):
    Patterns=list()
    seqlist=Dna.split( )
    frst=seqlist[0]
    neighborhood=list()
    for i in range(len(frst)-k+1):
        pattern=frst[i:i+k]
        neighborhood=Neighbors(pattern,d)
        for neighbor in neighborhood :
            c=0
            for seq in seqlist:
                neighborhoood=list()
                for f in range(len(seq)-k+1):
                    diff=seq[f:f+k]
                    neighboorhood=Neighbors(diff,d)
                    for g in range(len(neighboorhood)):
                        neighborhoood.append(neighboorhood[g])
                if neighbor in neighborhoood : 
                    c+=1
            if c==len(seqlist):
                Patterns.append(neighbor)
    Patterns.sort()
    patterns=list()
    for i in range(len(Patterns)):
        if Patterns[i] not in patterns :
            patterns.append(Patterns[i])
    return patterns


Dna="""GGGCATTGATTATCGCTCGCCCGGC
TAGCTGGGCGCAACCCGACGCGAGA
GGGCTCCTCGTGGCGGGCTAAACGT
TGAACGGGCTCAACAGAAGCGCTTG
GGGCAGTATCGTGGCATTGCCCGCT
CCAAGTATATCCTTGATACCGGGCT
"""
lst=MotifEnumeration(Dna,5,1)
for i in range(len(lst)):
    print(lst[i])



        


