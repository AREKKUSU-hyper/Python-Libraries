fname=input("Enter the file name:")
try:
    fhand=open(fname)
except:
    print("File cannot be opened:", fname)
    quit()

count=0
for line in fhand:
    line=line.rstrip()
    if line.startswith("From"):
        count+=1
print("There were", count, "From line in",fname)