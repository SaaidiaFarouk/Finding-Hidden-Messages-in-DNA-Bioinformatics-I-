def reverse_compliment(text):
    strr=''
    for i in range(len(text)):
        if text[i]=='A':
            strr='T'+strr
        elif text[i]=='T':
            strr='A'+strr
        elif text[i]=='G':
            strr='C'+strr
        elif text[i]=='C':
            strr='G'+strr
    return strr

text=('AAAACCCGGT')
print(reverse_compliment(text))
