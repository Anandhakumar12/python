import string
lwwe = list(string.ascii_lowercase)

l1 = list(input())
l2 = list(input())
l3 = []
for z in range(len(l1)):
    rw = lwwe.index(l1[z])+lwwe.index(l2[z])+1
    if rw < 25:
        print(lwwe[rw],end = "")
    else:
        print(lwwe[rw-26],end = "")
