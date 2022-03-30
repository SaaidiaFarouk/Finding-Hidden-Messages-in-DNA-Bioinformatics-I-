f=open("out.txt","r")
d=open("refs.txt","a")
data = f.read().replace('\n', '')
lst=data.split(">")
seq=lst[1]
lstt=seq.split("|")
l=len(lstt)
carr=lstt[l-1]
n=carr.find("-")
gen=carr[n:len(carr)]
print(len(gen))
