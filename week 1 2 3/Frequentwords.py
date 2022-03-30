def patterncount(text,pattern):
    c=0
    for i in range(len(text)-len(pattern)+1):
        if text[i:i+len(pattern)]==pattern:
            c=c+1
    return c 

def Frequentwords(text,k):
    countt=list()
    freqwords=list()
    for i in range(len(text)-k+1):
        pattern=(text[i:i+k])
        countt.append(patterncount(text,pattern))
    m=max(countt)
    for i in range(len(countt)):
        if countt[i]==m and (text[i:i+k] not in freqwords) :
            freqwords.append(text[i:i+k])
    return freqwords

text=('TATTATACAAGACAACG')

print(Frequentwords(text,4))
            
    
        