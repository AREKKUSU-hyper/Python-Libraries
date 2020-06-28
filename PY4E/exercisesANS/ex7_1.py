f=open("mbox.txt","r")
# inp=f.read()    # Reads the entire file into the variable inp as a string
# print(len(inp)) # how many characters
# print(inp[:10]) # 換行符號算一個字元

for line in f:
    line=line.rstrip() # 去掉文件中的分行符號(空白)
    if line.startswith("From"):
    # if not line.startswith("From"):  # opposite
    #     continue
        if not "Q" in line:
            continue
        print(line)
    
