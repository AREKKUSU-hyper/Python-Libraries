# List Comprehension

# lst=list()
# for key,val in counts.items():
#     newtuple=(val,key)
#     lst.append(newtuple)

### Short Version ###
c={"a":10,"b":1,"c":22} 
print(sorted([(v,k) for k,v in c.items()]))