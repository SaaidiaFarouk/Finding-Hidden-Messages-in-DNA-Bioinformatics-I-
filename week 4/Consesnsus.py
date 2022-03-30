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

def consensus(motifs,k,t):
    profile=motifmatrixcreatorrr(motifs,t)
    print(profile)
    consen=''
    for i in range(k) :
        m=float()
        list1=list()
        for j in ['A','C','G','T']:
            list1.append(profile[j][i])
        m=max(list1)
        x=list1.index(m)
        g=''
        if x == 0:
            g='A'
        if x == 1:
            g='C'
        if x == 2:
            g='G'
        if x == 3:
            g='T'
        consen=consen + g 
    return consen

def hamming_distance(p,q):
    c=0
    for i in range(len(p)):
        if p[i]!=q[i]:
            c+=1
    return c

def scoree(motifs,k,t):
    consen=consensus(motifs,k,t)
    sc=0
    for i in range(len(motifs)):
        dis=hamming_distance(consen,motifs[i])
        sc=sc+dis
    return sc


k=12
t=10
motifs=['TCGGGGGTTTTT','CCGGTGACTTAC','ACGGGGATTTTC','TTGGGGACTTTT','AAGGGGACTTCC','TTGGGGACTTCC','TCGGGGATTCAT','TCGGGGATTCCT','TAGGGGAACTAC','TCGGGTATAACC']
print(scoree(motifs,k,t))
print(consensus(motifs,k,t))