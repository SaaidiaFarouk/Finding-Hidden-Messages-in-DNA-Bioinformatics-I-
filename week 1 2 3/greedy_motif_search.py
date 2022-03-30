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
    profix=dict()

    nucleotides=profile.split('\n')
    profix['A']=nucleotides[0].split()
    profix['C']=nucleotides[1].split()
    profix['G']=nucleotides[2].split()
    profix['T']=nucleotides[3].split()
    scoree=0
    for i in range(len(text)-k+1):
        pattern=text[i:i+k]
        if scoree<score(profix,pattern):
            scoree=score(profix,pattern)
            patternn=pattern
    return patternn

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
    for i in range(t-1):
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
            dictt[x][j]=dictt[x][j]/10
    return dictt

def scorex(matrix,k,t):
    listtt=list()
    score=0
    for i in range(k):
        for x in ['A','C','G','T']:
            listtt.append(matrix[x][i])
            m=max(listtt)
            v=t-m
            score=score+v
    return score



def greedymotifsearch(dna,k,t):
    dnas=dna.split()
    motifs=list()
    for i in range(len(dnas)):
        motifs.append(dnas[i][0:k])
    bestmotifs=motifmatrixcreator(motifs,t)
    listt=list()
    for i in range(len(dnas[0])):
        motif1=dnas[0][i:i+k]
        listt.append(motif1)
        for i in range(2,t):
            profile=motifmatrixcreator(listt,t)
            listt.append(profilemostproba(profile,dnas[i],k))
            matrixx=motifmatrixcreator(listt,t)
            listtscore=scorex(matrixx,k,t)
            matrixxscore=scorex(bestmotifs,k,t)
            if listtscore < matrixxscore:
                motifs=listt
    return motifs

dna="""GGCGTTCAGGCA
AAGAATCAGTCA
CAAGGAGTTCGC
CACGTCAATCAC
CAATAATATTCG"""
k=3
t=5

print(greedymotifsearch(dna,k,t))