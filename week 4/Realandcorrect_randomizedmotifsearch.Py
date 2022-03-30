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
        dictt['A'].append(1)
        dictt['C'].append(1)
        dictt['G'].append(1)
        dictt['T'].append(1)
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
            dictt[x][j]=dictt[x][j]/(t+4)
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

def consensus(motifs,t,k):
    profile=motifmatrixcreatorrr(motifs,t)
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

def scoree(motifs,t,k):
    consen=consensus(motifs,t,k)
    sc=0
    for i in range(len(motifs)):
        dis=hamming_distance(consen,motifs[i])
        sc=sc+dis
    return sc

def scorex(Motifs,t,k):
    profile=motifmatrixcreator(Motifs,t)
    entropy=0.0
    val=0.0
    for i in range(k):
        for j in ['A','C','G','T']:
            val=profile[j][i]           
            x=math.log2(val)
            entropy=entropy-(val*x)     
    return entropy

def randomizedmotifdearch(dna,k,t):
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
        if scoree(Motifs,t,k)<scoree(Bestmotifs,t,k) :
            Bestmotifs=list()
            for i in range(t):
                Bestmotifs.append(Motifs[i])
        else:
            return(Bestmotifs)

dna="TCCGTGACGGTCTTCTAATTGAAACGTTGTTTGCATACGAAAGTATCTCAACGGCGCCGGTGATGAAGGCCATGTACGCGGTTAAAGCACCCAATATCGACGAATGCCTATGCTTGACCGTTACGCAGGTCCGGAGAACGTGAAGGGTTTGCCGGGCAACGAGCGTATAATCCGTGACGGTCTTC TAATTGAAACGTTGTTTGCATACGAAAGTATCTCAACGGCGCCGGTGATGAAGGCCATGTACGCGGTTAAAGCACCCAATATCGACGAATGAGGTGGCATCCTGGGCCTATGCTTGACCGTTACGCAGGTCCGGAGAACGTGAAGGGTTTGCCGGGCAACGAGCGTATAATCCGTGACGGTCTTC GGACCAGTAGTTCCTCAAATATGAACGCTGGCTTGCAGGCCTTAGCGAGCATCCTCACGCCACTCTAGTTCAGAGGTCTCATCTACTGTAAAATTGTGCTGGGCGTACACAATTTCGCCCGATGGTCCGTATCGTGACGCCCAGCAGAACAATTACAGTCTTGCGGACAAATAGAGACAAGCTTA GTCCAGTTAATATCCAAAGCATATTCGATGTAGATTTTCCCGCTCAGACGAGAAGCGAGGGTGCTTTGATCATTCGGGGGAGACAGTTGCACATTATGAGTCCTAGAGAGCGGCGATCCTGGCATGACTTGTAAAATCTGATTCTCAGTGAACGTTCGAATCCTATATGAAGGATAATCGCCCTA TTAATCGTCGCAGCAGGTCAACACAGCTAGACAACCCGTTAGAGGGGGCCAGATGTATAAATGTGCACGATCACTGTGCCGGTTTCGCGTGCTCGCCTAATACTCAAGTTATCGATTCATCGCAGACTCGTTTATTTGAGCGTAGATCCTGGGGGTTGTTTTGACCCGACACTGGCCCTTTTATG GAGAGATTATTTAGCAAAAGAGGAGGCTTGTAAGTTAAGAAAAACCATCTCAGCTGGCGGAGCATCCTGGGCGCGTTAGTGGCGAACGGACGTTGTAAAACTAGTGGTATATAGTGGAGTACTCGTTTACTTCCTTAACTACTTGCCAAGATGTTACTGAGGGAACAGAGTAGCGTAAAAAACGT AATTGTACCAGTACCGGCGTCACGTCCATCCCTTCCCTGCGCGTCCGGCAAATTGATGCCTATAGGGTACGTCCTATCCTTTTACACTCACGTATTAACGGGAGCCGACATCCTGGGCATTTTTAGGCTCCCCTTTACGAGCTGTACCATATTAGGCTTCCGCACCGTTCGGGCGACGCGTGTCA AATCGTTATCAGCCCGGTACACAGGTCTCTTAACGTACAGCAGGTAATTGAAGGCGCTAAAATTCGAGAACGGTGATAGGCAGGGAGCGATGTTCCTGGGCCACGTGCCAAAATTGCCGCGGTAATAGGAAGCCAACTAAAAGGCGGAACTTTTGTGGAACTCCCCGGCGGTATTACCATCTGCG ACTAGCATAATATCCTCTTCTTTGAGTCGACATGTGAGTACGCATCCTGGAGACTCAAGCCAGGAATAACGCTATTTTAGACGGCTCCACCGCAGTTAATGTTACTAGCGGTCCATAGAACTGGATTAGCTACGTTGGCGAGGTCCGAAAGGAACAAGACCGGTTCCTCACGACTCCGGTCTGTC ATTACCTTGCTTTTCTATCGCGCTTCGAGCCCAGAGCCAACCATCCCAATAGGATCCACAATTGACTTGGAAATAAACGAGGAGTGCTAGCTGATATCATGAAAAATTTGGAGATATCTAAGTGGAGTTAGCAACGACGTAGCATCCTGGAGAGCGTATACCCAAGATTGCCTATGCATGTCACA TATTATGTTCCTTCGTGTGTTGTTGCCTCATGTCTCGGAAGGCAAGATGCCGTTGTACCCCCAGCAACGGCAGTTCTAACTGTTCTTTTCCAGTGAGCTTACATCCTGGTGTATGGGGACCGATAGCGTGGAACAATGATGATAGGGTACCCCCACCCGTCGGGGCCTAATATTTTTTTCTCTAA GGTTACGCAGGCCATTTGGTCCGCACCTGCCGTTAGGATTGACCTCAAACTTCGTACAGATGTTTTATGGCTGCATGCGAGCATCCTGAGTAGACGACTATAGCTGAGCCCTGTAACTTTGGTTGCGTGTAAAACCAGGTGGTCAGCTGCGGTAGCAGGCAATTAGTGGCAAGTACTCCCCTGGT ACCGCCGTTGATTTCGGGATAATTTATCAAAACCACAAATGCGATAAGAGCGATGCTCCGACCTTCCACTAGCCCCGGACATTCCATACCAATTACGGAGATTGGATTAAAACTGTTAGTAGACGCGTATAAGACATTAACTGCCGAGCATCCTGGAAGCGGTTACCGCCATAGCCCTCGGGCGA TTAGGCACGGGAGACCCCGACCGTCCTTATAGCTAGCCTGCGGGCGCGGAGACTTCGAGCGAGCTCACTGGCGTGTCATTCCCTCGCAACGCAAACGCACCACGGACGCACGTAGCGCTGCCAAGTTTATCGGGAACTCGACGTGGAGCCGAAACGTGTAACATGGTAAGTTAGCGATAGTAAGA ATATATTTACTAGCTTGAGCGAGCATCGCAGACGCTTACTTGTAGTAGGTTGGATTGCAAACTGGAAGCCAGATAGCATTTTAGTCGGCTCCATCCTTCGTGATGGCGGTGTTATAGTCTCTGCTAATTTTGCCTCGTGCAAAGAAGTATAATCCACCACCTATCCGCATCGACTGTGGGAATAT TATTTGAAAACGATTAATTTCCACGGTCATACAGGAGCGAGCATAGGGGAAACTGTGGACAGTTTCCCTTTTCGTAGACCTCGCATGCCTAATACTAAGTGAGCGGTCATGTGTAAGCATATCGACTTATTACATTGTGTACGTTCGAATATGGTTAAGACCTATCTCACTTGGCGCGGTAGTCC TTAGTCGTCGATTTAGGGGTCGTCACGAGAGCTAATACAAGTTACAGATTACTTCTAACGAATAACTCCAAAGCCCTTGAATGCGATACCCGAACTAGATGGGCTGTGATGCTCTACCGCTTGCTCTTGGCACGGCCGATATTGAGAGAGCGAAGTTCCTGGCATTTTATACAATAATCTGGATG AATGGACAGGACCGTCCGTTTTCACTGGACCTAGAACGACGGGAAAAGTGACCTCCACGAGCGAGCACATTGGTAGGTCCTGACTGTTGAACCTTCCACTCGGGCACTTCGAGATGAATCAAGATATCCTTCACCTTTTACGGGGTAACGCGCCACAGGCGGTTATTGGAAGTAACTCCATGTAT ATATCGTAGGCTAGCTTTTCATGATCTCAAAAGTGTGGTCCGGTAGATCTTGTTTACGAACAAGAAAACCGTCCTCACGAGCGAGCATCCCAATCGGACTAGGACGTCCTTGGGAATACTCCAGCCCTGCGGTCGAAGGACTGAACCAACGAGGCCACCGAGTACGAGATTTTTTGAGTCGTTCG CCTACCCGCATGGGTTCTGGAAGGGGATTTATGTCTAGAGGTGGCATGATTGACACAGAGGGTGGACTAGGTACGGGATGCGCCCGAGCGAGTTCCCTGGTAGCGTGTATCCACCATGGATATTGCTTAGCGCGACCGGCTGGGGGTATCCGCCCTGGTGGACATCTGTCCCTCGGGTACAAATT"
k=15
t=20
i=0
list1=dna.split(" ")
random.seed(0)
x=list()
for j in range(t):
    a=random.randint(1,len(list1[0])-k)
    x.append(a)

lastmotifs=list()
for i in range(t):
    motif=list1[i][int(x[i]):int(x[i])+k]
    lastmotifs.append(motif)


while i<999:
    bestmotifs=randomizedmotifdearch(dna,k,t)
    if scoree(bestmotifs,t,k)<scoree(lastmotifs,t,k) :
        lastmotifs=bestmotifs[:]
        
    i=i+1
print(lastmotifs)
f=open("submissionn.txt","a")
for i in range(len(lastmotifs)):
    f.write(lastmotifs[i])
    f.write(" ")
for i in range(len(lastmotifs)):
    print(lastmotifs[i])
print(scoree(lastmotifs,t,k))
print(scorex(lastmotifs,t,k))
f.close()