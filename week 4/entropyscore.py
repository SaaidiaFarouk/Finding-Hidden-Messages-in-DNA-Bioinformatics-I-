import math
def motifmatrixcreator(dna,t):
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
            dictt[x][j]=(dictt[x][j]/t) 
    return dictt

def score(Motifs,t,k):
    profile=motifmatrixcreator(Motifs,t)
    print(profile)
    entropy=0.0
    colentropy=0.0
    val=0.0
    for i in range(k):
        for j in ['A','C','G','T']:
            val=profile[j][i]
            if val==0.0:
                x=0
            else:
                x=math.log2(val)
            entropy=entropy-(val*x)
            
    return entropy

motifs=['AAAAA','CCCCC','GGGGG','TTTTT']
print(score(motifs,4,5))
    

    
        





