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

def reverse_compliment(text):
    strr=''
    for i in range(len(text)):
        if text[i]=='A':
            strr='T'+strr
        elif text[i]=='T':
            strr='A'+strr
        elif text[i]=='G':
            strr='C'+strr
        elif text[i]=='C':
            strr='G'+strr
    return strr

def freqwordswithmismatches(text,k,d):
    patterns=list()
    freqmap={}
    n=len(text)
    for i in range(n-k+1):
        pattern=text[i:i+k]
        neighborhood=Neighbors(pattern,d)
        for j in range(len(neighborhood)-1):
            neighbor=neighborhood[j]
            if neighbor not in freqmap.keys():
                freqmap[neighbor]=1
            else:
                freqmap[neighbor]+=1
        rcneighborhood=Neighbors(reverse_compliment(pattern),d)
        for j in range(len(rcneighborhood)-1):
            neighbor=rcneighborhood[j]
            if neighbor not in freqmap.keys():
                freqmap[neighbor]=1
            else:
                freqmap[neighbor]+=1

    m=max(freqmap.values())
    for pattern in freqmap.keys():
        if freqmap[pattern]==m:
            patterns.append(pattern)
    return patterns


text=('')
k=7
d=2

lst=freqwordswithmismatches(text,k,d)
for i in range(len(lst)):
    print(lst[i])