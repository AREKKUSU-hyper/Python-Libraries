fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
# for line in fh:
#     if line.startswith("From"):
#         if not line.startswith("From:"):
#             words=line.split()
#             print(words[1])
#             count+=1
for line in fh:
    line=line.rstrip()
    words=line.split()

    # if len(words)<2:        # Guardian (make sure there's at least two words)
    #     continue
    # if line == "":        # another way to skip blank
    #     continue

    if len(words)<2 or words[0]!="From":    # Guardian 要放前面，不然還是有可能報錯
        continue         
    print(words[1])
    count+=1

print("There were", count, "lines in the file with From as the first word")


