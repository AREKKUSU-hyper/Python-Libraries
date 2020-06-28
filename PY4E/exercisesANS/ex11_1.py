import re
# x="From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
# y1=re.findall('\S+?@\S+?' ,x)
# y2=re.findall('\S@\S+?' ,x)
# y3=re.findall('\S+?@\S+' ,x)
# print(y1)
# print(y2)
# print(y3)

test = input("Is this test: y/n:")
if test=="y":
    fname = "regex_sum_42.txt"
elif test=="n":
    fname = "regex_sum_351868.txt"
else:
    print("wrong input")
    quit()

fh = open(fname,"r")

numlst=list()
for line in fh:
    if line == "":
        continue
    line=line.rstrip()
    nums=re.findall('[0-9]+',line)
    if len(nums) == 0:
        continue
    for num in nums:
        numlst.append(int(num))

count=0
for num in numlst:
    count+=num

print(count)

###  two-line version ###
#print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )

# ————————————————
# import re

# file = open('regex_sum_35430.txt')
# file_data = file.read()
# numbers_str = re.findall('[0-9]+',file_data)
# total = 0
# for number_str in numbers_str:
#     total = total + int(number_str)
# print(total)
# ————————————————