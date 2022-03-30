def pattern_position(text,pattern):
    k=len(pattern)
    positions=list()
    for i in range(len(text)-k+1):
        if text[i:i+k]==pattern:
            positions.append(i)
    return positions

text=('GATATATGCATATACTT')
pattern=('ATAT')
print(pattern_position(text,pattern))