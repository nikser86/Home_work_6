import collections

li = ''
with open("1.txt") as inp_file:
    for line in inp_file:
        li = li + ' ' + line.rstrip()
print(li)
li_s = sorted(li.split())
st = collections.Counter(li_k for li_k in li_s)
for item in st:
    with open("2.txt", 'a') as outFile:
        print(item+'     '+str(st[item]),file=outFile)