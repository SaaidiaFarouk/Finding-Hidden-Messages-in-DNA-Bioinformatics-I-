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

print(frequency_table('ATCGATCGATCG',4))