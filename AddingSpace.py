import re
ouptputstring = ""

inputstring = input("Nhap chuoi:")

for i in inputstring:
    if re.search("[A-Z]",i):
        lowkey = i.lower()
        char = " "+lowkey
        print(char)
        inputstring = inputstring.replace(i,char)


print(inputstring)