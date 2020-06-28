num=0
tot=0.0
while True:
    sval=input("Enter a number: ")
    if sval == "done":
        break
    try:
        fval = float(sval)
    except:
        print("Invalid input")
        continue

    num+=1
    tot+=fval

print("Sum:",tot,"|Num:",num,"|Avg:",tot/num)