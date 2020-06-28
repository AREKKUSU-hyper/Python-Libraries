# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count=0
tot=0.0
s1=len("X-DSPAM-Confidence:")
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"): 
    	continue
    s2=line.find("X-DSPAM-Confidence:")
    num=float(line[s2+s1+1:].strip())
    count+=1
    tot+=num

Avg=tot/count
print("Average spam confidence:",Avg)