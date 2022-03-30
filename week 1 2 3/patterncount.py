def patterncount(text,pattern):
    c=0
    for i in range(len(text)-len(pattern)+1):
        if text[i:i+len(pattern)]==pattern:
            c=c+1
    return c 

text='GCGGCGCTGCTAGCGTCAAACGTCGTACGCGTAGCCATTCAAGGCAAA'
pattern=('GCG')

print(patterncount(text,pattern))
