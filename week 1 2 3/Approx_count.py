def hamming_distance(p,q):
    c=0
    for i in range(len(p)):
        if p[i]!=q[i]:
            c+=1
    return c

def approx_count(text,pattern,d):
    places=list()
    for i in range(len(text)-len(pattern)+1):
        if hamming_distance(pattern,text[i:i+len(pattern)])<=d:
            places.append(i)
    return places


pattern='GAGG'
text='TTTAGAGCCTTCAGAGG'
d=2
print(approx_count(text,pattern,d))