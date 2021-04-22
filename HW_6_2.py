inp_file = open("1.txt")
li=''
for line in inp_file:
    li = li + line.rstrip() + "!\n"
    print(line.rstrip() + "!",li)
inp_file.close()
with open("1.txt",'w') as out_file:
    out_file.write(li)

with open("1.txt",'a') as out_file:
    print("Hello",file=out_file)



