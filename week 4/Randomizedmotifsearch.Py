import random
import math
def randomx(x):
    return random.randint(0, x)


def motifmatrixcreator(dna,t):
    dnas=dna
    dictt=dict()
    dictt['A']=list()
    dictt['C']=list()
    dictt['G']=list()
    dictt['T']=list()
    for i in range(len(dnas[0])):
        dictt['A'].append(0.1)
        dictt['C'].append(0.1)
        dictt['G'].append(0.1)
        dictt['T'].append(0.1)
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
            dictt[x][j]=dictt[x][j]/(t+0.4)
    return dictt
    

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


def scoree(Motifs,t,k):
    profile=motifmatrixcreator(Motifs,t)
    entropy=0.0
    val=0.0
    for i in range(k):
        for j in ['A','C','G','T']:
            val=profile[j][i]           
            x=math.log2(val)
            entropy=entropy-(val*x)     
    return entropy

dna="CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG TAGTACCGAGACCGAAAGAAGTATACAGGCGT TAGATCAAGTTTCAGGTGCACGTCGGTGAACC AATCCACCAGCTCCACGTGCAATGTTGGCCTA"
k=8
t=5
def greedy(dna,k,t):
    Bestmotifs=list()
    Motifs=list()
    list1=dna.split(" ")
    for i in range(t):
        x=(len(list1[0])-k)
        s=randomx(x)
        Motifs.append(list1[i][s:s+k])
    for i in range(t):
        Bestmotifs.append(Motifs[i])
    while True : 
        Profile=motifmatrixcreator(Motifs,t)
        Motifs=list()
        for i in range(t):
            Motifs.append(profilemostproba(Profile,list1[i],k))
        if scoree(Motifs,t,k)<scoree(Bestmotifs,t,k):
            Bestmotifs=list()
            for i in range(t):
                Bestmotifs.append(Motifs[i])
        else:
            return(Bestmotifs)

i=0
lastmotifs=greedy(dna,k,t)
while i<999:
    bestmotifs=greedy(dna,k,t)
    if scoree(bestmotifs,t,k)<scoree(lastmotifs,t,k):
        lastmotifs=bestmotifs[:]
        print(scoree(bestmotifs,t,k))
        print(lastmotifs)
    i=i+1
print(lastmotifs)
for i in range(len(lastmotifs)):
    print(lastmotifs[i])






        
        

        





        
















