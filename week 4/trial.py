dna="ATGAGGTC GCCCTAGA AAATAGAT TTGTGCTA"
motifs="GTC CCC ATA GCT"
k=3
t=4
def score(dict,pattern):
    scoree=1
    for i in range(len(pattern)):
        if pattern[i]=='A':
            val=float(dict['A'][i])
        if pattern[i]=='C':
            val=float(dict['C'][i])
        if pattern[i]=='G':
            val=float(dict['G'][i])
        if pattern[i]=='T':
            val=float(dict['T'][i])
        scoree=scoree*val
    return scoree
def profilemostproba(profile,text,k):
    profix=profile
    scoree=0
    for i in range(len(text)-k+1):
        pattern=text[i:i+k]
        if scoree<score(profix,pattern):
            scoree=score(profix,pattern)
            patternn=pattern
    return patternn
def motifmatrixcreatorrr(dna,t):
    dnas=dna
    dictt=dict()
    dictt['A']=list()
    dictt['C']=list()
    dictt['G']=list()
    dictt['T']=list()
    for i in range(len(dnas[0])):
        dictt['A'].append(0)
        dictt['C'].append(0)
        dictt['G'].append(0)
        dictt['T'].append(0)
    for i in range(t):
        for j in range(len(dnas[0])):
            if dnas[i][j]=='A':
                dictt['A'][j]=dictt['A'][j]+1
            elif dnas[i][j]=='C':
                dictt['C'][j]=dictt['C'][j]+1
            elif dnas[i][j]=='G':
                dictt['G'][j]=dictt['G'][j]+1
            elif dnas[i][j]=='T':
                dictt['T'][j]=dictt['T'][j]+1
    for x in ['A','C','G','T']:
        for j in range(len(dnas[0])):
            dictt[x][j]=dictt[x][j]/(t)
    return dictt
list1=list()
list1=dna.split(" ")
list2=motifs.split( )
profile=motifmatrixcreatorrr(list2,t)
for i in range(len(list1)):
    print(profilemostproba(profile,list1[i],k))


