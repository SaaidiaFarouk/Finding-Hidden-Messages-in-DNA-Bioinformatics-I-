def imediate_neighboor(pattern):
    imediate_neighboorhood=list()
    for i in range(len(pattern)):
        patternn=list(pattern)
        for x in ['A','C','T','G']:
            if x!= pattern[i]:
                patternn[i]=x
                patternnn=''
                for y in range(len(patternn)):
                    patternnn=patternnn+patternn[y]
                imediate_neighboorhood.append(patternnn)
    return imediate_neighboorhood
    
print(imediate_neighboor('ATT'))

