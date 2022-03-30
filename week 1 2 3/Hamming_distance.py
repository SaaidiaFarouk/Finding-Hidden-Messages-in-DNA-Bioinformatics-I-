def hamming_distance(p,q):
    c=0
    for i in range(len(p)):
        if p[i]!=q[i]:
            c+=1
    return c


print(hamming_distance('GGGCCGTTGGT','GGACCGTTGAC'))