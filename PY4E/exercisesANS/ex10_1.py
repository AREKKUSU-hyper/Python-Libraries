# The top ten most common words # tuple用value排序

name=input("Enter file:")
handle=open(name)

counts=dict()
for line in handle:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1

lst=list()
for key,val in counts.items():
    newtuple=(val,key)
    lst.append(newtuple)

lst=sorted(lst,reverse=True) # 從大到小排序

for val,key in lst[:10]:
    print(key,val)