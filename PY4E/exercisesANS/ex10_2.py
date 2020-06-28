# 10.2 Write a program to read through the mbox-short.txt and 
# figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and 
# then splitting the string a second time using a colon.

# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# Once you have accumulated the counts for each hour, print out the counts, 
# sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts=dict()
for line in handle:
    words=line.split()
    if len(words)<1 or words[0] != 'From':
        continue
    t=line.find(":")
    hr=line[t-2:t]
    counts[hr]=counts.get(hr,0)+1

### sorted by key(hr) ###
for key,val in sorted(counts.items()):
    print(key,val)

### sorted by value(time) ###
lst=list()
for key,val in counts.items():
    newtuple=(val,key)
    lst.append(newtuple)
lst=sorted(lst,reverse=True)
for val,key in lst:
    print(key,val)