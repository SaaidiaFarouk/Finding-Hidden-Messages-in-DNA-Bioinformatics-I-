import random 
random.seed(2017)
x=list()
for i in range(5):
    a=random.randint(1,25)
    x.append(a)


dna="CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG TAGTACCGAGACCGAAAGAAGTATACAGGCGT TAGATCAAGTTTCAGGTGCACGTCGGTGAACC AATCCACCAGCTCCACGTGCAATGTTGGCCTA"
k=8
t=5
list1=dna.split(" ")
lastmotifs=list()
for i in range(t):
    motif=list1[i][int(x[i]):int(x[i])+k]
    lastmotifs.append(motif)
print(lastmotifs)









