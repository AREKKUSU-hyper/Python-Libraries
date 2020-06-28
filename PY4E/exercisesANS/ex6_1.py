# string library
greet="Hello"
print(greet.lower())
print("Hi There".upper())
print("aBcd".capitalize())

print("AbcD".lower()=="abCd".lower())

greet="Hello Bob"
g2=greet.replace("Bob","Jane")
print(g2)

print(greet.startswith("h"))
print(greet.startswith("Hello"))

s="    stripping @BTC whitespace    "
print(s.lstrip())
print(s.rstrip())
print(s.strip())

nextfindstart=s.find("@")
spaceafter_mouse=s.find(" ",nextfindstart)
btc=s[nextfindstart+1:spaceafter_mouse]
print(nextfindstart)
print(spaceafter_mouse)
print(btc)

text = "X-DSPAM-Confidence:    0.8475"
t=text.find(" ")
num=float(text[t:].strip())
print(num)