# simplified counting with get()

# dict.get(key, default=None)
# key -- 字典中要查找的键。
# default -- 如果指定键的值不存在时，返回该默认值。

counts=dict()
names=["Alice","Bob","Bob","Cheryl","Cheryl","Cheryl"]
for name in names:
    counts[name]=counts.get(name,0)+1
print(counts)
print(counts.keys())    # list of keys
print(counts.values())  # list of values
print(counts.items())   # list of key-value tuples

for key,value in counts.items():
    print(key,value)
# ^ same as v
# for key in counts:
#     print(key,counts[key])


