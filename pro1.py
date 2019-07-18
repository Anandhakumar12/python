l1=int(input())
n=[]
for i in range(1l):
  c=input()
  n.append(c)
f=[]
for i in zip(*n):
  if(i.count(i[0])==len(i)):
    f.append(i[0])
  else:
    break
print(''.join(f))
