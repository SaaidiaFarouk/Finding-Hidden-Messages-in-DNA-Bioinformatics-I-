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

strsss=Neighbors('AG',2)
for i in range(len(strsss)):
    print(strsss[i])
