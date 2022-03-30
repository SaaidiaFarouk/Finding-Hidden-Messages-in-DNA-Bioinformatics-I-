def skewcalculator(text):
    skews=list()
    c=0
    skews.append(c)
    for i in range(len(text)):
        if text[i]=='C':
            c=c-1
        elif text[i]=='G':
            c=c+1
        skews.append(c)
    m=min(skews)
    places=list()
    for i in range(len(skews)):
        if skews[i]==m:
            places.append(i)
    return places
f=open('E_coli.txt','r')
t=f.read()

print(skewcalculator(t))
