import sys
s=sys.stdin.readline()

if s[0]=='F': print("0.0")
elif s[0]=='D':
    if s[1]=='+': print(1.3)
    if s[1] == '0': print(1.0)
    if s[1] == '-': print(0.7)
elif s[0]=='C':
    if s[1]=='+': print(2.3)
    if s[1] == '0': print(2.0)
    if s[1] == '-': print(1.7)
elif s[0]=='B':
    if s[1]=='+': print(3.3)
    if s[1] == '0': print(3.0)
    if s[1] == '-': print(2.7)
elif s[0]=='A':
    if s[1]=='+': print(4.3)
    if s[1] == '0': print(4.0)
    if s[1] == '-': print(3.7)