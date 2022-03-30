def motifmatrixcreator(dna,t):
    dnas=dna.split()
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
        for j in range(len(dnas[i])):
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
            dictt[x][j]=dictt[x][j]/10
    return dictt


dna="""AAG
GGT
CTG
"""
t=3


print(motifmatrixcreator(dna,t))

