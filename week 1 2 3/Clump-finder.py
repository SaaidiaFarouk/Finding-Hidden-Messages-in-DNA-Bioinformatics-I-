def patterncount(text,pattern):
    c=0
    for i in range(len(text)-len(pattern)+1):
        if text[i:i+len(pattern)]==pattern:
            c=c+1
    return c 

def frequency_table(text,k):
    countt=list()
    for i in range(len(text)-k+1):
        pattern=(text[i:i+k])
        countt.append(patterncount(text,pattern))
    return countt

def clumpfinder(text,k,l,t):
    clumps=list()
    for i in range(len(text)-l+1):
        sequence=(text[i:i+l])
        listt=frequency_table(sequence,k)
        for j in range(len(listt)):
            if listt[j]>=t and (sequence[j:j+k] not in clumps):
                clumps.append(sequence[j:j+k])
    return clumps

f=open('E_coli.txt')
t=f.read()
print(clumpfinder(t,9,500,))

